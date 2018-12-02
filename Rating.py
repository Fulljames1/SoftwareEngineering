from tkinter import *
import urllib.request
import json
import tkinter.messagebox


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


# creating a class for the StartPage window
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # set the value of the global StringVar "dbOption" to "1" for OMDb
        def dbPickOMDb(event):
            print("dbOption = 1")
            controller.shared_data["dbOption"]="1"

        # set the value of the global StringVar "dbOption" to "2" for IMDb
        def dbPickIMDb(event):
            print("dbOption = 2")
            controller.shared_data["dbOption"]="2"

        # a frame that will stretch over the whole window
        frame = Frame(self, height=400, width=600, bg='black')
        frame.grid_propagate(0)
        frame.pack(fill=BOTH, expand=TRUE)

        # a wishlist button in the top right corner of the window for ease of navigation
        wishlist = Button(frame, text='Wishlist', height=1, width=2, command=lambda: controller.show_frame(WishPage),bg='black', fg='orange', font=("Arial", "8", "italic"), highlightcolor='orange')
        wishlist.pack(side=TOP, ipadx=20, anchor='e')

        # create a label where we can insert the acme logo
        # this could be lbl_logo=PhotoImage(file=f)
        lbl_logo = Label(frame, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=50)

        # label for the welcome text
        lbl_welcome = Label(frame, text="Welcome back!", bg='black', fg='white')
        lbl_welcome.pack()

        # label for the tiny text
        lbl_txt = Label(frame, text="Please choose the database you want to search:", bg='black', fg='white')
        lbl_txt.pack(pady=15)

        # button for TMDb
        btn_IMDb = Button(frame, text="IMDb", bg='white', fg='black', anchor=CENTER, command=lambda: controller.show_frame(SearchPage),highlightcolor='orange')
        btn_IMDb.pack(padx=10, pady=2)
        btn_IMDb.bind("<Button-1>", dbPickIMDb)

        # button for OMDb
        btn_OMDb = Button(frame, text="OMDb", bg='white', fg='black', anchor=CENTER, command=lambda: controller.show_frame(SearchPage),highlightcolor='orange')
        btn_OMDb.pack(padx=10, pady=2)
        btn_OMDb.bind("<Button-1>", dbPickOMDb)

        # footer with the customersupport and contacts
        lbl_footer = Label(frame, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor='s',
                           bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)


# create class for the SearchPage
class SearchPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # defining the search function behind the search button
        def searchMovie(event):
            moviename=searchBox.get()
            title=moviename.replace(' ','-')

            if controller.shared_data["dbOption"]=="1":
                url='https://www.omdbapi.com/?t=' + title + '&apikey=244bde45'
                print('Db: 1\t'+url)
                # using the urllib.request library we can access urls from within our app, without the need of a browser
                json_obj = urllib.request.urlopen(url)
                data = json.load(json_obj)

                controller.shared_data["title"] = data['Title']
                controller.shared_data["year"] = data['Year']
                controller.shared_data["dire"] = data['Director']
                controller.shared_data["actors"] = data['Actors']
                controller.shared_data["plot"] = data['Plot']
                print("The details of the movie is stored")

            elif controller.shared_data["dbOption"]=="2":
                url='https://api.themoviedb.org/3/search/movie?api_key=da097a759910eefff9e3098e9e3d3870&query=' + title
                print('Db: 2\t'+url)

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
                    print("The details of the first movie are stored!")
                    break
            else:
                print("ERROR!There is no movie with such a name! Please try again!")


            print("Reached the end of the SEARCH function!\n")

        # a frame to cover and host all other widgets and structuring elements in the window
        frame = Frame(self, height=400, width=600, bg='black')
        frame.grid_propagate(0)
        frame.pack(fill=BOTH, expand=TRUE)

        # a home button in the top right side of the window for ease of access, could also be an image button with a bit of struggle
        # img=PhotoImage(file="hb.png", width=30, height=30)
        home=Button(frame, text='Home', command=lambda : controller.show_frame(StartPage),font=("Arial","8","italic"), width=5, height=2,bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        # logo
        lbl_logo = Label(frame, text="ACME",font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(side=TOP, anchor='center', pady=60)

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

        # footer
        lbl_footer = Label(frame, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN,anchor='s', bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)


# a class for the page where we output the movie info from the database
class InfoPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def showMovieInfo(param):
            tkinter.messagebox.showinfo('Movie Info', param)

        def saveMovie(param):
            name = open("savedmovies.txt", "a")
            name.write(param+"\n") #writes contents in file to usernames.txt
            #name.close() #closes file
            print("Saved\n")

        def upWishList(self): # this function reads the text in the savedmovie.txt and saves it in the global variable test
            txt = open("savedmovies.txt", "r")
            lines = txt.readlines() # this creates a list containing every line in the text file

            for l in lines: # looping through the movie names list
                movies.append(l) # and appending them to the global list "movies"

            txt.close()
            print(movies)

        def updateInfo():
            nameInfo_lbl.configure(text=controller.shared_data["title"])
            yearInfo_lbl.configure(text=controller.shared_data["year"])
            directorInfo_lbl.configure(text=controller.shared_data["dire"])
            castInfo_lbl.configure(text=controller.shared_data["actors"])
            descriptionInfo_lbl.configure(text=controller.shared_data["plot"])
            print("Info page updated!")

        # 7 frames for the layout
        frame1 = Frame(self, bg='black')
        frame1.pack(fill=BOTH, expand=TRUE, side=TOP)
        frame2 = Frame(self, bg='black')
        frame2.pack(fill=BOTH, expand=TRUE)
        frame3 = Frame(self, bg='black')
        frame3.pack(fill=BOTH, expand=TRUE)
        frame4 = Frame(self, bg='black')
        frame4.pack(fill=BOTH, expand=TRUE)
        frame5 = Frame(self, bg='black')
        frame5.pack(fill=BOTH, expand=TRUE)
        frame6 = Frame(self, bg='black')
        frame6.pack(fill=BOTH, expand=TRUE)
        frame7 = Frame(self, bg='black')
        frame7.pack(fill=BOTH, expand=TRUE)

        # wishlist button top right corner, ease of access
        wishlist = Button(frame1, text='Wishlist', height=2, width=6, command=lambda: controller.show_frame(WishPage), font=("Arial", "8", "italic"), bg='black', fg='orange', highlightcolor='orange')
        wishlist.pack(side=RIGHT, anchor='ne')
        wishlist.bind("<Button-1>", upWishList)

        # img=PhotoImage(file="hb.png", width=30, height=30)
        home = Button(frame1, text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        # logo on the left-top corner
        lbl_logo = Label(frame1, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=10, side=LEFT)

        # a button to force-update the info labels
        refresh = Button(frame2, text="Refresh Page", bg='black', fg='orange', command=updateInfo)
        refresh.pack(side=RIGHT)

        # "Add to wishlist" button on the right of the window
        addToWishBtn = Button(frame2, text="Add to wishlist", bg='gray', fg='white', command=lambda:saveMovie(controller.shared_data["title"]))
        addToWishBtn.pack(side=RIGHT, pady=5, padx=5)

        
        
        

        # labels on the left
        name_lbl = Label(frame3, text="Name", bg='black', fg='white')#, command=lambda:showMovieInfo(controller.shared_data["title"]))
        name_lbl.pack(side=LEFT, padx=15, pady=5)
        #name_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["title"]))

        year_lbl = Label(frame4, text="Year", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["year"]))
        year_lbl.pack(side=LEFT, padx=15, pady=5)
        #year_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["year"]))

        director_lbl = Label(frame5, text="Director", bg='black', fg='white')#, command=lambda:showMovieInfo(controller.shared_data["dire"]))
        director_lbl.pack(side=LEFT, padx=15, pady=5)
        #director_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["dire"]))

        cast_lbl = Label(frame6, text="Cast", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["actors"]))
        cast_lbl.pack(side=LEFT, padx=15, pady=5)
        #cast_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["actors"]))

        description_lbl = Label(frame7, text="Description", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["plot"]))
        description_lbl.pack(side=LEFT, padx=15, pady=5)
        #description_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["plot"]))

        # labels for info on the right

        nameInfo_lbl = Label(frame3, text="info", bg='black', fg='white')
        nameInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        yearInfo_lbl = Label(frame4, text="info", bg='black', fg='white')
        yearInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        directorInfo_lbl = Label(frame5, text="info", bg='black', fg='white')
        directorInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        castInfo_lbl = Label(frame6, text="info", bg='black', fg='white')
        castInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        descriptionInfo_lbl = Label(frame7, text="info", bg='black', fg='white')
        descriptionInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        lbl_footer = Label(frame7, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X, anchor='center')


class WishPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        l = PanedWindow(self, bg='black')
        l.pack(fill=X)

# we need to find a way to update the values in these fields

        m1 = ["1", "title", "Add Comment", "Add rating"]
        m2 = ["2","title", "Add Comment", "Add rating"]
        m3 = ["3","title", "Add Comment", "Add rating"]
        m4 = ["4","title", "Add Comment", "Add rating"]
        m5 = ["5","title", "Add Comment", "Add rating"]
        m6 = ["6","title", "Add Comment", "Add rating"]
        m7 = ["7","title", "Add Comment", "Add rating"]
        m8 = ["8","title", "Add Comment", "Add rating"]
        m9 = ["9","title", "Add Comment", "Add rating"]
        m10 = ["10","title", "Add Comment", "Add rating"]
        
        subMenu = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

        home = Button(l, text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        lbl_logo = Label(l, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=10, side=LEFT)

        header = PanedWindow(self, orient=HORIZONTAL, bg='black')
        header.pack(fill=X)

        def updateWishy():
            moviename.configure(text=movies[0])
            movie1name.configure(text=movies[1])
            movie2name.configure(text=movies[2])
            movie3name.configure(text=movies[3])
            movie4name.configure(text=movies[4])
            movie5name.configure(text=movies[5])
            movie6name.configure(text=movies[6])
            movie7name.configure(text=movies[7])
            movie8name.configure(text=movies[8])
            movie9name.configure(text=movies[9])

        refresh=Button(header,text="Refresh Page", bg='black', fg='orange', command= updateWishy)
        refresh.pack(side=RIGHT)

      

        movieList = PanedWindow(self, orient=HORIZONTAL, bg='black')
        movieList.pack(fill='both', expand=True)
        
        movieid = Label(movieList, text="ID:       " + subMenu[0] [0], bg='black', fg='white')
        movieid.grid(column=0, row=4, sticky=W)
        moviename = Label(movieList, text="Movie Name:       " + subMenu[0] [1], bg='black', fg='white')
        moviename.grid(column=1, row=4, sticky=W)
        moviecomment = Label(movieList, text="Comment:       " + subMenu[0] [2], bg='black', fg='white')
        moviecomment.grid(column=2, row=4, sticky=W)
        movierate = Label(movieList, text="Raiting:   "+subMenu[0] [3], bg='black', fg='white')
        movierate.grid(column=3, row=4, sticky=W)
        
        movie1id = Label(movieList, text="ID:       " + subMenu[1] [0], bg='black', fg='white')
        movie1id.grid(column=0, row=5, sticky=W)
        movie1name = Label(movieList, text="Movie Name:       " + subMenu[1] [1], bg='black', fg='white')
        movie1name.grid(column=1, row=5, sticky=W)
        movie1comment = Label(movieList, text="Comment:       " + subMenu[1] [2], bg='black', fg='white')
        movie1comment.grid(column=2, row=5, sticky=W)
        movie1rate = Label(movieList, text="Raiting:   "+subMenu[1] [3], bg='black', fg='white')
        movie1rate.grid(column=3, row=5, sticky=W)
        
        movie2id = Label(movieList, text="ID:       " + subMenu[2] [0], bg='black', fg='white')
        movie2id.grid(column=0, row=6, sticky=W)
        movie2name = Label(movieList, text="Movie Name:       " + subMenu[2] [1], bg='black', fg='white')
        movie2name.grid(column=1, row=6, sticky=W)
        movie2comment = Label(movieList, text="Comment:       " + subMenu[2] [2], bg='black', fg='white')
        movie2comment.grid(column=2, row=6, sticky=W)
        movie2rate = Label(movieList, text="Raiting:   "+subMenu[2] [3], bg='black', fg='white')
        movie2rate.grid(column=3, row=6, sticky=W)
        
        movie3id = Label(movieList, text="ID:       " + subMenu[3] [0], bg='black', fg='white')
        movie3id.grid(column=0, row=7, sticky=W)
        movie3name = Label(movieList, text="Movie Name:       " + subMenu[3] [1], bg='black', fg='white')
        movie3name.grid(column=1, row=7, sticky=W)
        movie3comment = Label(movieList, text="Comment:       " + subMenu[3] [2], bg='black', fg='white')
        movie3comment.grid(column=2, row=7, sticky=W)
        movie3rate = Label(movieList, text="Raiting:   "+subMenu[3] [3], bg='black', fg='white')
        movie3rate.grid(column=3, row=7, sticky=W)
        
        movie4id = Label(movieList, text="ID:       " + subMenu[4] [0], bg='black', fg='white')
        movie4id.grid(column=0, row=8, sticky=W)
        movie4name = Label(movieList, text="Movie Name:       " + subMenu[4] [1], bg='black', fg='white')
        movie4name.grid(column=1, row=8, sticky=W)
        movie4comment = Label(movieList, text="Comment:       " + subMenu[4] [2], bg='black', fg='white')
        movie4comment.grid(column=2, row=8, sticky=W)
        movie4rate = Label(movieList, text="Raiting:   "+subMenu[4] [3], bg='black', fg='white')
        movie4rate.grid(column=3, row=8, sticky=W)
        
        movie5id = Label(movieList, text="ID:       " + subMenu[5] [0], bg='black', fg='white')
        movie5id.grid(column=0, row=9, sticky=W)
        movie5name = Label(movieList, text="Movie Name:       " + subMenu[5] [1], bg='black', fg='white')
        movie5name.grid(column=1, row=9, sticky=W)
        movie5comment = Label(movieList, text="Comment:       " + subMenu[5] [2], bg='black', fg='white')
        movie5comment.grid(column=2, row=9, sticky=W)
        movie5rate = Label(movieList, text="Raiting:   "+subMenu[5] [3], bg='black', fg='white')
        movie5rate.grid(column=3, row=9, sticky=W)
        
        movie6id = Label(movieList, text="ID:       " + subMenu[6] [0], bg='black', fg='white')
        movie6id.grid(column=0, row=10, sticky=W)
        movie6name = Label(movieList, text="Movie Name:       " + subMenu[6] [1], bg='black', fg='white')
        movie6name.grid(column=1, row=10, sticky=W)
        movie6comment = Label(movieList, text="Comment:       " + subMenu[6] [2], bg='black', fg='white')
        movie6comment.grid(column=2, row=10, sticky=W)
        movie6rate = Label(movieList, text="Raiting:   "+subMenu[6] [3], bg='black', fg='white')
        movie6rate.grid(column=3, row=10, sticky=W)
        
        movie7id = Label(movieList, text="ID:       " + subMenu[7] [0], bg='black', fg='white')
        movie7id.grid(column=0, row=11, sticky=W)
        movie7name = Label(movieList, text="Movie Name:       " + subMenu[7] [1], bg='black', fg='white')
        movie7name.grid(column=1, row=11, sticky=W)
        movie7comment = Label(movieList, text="Comment:       " + subMenu[7] [2], bg='black', fg='white')
        movie7comment.grid(column=2, row=11, sticky=W)
        movie7rate = Label(movieList, text="Raiting:   "+subMenu[7] [3], bg='black', fg='white')
        movie7rate.grid(column=3, row=11, sticky=W)
        
        movie8id = Label(movieList, text="ID:       " + subMenu[8] [0], bg='black', fg='white')
        movie8id.grid(column=0, row=12, sticky=W)
        movie8name = Label(movieList, text="Movie Name:       " + subMenu[8] [1], bg='black', fg='white')
        movie8name.grid(column=1, row=12, sticky=W)
        movie8comment = Label(movieList, text="Comment:       " + subMenu[8] [2], bg='black', fg='white')
        movie8comment.grid(column=2, row=12, sticky=W)
        movie8rate = Label(movieList, text="Raiting:   "+subMenu[8] [3], bg='black', fg='white')
        movie8rate.grid(column=3, row=12, sticky=W)
        
        movie9id = Label(movieList, text="ID:       " + subMenu[9] [0], bg='black', fg='white')
        movie9id.grid(column=0, row=13, sticky=W)
        movie9name = Label(movieList, text="Movie Name:       " + subMenu[9] [1], bg='black', fg='white')
        movie9name.grid(column=1, row=13, sticky=W)
        movie9comment = Label(movieList, text="Comment:       " + subMenu[9] [2], bg='black', fg='white')
        movie9comment.grid(column=2, row=13, sticky=W)
        movie9rate = Label(movieList, text="Raiting:   "+subMenu[9] [3], bg='black', fg='white')
        movie9rate.grid(column=3, row=13, sticky=W)

        txtid = Entry(movieList,width=10)
        txtid.grid(column=1, row=0)



        def idload():
            name = int(txtid.get())
        
            if name == 1:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
                
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    moviecomment.configure(text= res)
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movierate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==2:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie1comment.configure(text= res)
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie1rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
                
            elif name ==3:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie2comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie2rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
               
                movieList.mainloop()
                
            elif name ==4:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie3comment.configure(text= res)
                    
                
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie3rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                
                movieList.mainloop()
                
            elif name ==5:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie4comment.configure(text= res)
                    
                
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie4rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==6:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie5comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie5rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==7:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie6comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie6rate.configure(text= res1)
                    
                    
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==8:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie7comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie7rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==9:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie8comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie8rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            elif name ==10:
                txt = Entry(movieList,width=10)
                txt.grid(column=1, row=2)
                txt1 = Entry(movieList,width=10)
                txt1.grid(column=1, row=3)
            
                def clicked():
                    res =  "Comment:       " + txt.get()
                    movie9comment.configure(text= res)
                    
                    
                def clickedRate():
                    res1 = "Raiting:   " + txt1.get()+ "/5"
                    movie9rate.configure(text= res1)
        
                btn = Button(movieList, text="Add comment", command=clicked)
                btn.grid(column=2, row=2)
                btn = Button(movieList, text= "Add raiting",command=clickedRate)
                btn.grid(column=2, row=3)
                movieList.mainloop()
                
            else: 
                print("Please enter a movie ID between 1-10")
                
        btnid = Button(movieList, text="Movie ID", command=idload)
        btnid.grid(column=2, row=0)  


        lbl_footer = Label(self, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor='s',bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)
        
        
app = App()
app.mainloop()
print(id(app), app.spam())

impostor=App()
impostor.mainloop()
#print(id(impostor), impostor.spam())