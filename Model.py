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
            
def delete(line_to_replace):
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
    
    #Rating Delete
    with open(rating_file, 'r') as file:
        lines = file.readlines()
    if len(lines) > int(line_to_replace):
        lines[line_to_replace] = ""
        with open(rating_file, 'w') as file:                            
                file.writelines( lines )
               
    #Comment Delete
    with open(comment_file, 'r') as file:
        lines = file.readlines()
    if len(lines) > int(line_to_replace):
        lines[line_to_replace] = ""
        with open(comment_file, 'w') as file:                            
                file.writelines( lines )            
                
def addComment(line_to_replace, input):
                my_file = 'savedComment.txt'

                with open(my_file, 'r') as file:
                    lines = file.readlines()
                    
                if 11 > int(line_to_replace):
                    print("TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
                    lines[line_to_replace] = input+"\n"
                    with open(my_file, 'w') as file:                            
                            file.writelines( lines )

def addRating(line_to_replace, input):
                my_file = 'savedratings.txt'

                with open(my_file, 'r') as file:
                    lines = file.readlines()
                    
                if len(lines) > int(line_to_replace):
                    lines[line_to_replace] = input+"\n"
                if input == "1" or input == "2" or input == "3" or input == "4" or input == "5":
                    with open(my_file, 'w') as file:
                        file.writelines( lines )  
                else:
                    messagebox.showwarning("Warning","Pick a number from 1 to 5")