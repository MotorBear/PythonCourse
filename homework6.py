#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:26:52 2021

@assignment: Homework #6

@description: Advanced loops

@author: Claus Derlien
"""
rows = 15
columns = 44

def RenderGameBoard(rows,columns) :    
    if rows < 2 or columns < 2 or rows > 15 or columns > 40:
        return False
    for y in range(1,rows * 2,1):
        if y % 2 == 0 :
            print("-" * ((columns * 2)-1))
        else:
            for x in range(1,columns * 2,1):
                if x % 2 == 0:
                    print("|",end = "")
                else: 
                    print(" ",end= "")
            print("")
    return True         
    
            
  
if RenderGameBoard(rows, columns) == True:
    print("parameters were ok")
else:
    print("Parameters were to big or too small")
          
            
        