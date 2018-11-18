# -*- coding: utf-8 -*-

from selenium import webdriver
#import time
br = webdriver.Firefox(executable_path='C:/Users/lewis/Downloads/geckodriver.exe')
br.implicitly_wait(15) # wait's for the page to get done
#loading before it does anything with it

dboption = input("Please select a movie DB (1 = OMDB) (2 = TheMovieDB): ");
type(dboption)


#Give output to console and expect a input from user
name = input("Please enter a movie: ");
type(name)

if dboption == "1":
    #API key with name variable
    br.get('http://www.omdbapi.com/?t='+name+'&apikey=5a902c4d')

else:
    #API key with name variable - themoviedb
    br.get('https://api.themoviedb.org/3/search/movie?api_key=da097a759910eefff9e3098e9e3d3870&query='+name)