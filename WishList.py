from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('850x500')



name = 0
m1 = ["1", "Avatar", "Weekend movie", "5/5"]
m2 = ["2","Star Wars", "Trash", "1/5"]
m3 = ["3","The Imitation Game", "History movie", "5/5"]
m4 = ["4","The Polar Express", "Nice Christmas movie", "2/5"]
m5 = ["5","Star Wars", "Need to start watching this", "3/5"]
m6 = ["6","Interstellar", "Does this count as revision?", "5/5"]
m7 = ["7","The Predator", "Scary dont watch alone!", "2/5"]
m8 = ["8","The Lion King", "Sing along", "3/5"]
m9 = ["9","Mission: Impossible - Rogue Nation", "ACTION!", "1/5"]
m10 = ["10","Pirates of the Caribbean: The Curse of the Black Pearl", "ARRRRR!!", "5/5"]


subMenu = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

#from pprint import pprint
#pprint(subMenu)
#print (subMenu[1][2])
movieid = Label(window, text="ID:       " + subMenu[0] [0])
movieid.grid(column=0, row=4, sticky=W)
moviename = Label(window, text="Movie Name:       " + subMenu[0] [1])
moviename.grid(column=1, row=4, sticky=W)
moviecomment = Label(window, text="Comment:       " + subMenu[0] [2])
moviecomment.grid(column=2, row=4, sticky=W)
movierate = Label(window, text="Raiting:   "+subMenu[0] [3])
movierate.grid(column=3, row=4, sticky=W)

movie1id = Label(window, text="ID:       " + subMenu[1] [0])
movie1id.grid(column=0, row=5, sticky=W)
movie1name = Label(window, text="Movie Name:       " + subMenu[1] [1])
movie1name.grid(column=1, row=5, sticky=W)
movie1comment = Label(window, text="Comment:       " + subMenu[1] [2])
movie1comment.grid(column=2, row=5, sticky=W)
movie1rate = Label(window, text="Raiting:   "+subMenu[1] [3])
movie1rate.grid(column=3, row=5, sticky=W)

movie2id = Label(window, text="ID:       " + subMenu[2] [0])
movie2id.grid(column=0, row=6, sticky=W)
movie2name = Label(window, text="Movie Name:       " + subMenu[2] [1])
movie2name.grid(column=1, row=6, sticky=W)
movie2comment = Label(window, text="Comment:       " + subMenu[2] [2])
movie2comment.grid(column=2, row=6, sticky=W)
movie2rate = Label(window, text="Raiting:   "+subMenu[2] [3])
movie2rate.grid(column=3, row=6, sticky=W)

movie3id = Label(window, text="ID:       " + subMenu[3] [0])
movie3id.grid(column=0, row=7, sticky=W)
movie3name = Label(window, text="Movie Name:       " + subMenu[3] [1])
movie3name.grid(column=1, row=7, sticky=W)
movie3comment = Label(window, text="Comment:       " + subMenu[3] [2])
movie3comment.grid(column=2, row=7, sticky=W)
movie3rate = Label(window, text="Raiting:   "+subMenu[3] [3])
movie3rate.grid(column=3, row=7, sticky=W)

movie4id = Label(window, text="ID:       " + subMenu[4] [0])
movie4id.grid(column=0, row=8, sticky=W)
movie4name = Label(window, text="Movie Name:       " + subMenu[4] [1])
movie4name.grid(column=1, row=8, sticky=W)
movie4comment = Label(window, text="Comment:       " + subMenu[4] [2])
movie4comment.grid(column=2, row=8, sticky=W)
movie4rate = Label(window, text="Raiting:   "+subMenu[4] [3])
movie4rate.grid(column=3, row=8, sticky=W)

movie5id = Label(window, text="ID:       " + subMenu[5] [0])
movie5id.grid(column=0, row=9, sticky=W)
movie5name = Label(window, text="Movie Name:       " + subMenu[5] [1])
movie5name.grid(column=1, row=9, sticky=W)
movie5comment = Label(window, text="Comment:       " + subMenu[5] [2])
movie5comment.grid(column=2, row=9, sticky=W)
movie5rate = Label(window, text="Raiting:   "+subMenu[5] [3])
movie5rate.grid(column=3, row=9, sticky=W)

movie6id = Label(window, text="ID:       " + subMenu[6] [0])
movie6id.grid(column=0, row=10, sticky=W)
movie6name = Label(window, text="Movie Name:       " + subMenu[6] [1])
movie6name.grid(column=1, row=10, sticky=W)
movie6comment = Label(window, text="Comment:       " + subMenu[6] [2])
movie6comment.grid(column=2, row=10, sticky=W)
movie6rate = Label(window, text="Raiting:   "+subMenu[6] [3])
movie6rate.grid(column=3, row=10, sticky=W)

movie7id = Label(window, text="ID:       " + subMenu[7] [0])
movie7id.grid(column=0, row=11, sticky=W)
movie7name = Label(window, text="Movie Name:       " + subMenu[7] [1])
movie7name.grid(column=1, row=11, sticky=W)
movie7comment = Label(window, text="Comment:       " + subMenu[7] [2])
movie7comment.grid(column=2, row=11, sticky=W)
movie7rate = Label(window, text="Raiting:   "+subMenu[7] [3])
movie7rate.grid(column=3, row=11, sticky=W)

movie8id = Label(window, text="ID:       " + subMenu[8] [0])
movie8id.grid(column=0, row=12, sticky=W)
movie8name = Label(window, text="Movie Name:       " + subMenu[8] [1])
movie8name.grid(column=1, row=12, sticky=W)
movie8comment = Label(window, text="Comment:       " + subMenu[8] [2])
movie8comment.grid(column=2, row=12, sticky=W)
movie8rate = Label(window, text="Raiting:   "+subMenu[8] [3])
movie8rate.grid(column=3, row=12, sticky=W)

movie9id = Label(window, text="ID:       " + subMenu[9] [0])
movie9id.grid(column=0, row=13, sticky=W)
movie9name = Label(window, text="Movie Name:       " + subMenu[9] [1])
movie9name.grid(column=1, row=13, sticky=W)
movie9comment = Label(window, text="Comment:       " + subMenu[9] [2])
movie9comment.grid(column=2, row=13, sticky=W)
movie9rate = Label(window, text="Raiting:   "+subMenu[9] [3])
movie9rate.grid(column=3, row=13, sticky=W)
  

txtid = Entry(window,width=10)
txtid.grid(column=1, row=0)



def idload():
    name = int(txtid.get())
    
   


#name = 1

    if name == 1:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            moviecomment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==2:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie1comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==3:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie2comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==4:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie3comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==5:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie4comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==6:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie5comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==7:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie6comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==8:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie7comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==9:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie8comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    elif name ==10:
        txt = Entry(window,width=10)
        txt.grid(column=1, row=2)
    
        def clicked():
            res =  "Comment:       " + txt.get()
            movie9comment.configure(text= res)

        btn = Button(window, text="Add comment", command=clicked)
        btn.grid(column=2, row=2)
        window.mainloop()
        
    else: 
        print("Please enter a movie ID between 1-10")
        
btnid = Button(window, text="Movie ID", command=idload)
btnid.grid(column=2, row=0)    

window.mainloop()