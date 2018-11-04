# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
#import time
br = webdriver.Firefox(executable_path='C:/Users/lewis/Downloads/geckodriver.exe')
br.implicitly_wait(15) # wait's for the page to get done
#loading before it does anything with it

name = input("Please enter a movie ");
type(name)


br.get('http://www.omdbapi.com/?t='+name+'&apikey=5a902c4d')
# to fill out a form
#search = br.find_element_by_name('q')
#search.send_keys('blade runner')
#search.submit()
#time.sleep(5)
#print(br.title)