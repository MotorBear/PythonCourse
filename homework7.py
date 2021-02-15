#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@course: Python is Easy

@assignment: Homework #7

@description: 

@created: on  Feb 11 07:33:32 2021

@author: Claus Derlien

@title: Metadata for music
"""
#setup the Dictionary
Dictionary = {}
Dictionary = {"Artist":"Pink Floyd",
              "Genre":"Progressive Rock",
              "Album":"The Dark Side of the Moon",
              "ReleasedYear":1973,
              "Side":"A","SongNumber":1,
              "SongTitle":"Speak to Me",
              "SongAuthor":"Mason",
              "LeadVocal":"Instrumental",
              "DurationInSeconds":90}
# to add remaining 3 keys which depends on Seconds i extract seconds first
Seconds = Dictionary["DurationInSeconds"]
# add remaining keys to dictionary using calculations based on Seconds
Dictionary["DurationMinutes"] = Seconds // 60
Dictionary["DurationInMinutes"] = Seconds / 60
Dictionary["DurationSeconds"] = Seconds % 60

#Function for guessing any key,value in the dictionary
def Guess(key,value):
    if  str(Dictionary[key]) == str(value):
        result = True
    else:
        result = False
    return result
while True:
    key = ""
    value = ""
    for key in Dictionary:
        print(key,end=" ")
        print("")

    key =   input("Please enter a key from above line (x to quit): ")   
    if key == "x":
        print("Program aborted!")
        break
    value = input("Please guess value of key : ")
    
    if Guess(key,value):
        print("-----------")
        print("!!! SUCCESS !!!")
        print("-----------")
    else:
        print("*****************")
        print("* You Blew it!  correct result = ", Dictionary[key]," *")
        print("*****************")
