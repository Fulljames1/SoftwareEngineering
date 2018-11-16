from tkinter import *


def doSomething():
    print("I am doing something!")

#empty window
root = Tk()
#root.geometry('600x400')

#a frame that will stretch over the whole window
frame = Frame(root, height=400,width=600, bg='black')
frame.grid_propagate(0)
frame.pack(fill=BOTH, expand=TRUE)

#layout frames
#frameT=Frame(frame)
#frameT.pack(side=TOP)
#frameB=Frame(frame)
#frameB.pack(side=BOTTOM)
#frameR=Frame(frame)
#frameR.pack(side=RIGHT)
#frameL=Frame(frame)
#frameL.pack(side=LEFT)

#logo
lbl_logo = Label(frame, text= "ACME", bg='black', fg = 'white')
lbl_logo.pack(pady=50)

#input box
searchBox=Entry(frame)
searchBox.pack(pady=10, padx=10)

#search button in line with the input box
searchBtn=Button(frame, text="Search", bg='white', fg='black', command=doSomething)
searchBtn.pack()

#RANDOM button underneath input box
randomBtn=Button(frame, text="Random", bg='white', fg='black', command=doSomething)
randomBtn.pack()

#WISHLIST in line with Random button
wishBtn=Button(frame, text="Wishlist", bg='white', fg='black', command=doSomething)
wishBtn.pack()

#footer
lbl_footer = Label(frame, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor=CENTER)
lbl_footer.pack(side=BOTTOM, fill=X)

root.mainloop()