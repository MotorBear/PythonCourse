#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:01:46 2021

@course: Python is Easy

@assignment: Homework #4

@description: Lists

@author: Claus Derlien

I specifically avoided using loops as that has not been on the agenda, 
so this is my attempt at doing it without loops or while's'

"""

# define variables for this assignment
global myUniqueList
global myLeftOvers
# this list is to feed the elements to be added to myUniqueList
global FeedList
global FeedListNumbers
#initialize variables
myUniqueList = []
myLeftOvers = []
FeedList = [1,2,7,5,2,4,8,9,11,1,3]
FeedListNumbers = len(list(FeedList))
#define functions
def addToList(element):
    if myUniqueList.count(element) > 0 :
        # element to add already exists
        myLeftOvers.append(element)
        print(element,"added to myLeftOvers")
    else:
        # element is unique
        myUniqueList.append(element)
        print(element," added to myUniqueList")
    return
    


#proof befoore values
print("--Start Conditions--------------------")
print("myUniqueList = ",myUniqueList)
print("myLeftOvers  = ",myLeftOvers)
print("FeedList     = ",FeedList)
print(FeedListNumbers)
print("--Add Elements------------------------")
addToList(FeedList[0])
addToList(FeedList[1])
addToList(FeedList[2])
addToList(FeedList[3])
addToList(FeedList[4])
addToList(FeedList[5])
addToList(FeedList[6])
addToList(FeedList[7])
addToList(FeedList[8])
addToList(FeedList[9])
addToList(FeedList[10])
# for added credit sortig the myUniqueList
myUniqueList.sort()
print("-End Conditions-----------------------")
print("myUniqueList = ",myUniqueList)
print("myLeftOvers  = ",myLeftOvers)
print("FeedList     = ",FeedList)
print(FeedListNumbers)