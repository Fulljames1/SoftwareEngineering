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


#create a label where we can insert the acme logo
#this could be lbl_logo=PhotoImage(file=f)
lbl_logo = Label(frame, text= "ACME", bg='black', fg = 'white')
lbl_logo.pack(pady=50)

#label for the welcome text
lbl_welcome = Label(frame, text="Welcome back!", bg='black', fg='white')
lbl_welcome.pack()

#label for the tiny text
lbl_txt = Label(frame, text="Please choose the database you want to search:", bg='black', fg='white')
lbl_txt.pack(pady=15)

#button for TMDb
btn_IMDb = Button(frame, text="IMDb", bg='white', fg='black', anchor=CENTER, command=doSomething)
btn_IMDb.pack(padx=10, pady=2)

#button for OMDb
btn_OMDb = Button(frame, text="IMDb", bg='white', fg='black', anchor=CENTER, command=doSomething)
btn_OMDb.pack( padx=10, pady=2)


#footer with the customersupport and contacts
lbl_footer = Label(frame, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor=CENTER)
lbl_footer.pack(side=BOTTOM, fill=X)

root.mainloop()