# -*- coding: utf-8 -*-
from tkinter import *
import urllib.request
import json
import tkinter.messagebox
#import View

def saveMovie(param):
            name = open("savedmovies.txt", "a")
            name.write(param+"\n") #writes contents in file to usernames.txt
            #name.close() #closes file
            print("Saved\n")
            