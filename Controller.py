from tkinter import *
import urllib.request
import json
import tkinter.messagebox
import linecache
from tkinter import messagebox
import View
import Model
#from Model import updateInfomation
# constructor of the class App
class App(Tk):
    class __impl:
        def spam(self):
            return id(self)
    __instance = None

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # create a dictionary of variables for all the classes to share

        self.shared_data={
            #  a variable that shared by functions in the StartPage and SearchPage for establishing the chosen Database
            "dbOption":StringVar(),
            # variables to be shared by SearchPage and InfoPage, to store the movie info data
            "title":StringVar(),
            "year": StringVar(),
            "dire": StringVar(),
            "actors": StringVar(),
            "plot": StringVar()
        }
        
        #Setup Frame
        container=Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self['bg'] = 'black'
        
        self.frames={}

        for F in (StartPage, SearchPage, InfoPage, WishPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(StartPage)

        # create singleton instance

        # check if instance exists already
        if App.__instance is None:
            # create and remember instance
            App.__instance = App.__impl()
        # store instance reference as the only member in the handle
        self.__dict__['_App_instance'] = App.__instance

        def __getattr__(self, attr):
            """ Delegate access to implementation """
            return getattr(self.__instance, attr)

        def __setattr__(self, attr, value):
            """ Delegate access to implementation """
            return setattr(self.__instance, attr, value)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

movies = [] # global list of movie names for the wishlist
comments = []
ratings = []
# creating a class for the StartPage window
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def upWishList(self): # this function reads the text in the savedmovie.txt and saves it in the global variable test
            txt = open("savedmovies.txt", "r")
            lines = txt.readlines() # this creates a list containing every line in the text file
            movies.clear()
            for l in lines: # looping through the movie names list
                movies.append(l) # and appending them to the global list "movies"
            movies.append(' ')
            txt.close()
            comTxt = open("savedComment.txt", "r")
            ratTxt = open("savedratings.txt", "r")
            comLines = comTxt.readlines() # this creates a list containing every line in the text file
            ratLines = ratTxt.readlines() # this creates a list containing every line in the text file
            comments.clear()
            for c in comLines: # looping through the movie names list
                comments.append(c) # and appending them to the global list "movies"
            ratings.clear()
            for r in ratLines: # looping through the movie names list
                ratings.append(r) # and appending them to the global list "movies"
            comTxt.close()
            ratTxt.close()
            print(movies)

        # set the value of the global StringVar "dbOption" to "1" for OMDb
        def dbPickOMDb(event):
            View.startPageDbView(1)
            controller.shared_data["dbOption"]="1"

        # set the value of the global StringVar "dbOption" to "2" for IMDb
        def dbPickIMDb(event):
            View.startPageDbView(2)
            controller.shared_data["dbOption"]="2"
        
        frame = View.startFrame(Frame, self)
        
        # a wishlist button in the top right corner of the window for ease of navigation
        wishlist = Button(frame, text='Wishlist', height=1, width=2, command=lambda: controller.show_frame(WishPage),bg='black', fg='orange', font=("Arial", "8", "italic"), highlightcolor='orange')
        wishlist.pack(side=TOP, ipadx=20, anchor='e')
        wishlist.bind("<Button-1>", upWishList)
        #def startLayout(frame):
        View.startPageLayout(frame)
        
        # button for TMDb
        btn_IMDb = Button(frame, text="IMDb", bg='white', fg='black', anchor=CENTER, command=lambda: controller.show_frame(SearchPage),highlightcolor='orange')
        btn_IMDb.pack(padx=10, pady=2)
        btn_IMDb.bind("<Button-1>", dbPickIMDb)

        # button for OMDb
        btn_OMDb = Button(frame, text="OMDb", bg='white', fg='black', anchor=CENTER, command=lambda: controller.show_frame(SearchPage),highlightcolor='orange')
        btn_OMDb.pack(padx=10, pady=2)
        btn_OMDb.bind("<Button-1>", dbPickOMDb)

# create class for the SearchPage
class SearchPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def upWishList(self): # this function reads the text in the savedmovie.txt and saves it in the global variable test
                txt = open("savedmovies.txt", "r")
                lines = txt.readlines() # this creates a list containing every line in the text file
                movies.clear()
                for l in lines: # looping through the movie names list
                    movies.append(l) # and appending them to the global list "movies"
                movies.append(' ')
                txt.close()
                comTxt = open("savedComment.txt", "r")
                ratTxt = open("savedratings.txt", "r")
                comLines = comTxt.readlines() # this creates a list containing every line in the text file
                ratLines = ratTxt.readlines() # this creates a list containing every line in the text file
                comments.clear()
                for c in comLines: # looping through the movie names list
                    comments.append(c) # and appending them to the global list "movies"
                ratings.clear()
                for r in ratLines: # looping through the movie names list
                    ratings.append(r) # and appending them to the global list "movies"
                comTxt.close()
                ratTxt.close()
                print(movies)
        
        # defining the search function behind the search button
        def searchMovie(event):
            moviename = searchBox.get()
            title=moviename.replace(' ','-')

            if controller.shared_data["dbOption"]=="1":
                url='https://www.omdbapi.com/?t=' + title + '&apikey=244bde45'
                View.searchDbURL(url, 1, 0)
                # using the urllib.request library we can access urls from within our app, without the need of a browser
                json_obj = urllib.request.urlopen(url)
                data = json.load(json_obj)

                controller.shared_data["title"] = data['Title']
                controller.shared_data["year"] = data['Year']
                controller.shared_data["dire"] = data['Director']
                controller.shared_data["actors"] = data['Actors']
                controller.shared_data["plot"] = data['Plot']
                View.searchDbURL(url, 1, 1)

            elif controller.shared_data["dbOption"]=="2":
                url='https://api.themoviedb.org/3/search/movie?api_key=da097a759910eefff9e3098e9e3d3870&query=' + title
                View.searchDbURL(url, 2, 1)

                json_obj = urllib.request.urlopen(url)
                data = json.load(json_obj)

                # because the JSON from TMDb is organized innto a list of more movie elements, the use of a for loop to go through it is necessary
                # for the purpose of this application we will only use the first movie entry in the list (supposing it will be the most relevant
                for element in data['results']:
                    controller.shared_data["title"] = element['title']
                    controller.shared_data["year"] = element['release_date']
                    controller.shared_data["dire"] = "N/A"
                    controller.shared_data["actors"] = "N/A"
                    controller.shared_data["plot"] = element['overview']
                    View.searchDbURL(url, 2, 1)
                    break
            else:
                View.searchDbURL(url, 4, 1)

            View.searchDbURL("endofsearch", 3, 1)

        frame = View.startFrame(Frame, self)

        # a home button in the top right side of the window for ease of access, could also be an image button with a bit of struggle
        # img=PhotoImage(file="hb.png", width=30, height=30)
        home=Button(frame, text='Home', command=lambda : controller.show_frame(StartPage),font=("Arial","8","italic"), width=5, height=2,bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        View.searchPageLayout(frame)
        
        # input box
        searchBox = Entry(frame)
        searchBox.pack(pady=5)
        
        # search button in line with the input box
        searchBtn = Button(frame, text="Search", bg='white', fg='black',highlightcolor='orange', command=lambda: controller.show_frame(InfoPage))
        searchBtn.bind("<Button-1>", searchMovie)
        # searchBtn.bind("<Button-1>", lambda x: controller.show_frame(InfoPage))
        searchBtn.pack(pady=10)

        # RANDOM button underneath input box
        randomBtn = Button(frame, text="Random", bg='white', fg='black', command=lambda: controller.show_frame(InfoPage),highlightcolor='orange')
        randomBtn.pack()

        # WISHLIST in line with Random button
        wishBtn = Button(frame, text="Wishlist", bg='white', fg='black', command=lambda: controller.show_frame(WishPage),highlightcolor='orange')
        wishBtn.pack()
        wishBtn.bind("<Button-1>", upWishList)
# a class for the page where we output the movie info from the database
class InfoPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        def upWishList(self): # this function reads the text in the savedmovie.txt and saves it in the global variable test
            txt = open("savedmovies.txt", "r")
            lines = txt.readlines() # this creates a list containing every line in the text file
            movies.clear()
            for l in lines: # looping through the movie names list
                movies.append(l) # and appending them to the global list "movies"
            movies.append(' ')
            txt.close()
            comTxt = open("savedComment.txt", "r")
            ratTxt = open("savedratings.txt", "r")
            comLines = comTxt.readlines() # this creates a list containing every line in the text file
            ratLines = ratTxt.readlines() # this creates a list containing every line in the text file
            comments.clear()
            for c in comLines: # looping through the movie names list
                comments.append(c) # and appending them to the global list "movies"
            ratings.clear()
            for r in ratLines: # looping through the movie names list
                ratings.append(r) # and appending them to the global list "movies"
            comTxt.close()
            ratTxt.close()
            print(movies)
            
        def updateInfo():
            nameInfo_lbl.configure(text=controller.shared_data["title"])
            yearInfo_lbl.configure(text=controller.shared_data["year"])
            directorInfo_lbl.configure(text=controller.shared_data["dire"])
            castInfo_lbl.configure(text=controller.shared_data["actors"])
            descriptionInfo_lbl.configure(text=controller.shared_data["plot"])
            
            View.InfoMoviePrint(movies, 2)
        framelist = View.infoFrame(Frame, self)    
        
        View.infoPageLayout(framelist)
        
        # wishlist button top right corner, ease of access
        wishlist = Button(framelist[0], text='Wishlist', height=2, width=6, command=lambda: controller.show_frame(WishPage), font=("Arial", "8", "italic"), bg='black', fg='orange', highlightcolor='orange')
        wishlist.pack(side=RIGHT, anchor='ne')
        wishlist.bind("<Button-1>", upWishList)
        
        # img=PhotoImage(file="hb.png", width=30, height=30)
        home = Button(framelist[0], text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        # a button to force-update the info labels
        refresh = Button(framelist[1], text="Refresh Page", bg='black', fg='orange', command=updateInfo)
        refresh.pack(side=RIGHT)

        # "Add to wishlist" button on the right of the window
        addToWishBtn = Button(framelist[1], text="Add to wishlist", bg='gray', fg='white', command=lambda:Model.saveMovie(controller.shared_data["title"]))
        addToWishBtn.pack(side=RIGHT, pady=5, padx=5)

        # labels for info on the right
        nameInfo_lbl = Label(framelist[2], text="info", bg='black', fg='white')
        nameInfo_lbl.pack(side=LEFT, padx=15, pady=5)
    
        yearInfo_lbl = Label(framelist[3], text="info", bg='black', fg='white')
        yearInfo_lbl.pack(side=LEFT, padx=15, pady=5)
    
        directorInfo_lbl = Label(framelist[4], text="info", bg='black', fg='white')
        directorInfo_lbl.pack(side=LEFT, padx=15, pady=5)
    
        castInfo_lbl = Label(framelist[5], text="info", bg='black', fg='white')
        castInfo_lbl.pack(side=LEFT, padx=15, pady=5)
    
        descriptionInfo_lbl = Label(framelist[6], text="info", bg='black', fg='white')
        descriptionInfo_lbl.pack(side=LEFT, padx=15, pady=5)
    
        


class WishPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        l = PanedWindow(self, bg='black')
        l.pack(fill=X)
    
        home = Button(l, text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        lbl_logo = Label(l, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=10, side=LEFT)

        header = PanedWindow(self, orient=HORIZONTAL, bg='black')
        header.pack(fill=X)

        def updateWishy():
            moviename.configure(text= "1) Title:     " + movies[0])
            moviecomment.configure(text= "Comment:    " + comments[0])
            movierate.configure(text= "Star Rating:     " + ratings[0])
            movie1name.configure(text= "2) Title:     " + movies[1])
            movie1comment.configure(text= "Comment:    " + comments[1])
            movie1rate.configure(text= "Star Rating:     " + ratings[1])
            movie2name.configure(text= "3) Title:     " + movies[2])
            movie2comment.configure(text= "Comment:    " + comments[2])
            movie2rate.configure(text= "Star Rating:     " + ratings[2])
            movie3name.configure(text= "4) Title:     " + movies[3])
            movie3comment.configure(text= "Comment:    " + comments[3])
            movie3rate.configure(text= "Star Rating:     " + ratings[3])
            movie4name.configure(text= "5) Title:     " + movies[4])
            movie4comment.configure(text= "Comment:    " + comments[4])
            movie4rate.configure(text= "Star Rating:     " + ratings[4])
            movie5name.configure(text= "6) Title:     " + movies[5])
            movie5comment.configure(text= "Comment:    " + comments[5])
            movie5rate.configure(text= "Star Rating:     " + ratings[5])
            movie6name.configure(text= "7) Title:     " + movies[6])
            movie6comment.configure(text= "Comment:    " + comments[6])
            movie6rate.configure(text= "Star Rating:     " + ratings[6])
            movie7name.configure(text= "8) Title:     " + movies[7])
            movie7comment.configure(text= "Comment:    " + comments[7])
            movie7rate.configure(text= "Star Rating:     " + ratings[7])
            movie8name.configure(text= "9) Title:     " + movies[8])
            movie8comment.configure(text= "Comment:    " + comments[8])
            movie8rate.configure(text= "Star Rating:     " + ratings[8])
            movie9name.configure(text= "10) Title:     " + movies[9])
            movie9comment.configure(text= "Comment:    " + comments[9])
            movie9rate.configure(text= "Star Rating:     " + ratings[9])
            movieList.mainloop()
            
        refresh=Button(header,text="Refresh Page", bg='black', fg='orange', command= updateWishy)
        refresh.pack(side=RIGHT)
        
        Titleline1 = linecache.getline("savedmovies.txt", 1)
        Titleline2 = linecache.getline("savedmovies.txt", 2)
        Titleline3 = linecache.getline("savedmovies.txt", 3)
        Titleline4 = linecache.getline("savedmovies.txt", 4)
        Titleline5 = linecache.getline("savedmovies.txt", 5)
        Titleline6 = linecache.getline("savedmovies.txt", 6)
        Titleline7 = linecache.getline("savedmovies.txt", 7)
        Titleline8 = linecache.getline("savedmovies.txt", 8)
        Titleline9 = linecache.getline("savedmovies.txt", 9)
        Titleline10 = linecache.getline("savedmovies.txt", 10)

        Rateline1 = linecache.getline("savedRatings.txt", 1)
        Rateline2 = linecache.getline("savedRatings.txt", 2)
        Rateline3 = linecache.getline("savedRatings.txt", 3)
        Rateline4 = linecache.getline("savedRatings.txt", 4)
        Rateline5 = linecache.getline("savedRatings.txt", 5)
        Rateline6 = linecache.getline("savedRatings.txt", 6)
        Rateline7 = linecache.getline("savedRatings.txt", 7)
        Rateline8 = linecache.getline("savedRatings.txt", 8)
        Rateline9 = linecache.getline("savedRatings.txt", 9)
        Rateline10 = linecache.getline("savedRatings.txt", 10)
        
        Commentline1 = linecache.getline("savedComment.txt", 1)
        Commentline2 = linecache.getline("savedComment.txt", 2)
        Commentline3 = linecache.getline("savedComment.txt", 3)
        Commentline4 = linecache.getline("savedComment.txt", 4)
        Commentline5 = linecache.getline("savedComment.txt", 5)
        Commentline6 = linecache.getline("savedComment.txt", 6)
        Commentline7 = linecache.getline("savedComment.txt", 7)
        Commentline8 = linecache.getline("savedComment.txt", 8)
        Commentline9 = linecache.getline("savedComment.txt", 9)
        Commentline10 = linecache.getline("savedComment.txt", 10)
        
        movieList = PanedWindow(self, orient=HORIZONTAL, bg='black')
        movieList.pack(fill='both', expand=True)
        
        #movieid = Label(movieList, text="ID:       " + subMenu[0] [0], bg='black', fg='white')
       # movieid.grid(column=0, row=5, sticky=W)
        moviename = Label(movieList, text="1) Title:     " + Titleline1, bg='black', fg='white')
        moviename.grid(column=1, row=5, sticky=W)
        moviecomment = Label(movieList, text="Comment:    " + Commentline1, bg='black', fg='white')
        moviecomment.grid(column=2, row=5, sticky=W)
        movierate = Label(movieList, text="Star Rating:     "+ Rateline1, bg='black', fg='white')
        movierate.grid(column=3, row=5, sticky=W)
        
        #movie1id = Label(movieList, text="ID:       " + subMenu[1] [0], bg='black', fg='white')
        #movie1id.grid(column=0, row=6, sticky=W)
        movie1name = Label(movieList, text="2) Title:     " + Titleline2, bg='black', fg='white')
        movie1name.grid(column=1, row=6, sticky=W)
        movie1comment = Label(movieList, text="Comment:    " + Commentline2, bg='black', fg='white')
        movie1comment.grid(column=2, row=6, sticky=W)
        movie1rate = Label(movieList, text="Star Rating:     "+ Rateline2, bg='black', fg='white')
        movie1rate.grid(column=3, row=6, sticky=W)
        
       # movie2id = Label(movieList, text="ID:       " + subMenu[2] [0], bg='black', fg='white')
       # movie2id.grid(column=0, row=7, sticky=W)
        movie2name = Label(movieList, text="3) Title:     " + Titleline3, bg='black', fg='white')
        movie2name.grid(column=1, row=7, sticky=W)
        movie2comment = Label(movieList, text="Comment:    " + Commentline3, bg='black', fg='white')
        movie2comment.grid(column=2, row=7, sticky=W)
        movie2rate = Label(movieList, text="Star Rating:     "+ Rateline3, bg='black', fg='white')
        movie2rate.grid(column=3, row=7, sticky=W)
        
       # movie3id = Label(movieList, text="ID:       " + subMenu[3] [0], bg='black', fg='white')
       # movie3id.grid(column=0, row=8, sticky=W)
        movie3name = Label(movieList, text="4) Title:     " + Titleline4, bg='black', fg='white')
        movie3name.grid(column=1, row=8, sticky=W)
        movie3comment = Label(movieList, text="Comment:    " + Commentline4, bg='black', fg='white')
        movie3comment.grid(column=2, row=8, sticky=W)
        movie3rate = Label(movieList, text="Star Rating:     "+ Rateline4, bg='black', fg='white')
        movie3rate.grid(column=3, row=8, sticky=W)
        
        #movie4id = Label(movieList, text="ID:       " + subMenu[4] [0], bg='black', fg='white')
        #movie4id.grid(column=0, row=9, sticky=W)
        movie4name = Label(movieList, text="5) Title:     " + Titleline5, bg='black', fg='white')
        movie4name.grid(column=1, row=9, sticky=W)
        movie4comment = Label(movieList, text="Comment:    " + Commentline5, bg='black', fg='white')
        movie4comment.grid(column=2, row=9, sticky=W)
        movie4rate = Label(movieList, text="Star Rating:     "+ Rateline5, bg='black', fg='white')
        movie4rate.grid(column=3, row=9, sticky=W)
        
       # movie5id = Label(movieList, text="ID:       " + subMenu[5] [0], bg='black', fg='white')
      #  movie5id.grid(column=0, row=10, sticky=W)
        movie5name = Label(movieList, text="6) Title:     " + Titleline6, bg='black', fg='white')
        movie5name.grid(column=1, row=10, sticky=W)
        movie5comment = Label(movieList, text="Comment:    " + Commentline6, bg='black', fg='white')
        movie5comment.grid(column=2, row=10, sticky=W)
        movie5rate = Label(movieList, text="Star Rating:     "+ Rateline6, bg='black', fg='white')
        movie5rate.grid(column=3, row=10, sticky=W)
        
       # movie6id = Label(movieList, text="ID:       " + subMenu[6] [0], bg='black', fg='white')
      #  movie6id.grid(column=0, row=11, sticky=W)
        movie6name = Label(movieList, text="7) Title:     " + Titleline7, bg='black', fg='white')
        movie6name.grid(column=1, row=11, sticky=W)
        movie6comment = Label(movieList, text="Comment:    " + Commentline7, bg='black', fg='white')
        movie6comment.grid(column=2, row=11, sticky=W)
        movie6rate = Label(movieList, text="Star Rating:     "+ Rateline7, bg='black', fg='white')
        movie6rate.grid(column=3, row=11, sticky=W)
        
      #  movie7id = Label(movieList, text="ID:       " + subMenu[7] [0], bg='black', fg='white')
       # movie7id.grid(column=0, row=12, sticky=W)
        movie7name = Label(movieList, text="8) Title:     " + Titleline8, bg='black', fg='white')
        movie7name.grid(column=1, row=12, sticky=W)
        movie7comment = Label(movieList, text="Comment:    " + Commentline8, bg='black', fg='white')
        movie7comment.grid(column=2, row=12, sticky=W)
        movie7rate = Label(movieList, text="Star Rating:     "+ Rateline8, bg='black', fg='white')
        movie7rate.grid(column=3, row=12, sticky=W)
        
       # movie8id = Label(movieList, text="ID:       " + subMenu[8] [0], bg='black', fg='white')
      #  movie8id.grid(column=0, row=13, sticky=W)
        movie8name = Label(movieList, text="9) Title:     " + Titleline9, bg='black', fg='white')
        movie8name.grid(column=1, row=13, sticky=W)
        movie8comment = Label(movieList, text="Comment:    " + Commentline9, bg='black', fg='white')
        movie8comment.grid(column=2, row=13, sticky=W)
        movie8rate = Label(movieList, text="Star Rating:     "+ Rateline9, bg='black', fg='white')
        movie8rate.grid(column=3, row=13, sticky=W)
        
      #  movie9id = Label(movieList, text="ID:       " + subMenu[9] [0], bg='black', fg='white')
      #  movie9id.grid(column=0, row=14, sticky=W)
        movie9name = Label(movieList, text="10) Title:     " + Titleline10, bg='black', fg='white')
        movie9name.grid(column=1, row=14, sticky=W)
        movie9comment = Label(movieList, text="Comment:    " + Commentline10, bg='black', fg='white')
        movie9comment.grid(column=2, row=14, sticky=W)
        movie9rate = Label(movieList, text="Star Rating:     "+ Rateline10, bg='black', fg='white')
        movie9rate.grid(column=3, row=14, sticky=W)

        txtid = Entry(movieList,width=10)
        txtid.grid(column=1, row=0)
        
        def delete():
            name = int(txtid.get())
            line_to_replace = (name -1)
            comment_file = 'savedComment.txt'
            rating_file = 'savedratings.txt'
            movie_file = 'savedmovies.txt'
            
            #Movie Delete
            with open(movie_file, 'r') as file:
                lines = file.readlines()
                
            if len(lines) > int(line_to_replace):
                lines[line_to_replace] = ""
                with open(movie_file, 'w') as file:                            
                        file.writelines( lines )
            movies[line_to_replace] = ""
            
            #Rating Delete
            with open(rating_file, 'r') as file:
                lines = file.readlines()
                
            if len(lines) > int(line_to_replace):
                lines[line_to_replace] = "N/A \n"
                with open(rating_file, 'w') as file:                            
                        file.writelines( lines )
            ratings[line_to_replace] = "N/A \n"

            #Comment Delete
            with open(comment_file, 'r') as file:
                lines = file.readlines()
                
            if len(lines) > int(line_to_replace):
                lines[line_to_replace] = "N/A \n"
                with open(comment_file, 'w') as file:                            
                        file.writelines( lines )
            comments[line_to_replace] = "N/A \n"

        def idload():
            name = int(txtid.get())
              
            instructionComment = Label(movieList, text="Please add a comment", bg='black', fg='white')
            instructionComment.grid(column=1, row=1, sticky=W)
            
            txt = Entry(movieList,width=10)
            txt.grid(column=1, row=2)
            
            instructionrate = Label(movieList, text="Please rate the movie from 1 to 5", bg='black', fg='white')
            instructionrate.grid(column=1, row=3, sticky=W)
                            
            txt1 = Entry(movieList,width=10)
            txt1.grid(column=1, row=4)
            
        
            def clickedComment():
                line_to_replace = (name -1)
                my_file = 'savedComment.txt'

                with open(my_file, 'r') as file:
                    lines = file.readlines()
                    
                if len(lines) > int(line_to_replace):
                    lines[line_to_replace] = txt.get()+"\n"
                    with open(my_file, 'w') as file:                            
                            file.writelines( lines )
                comments[line_to_replace] = txt.get()+"\n"
                                                  
            def clickedRate():
                line_to_replace = (name -1)
                my_file = 'savedratings.txt'

                with open(my_file, 'r') as file:
                    lines = file.readlines()
                    
                if len(lines) > int(line_to_replace):
                    lines[line_to_replace] = txt1.get()+"\n"
                if txt1.get() == "1" or txt1.get() == "2" or txt1.get() == "3" or txt1.get() == "4" or txt1.get() == "5":
                    with open(my_file, 'w') as file:
                        file.writelines( lines )  
                else:
                    messagebox.showwarning("Warning","Pick a number from 1 to 5")
                ratings[line_to_replace] = txt1.get()+"\n"
    
            btn = Button(movieList, text="Add comment", command=clickedComment)
            btn.grid(column=2, row=2)
            btn = Button(movieList, text= "Add raiting",command=clickedRate)
            btn.grid(column=2, row=4)
            movieList.mainloop()
                
           
                
        btnid = Button(movieList, text="Movie ID", command=idload)
        btnid.grid(column=2, row=0)  
        
        btndel = Button(movieList, text="Delete Entry", command=delete)
        btndel.grid(column=3, row=0)  

        lbl_footer = Label(self, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor='s',bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)
        
        
app = App()
app.mainloop()
print(id(app), app.spam())

impostor=App()
impostor.mainloop()
#print(id(impostor), impostor.spam())