# -*- coding: utf-8 -*-

from selenium import webdriver
#import time
br = webdriver.Firefox(executable_path='C:/Users/lewis/Downloads/geckodriver.exe')
br.implicitly_wait(15) # wait's for the page to get done
#loading before it does anything with it

#Give output to console and expect a input from user
name = input("Please enter a movie ");
type(name)

#API key with name variable
br.get('http://www.omdbapi.com/?t='+name+'&apikey=5a902c4d')
