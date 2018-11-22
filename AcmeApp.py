from tkinter import *
import urllib.request
import json
import tkinter.messagebox

# constructor of the class App
class App(Tk):
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

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


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

        # img=PhotoImage(file="hb.png", width=30, height=30)
        home = Button(frame1, text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        # logo on the left-top corner
        lbl_logo = Label(frame1, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=10, side=LEFT)

        # "Add to wishlist" button on the right of the window
        addToWishBtn = Button(frame2, text="Add to wishlist", bg='gray', fg='white', command=lambda : controller.show_frame(WishPage),highlightcolor='orange')
        addToWishBtn.pack(side=RIGHT, pady=5, padx=5)

        # labels on the left
        name_lbl = Button(frame3, text="Name", bg='black', fg='white', command=lambda:showMovieInfo(controller.shared_data["title"]))
        name_lbl.pack(side=LEFT, padx=15, pady=5)
        #name_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["title"]))

        year_lbl = Button(frame4, text="Year", bg='black', fg='white',command=lambda:showMovieInfo(controller.shared_data["year"]))
        year_lbl.pack(side=LEFT, padx=15, pady=5)
        #year_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["year"]))

        director_lbl = Button(frame5, text="Director", bg='black', fg='white', command=lambda:showMovieInfo(controller.shared_data["dire"]))
        director_lbl.pack(side=LEFT, padx=15, pady=5)
        #director_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["dire"]))

        cast_lbl = Button(frame6, text="Cast", bg='black', fg='white',command=lambda:showMovieInfo(controller.shared_data["actors"]))
        cast_lbl.pack(side=LEFT, padx=15, pady=5)
        #cast_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["actors"]))

        description_lbl = Button(frame7, text="Description", bg='black', fg='white',command=lambda:showMovieInfo(controller.shared_data["plot"]))
        description_lbl.pack(side=LEFT, padx=15, pady=5)
        #description_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["plot"]))

        # labels for info on the right
       # print("Ready to display the global vars!")

        #nameInfo_lbl = Label(frame3, text=controller.shared_data["title"], bg='black', fg='white')
        #nameInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        #yearInfo_lbl = Label(frame4, text=controller.shared_data["year"], bg='black', fg='white')
        #yearInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        #directorInfo_lbl = Label(frame5, text=controller.shared_data["dire"], bg='black', fg='white')
        #directorInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        #castInfo_lbl = Label(frame6, text=controller.shared_data["actors"], bg='black', fg='white')
        #castInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        #descriptionInfo_lbl = Label(frame7, text=controller.shared_data["plot"], bg='black', fg='white')
        #descriptionInfo_lbl.pack(side=LEFT, padx=15, pady=5)

        #lbl_footer = Label(frame7, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, bg='black', fg='white', bd=0)
        #lbl_footer.pack(side=BOTTOM, fill=X, anchor='center')


class WishPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        l = PanedWindow(self, bg='black')
        l.pack(fill=X)

        # img=PhotoImage(file="hb.png", width=30, height=30)
        home = Button(l, text='Home', command=lambda: controller.show_frame(StartPage), font=("Arial", "8", "italic"), width=5, height=2, bg='black', fg='orange', highlightcolor='orange')
        home.pack(side=RIGHT, anchor='ne')

        lbl_logo = Label(l, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(pady=10, side=LEFT)

        header = PanedWindow(self, orient=HORIZONTAL, bg='black')
        header.pack(fill=X)

        name_lbl = Label(header, text='Name', bg='black', fg='white', height=10, width=25)
        name_lbl.pack(side=LEFT)

        com_lbl = Label(header, text='Comment', bg='black', fg='white', height=10, width=25)
        com_lbl.pack(side=LEFT)

        rate_lbl = Label(header, text='Rating', bg='black', fg='white', height=10, width=25)
        rate_lbl.pack(side=LEFT)

        movieList = PanedWindow(self, orient=HORIZONTAL, bg='black')
        movieList.pack(fill='both', expand=True)

        nameInfo = Text(movieList, bg='black', fg='white', height=25, width=25)
        nameInfo.insert(INSERT, 'Movie name example')
        nameInfo.pack(side=LEFT)

        comInfo = Text(movieList, bg='black', fg='white', height=25, width=25)
        comInfo.insert(INSERT, 'Comment example. It should be very very very very very very very very very very very very very very very very loooooooooooooooooong. Cause that\'s how comments usually are. ')
        comInfo.pack(side=LEFT)

        rating = Text(movieList, bg='black', fg='white', height=25, width=25)
        rating.insert(INSERT, 'This section will have the n/5 ')
        rating.pack(side=LEFT)

        scroll = Scrollbar(movieList)
        scroll.pack(side=RIGHT, fill=Y)

        lbl_footer = Label(self, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor='s',bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)


app = App()
app.mainloop()