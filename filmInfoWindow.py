from tkinter import *


def doSomething():
    print("I am doing something!")

# empty window
root = Tk()
root.geometry('600x400')

# 7 frames for the layout
frame1 = Frame(root, bg='black')
frame1.pack(fill=BOTH, expand=TRUE, side=TOP)
frame2 = Frame(root, bg='black')
frame2.pack(fill=BOTH, expand=TRUE)
frame3 = Frame(root, bg='black')
frame3.pack(fill=BOTH, expand=TRUE)
frame4 = Frame(root, bg='black')
frame4.pack(fill=BOTH, expand=TRUE)
frame5 = Frame(root, bg='black')
frame5.pack(fill=BOTH, expand=TRUE)
frame6 = Frame(root, bg='black')
frame6.pack(fill=BOTH, expand=TRUE)
frame7 = Frame(root, bg='black')
frame7.pack(fill=BOTH, expand=TRUE)

# logo on the left-top corner
lbl_logo = Label(frame1, text= "ACME", bg='black', fg = 'white')
lbl_logo.pack(pady=10, side=LEFT)

# "Add to wishlist" button on the right of the window
addToWishBtn=Button(frame2, text="Add to wishlist", bg='gray', fg='white', command=doSomething)
addToWishBtn.pack(side=RIGHT, pady=5, padx=5)

# labels on the left
name_lbl=Label(frame3, text="Name", bg='black', fg='white')
name_lbl.pack(side=LEFT, padx=15, pady=5)

year_lbl=Label(frame4, text="Year", bg='black', fg='white')
year_lbl.pack(side=LEFT, padx=15, pady=5)

director_lbl=Label(frame5, text="Director", bg='black', fg='white')
director_lbl.pack(side=LEFT, padx=15, pady=5)

cast_lbl=Label(frame6, text="Cast", bg='black', fg='white')
cast_lbl.pack(side=LEFT, padx=15, pady=5)

description_lbl=Label(frame7, text="Description", bg='black', fg='white')
description_lbl.pack(side=LEFT, padx=15, pady=5)

# labels for info on the right
nameInfo_lbl=Label(frame3, text="Name_of_the_movie", bg='black', fg='white')
nameInfo_lbl.pack(side=LEFT, padx=15, pady=5)

yearInfo_lbl=Label(frame4, text="Year_of_the_movie", bg='black', fg='white')
yearInfo_lbl.pack(side=LEFT, padx=15, pady=5)

directorInfo_lbl=Label(frame5, text="Director_of_the_movie", bg='black', fg='white')
directorInfo_lbl.pack(side=LEFT, padx=15, pady=5)

castInfo_lbl=Label(frame6, text="Cast_of_the_movie", bg='black', fg='white')
castInfo_lbl.pack(side=LEFT, padx=15, pady=5)

descriptionInfo_lbl=Label(frame7, text="Descriprtion_of_the_movie", bg='black', fg='white')
descriptionInfo_lbl.pack(side=LEFT, padx=15, pady=5)

root.mainloop()