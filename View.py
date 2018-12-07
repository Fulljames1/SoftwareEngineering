# -*- coding: utf-8 -*-
from tkinter import *
import urllib.request
import json
import tkinter.messagebox
#from .Model import updateInfomation

def startPageDbView(option):
    if option ==1:
        print("dbOption = 1")
    elif option ==2:
        print("dbOption = 2")
        
def startFrame(Container, instance):
    # a frame that will stretch over the whole window
    container = Container(instance, height=400, width=600, bg='black')
    container.grid_propagate(0)
    container.pack(fill=BOTH, expand=TRUE)
    return container

def startPageLayout(container):
    # create a label where we can insert the acme logo
    # this could be lbl_logo=PhotoImage(file=f)
    lbl_logo = Label(container, text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
    lbl_logo.pack(pady=50)

    # label for the welcome text
    lbl_welcome = Label(container, text="Welcome back!", bg='black', fg='white')
    lbl_welcome.pack()

    # label for the tiny text
    lbl_txt = Label(container, text="Please choose the database you want to search:", bg='black', fg='white')
    lbl_txt.pack(pady=15)

    # footer with the customersupport and contacts
    lbl_footer = Label(container, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, anchor='s', bg='black', fg='white', bd=0)
    lbl_footer.pack(side=BOTTOM, fill=X)
    
def searchDbURL(address, option, saved):
    if option ==1:
        print('Db: 1\t'+address)
        if saved ==1:
            print("The details of the movie is stored")
    elif option ==2:
        print('Db: 2\t'+address)
        if saved ==1:
            print("The details of the movie is stored")
    elif option ==3:        
        print("Reached the end of the SEARCH function!\n")    
    elif option ==4:
        print("ERROR!There is no movie with such a name! Please try again!")
        
def searchFrame(Container, instance):
    # a frame to cover and host all other widgets and structuring elements in the window
        container = Container(instance, height=400, width=600, bg='black')
        container.grid_propagate(0)
        container.pack(fill=BOTH, expand=TRUE)
        return container
    
def searchPageLayout(container):
    # logo
        lbl_logo = Label(container, text="ACME",font=("Arial Black", "30", "bold"), bg='black', fg='orange')
        lbl_logo.pack(side=TOP, anchor='center', pady=60)
               
        # footer
        lbl_footer = Label(container, text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN,anchor='s', bg='black', fg='white', bd=0)
        lbl_footer.pack(side=BOTTOM, fill=X)
    
        
def InfoMoviePrint(films, option):
        if option ==1:
            print(films)
        elif option ==2:
            print("Info page updated!")
            
def infoFrame(Container, instance):
    containerlist = []
    # 7 frames for the layout
    frame1 = Container(instance, bg='black')
    frame1.pack(fill=BOTH, expand=TRUE, side=TOP)
    containerlist.append(frame1)
    frame2 = Container(instance, bg='black')
    frame2.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame2)
    frame3 = Container(instance, bg='black')
    frame3.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame3)
    frame4 = Container(instance, bg='black')
    frame4.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame4)
    frame5 = Container(instance, bg='black')
    frame5.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame5)
    frame6 = Container(instance, bg='black')
    frame6.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame6)
    frame7 = Container(instance, bg='black')
    frame7.pack(fill=BOTH, expand=TRUE)
    containerlist.append(frame7)
    return containerlist

def infoPageLayout(containerlist):
    # logo on the left-top corner
    lbl_logo = Label(containerlist[0], text="ACME", font=("Arial Black", "30", "bold"), bg='black', fg='orange')
    lbl_logo.pack(pady=10, side=LEFT)

    # labels on the left
    name_lbl = Label(containerlist[2], text="Name", bg='black', fg='white')#, command=lambda:showMovieInfo(controller.shared_data["title"]))
    name_lbl.pack(side=LEFT, padx=15, pady=5)
    #name_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["title"]))

    year_lbl = Label(containerlist[3], text="Year", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["year"]))
    year_lbl.pack(side=LEFT, padx=15, pady=5)
    #year_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["year"]))

    director_lbl = Label(containerlist[4], text="Director", bg='black', fg='white')#, command=lambda:showMovieInfo(controller.shared_data["dire"]))
    director_lbl.pack(side=LEFT, padx=15, pady=5)
    #director_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["dire"]))

    cast_lbl = Label(containerlist[5], text="Cast", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["actors"]))
    cast_lbl.pack(side=LEFT, padx=15, pady=5)
    #cast_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["actors"]))

    description_lbl = Label(containerlist[6], text="Description", bg='black', fg='white')#,command=lambda:showMovieInfo(controller.shared_data["plot"]))
    description_lbl.pack(side=LEFT, padx=15, pady=5)
    #description_lbl.bind("<Button-1>",showMovieInfo(controller.shared_data["plot"]))

    lbl_footer = Label(containerlist[6], text="customersupport@acme.com         Tel:01632 960625", relief=SUNKEN, bg='black', fg='white', bd=0)
    lbl_footer.pack(side=BOTTOM, fill=X, anchor='center')
    
def printInfoMovies(films):
    print(films)