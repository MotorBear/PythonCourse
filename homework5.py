#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 11:27:33 2021

@assignment: Homework #5

@description: Basic Loops

@author: Claus Derlien

"""
# importing math module for sqrt function
import math

#defining function to return True if given number is a prime
def isPrime(n) :
    Result = True
    if n <= 0 :
        return False
    if n == 1 :
        return False
    s = int(math.sqrt(n))
    for i in range(2,s+1,1):
        if n % i == 0 :
            Result = False
            break
    return Result
    
#setting up for looping through 1 to 100
# i have tried to minimize number of executing lines to a minimum by using 
# continue on all test cases, this will make this code snippet very efficient
for count in range(1,101,1) :
    test3 = count % 3
    test5 = count % 5
    # if isPrime returns true we have a prime
    if isPrime(count) == True :
        print(count,"Prime")
        continue
    # if both test3 and test5 has a remainde we have the common situation
    # and after printing count we resume the loop by using continue
    if test3 > 0 and test5 > 0 :
        print(count)
        continue
    #if test3 = = and test5 has a remainder we print Fizz and continue
    if test3 == 0 and test5 > 0 :
        print(count,"Fizz")
        continue
    #if test3 has a remainder and test5  = 0 we print Buzz and contine 
    if test3 > 0 and test5 == 0 :
        print(count, "Buzz")
        continue
    #if both test3 & test5 = 0 we print FizzBuzz and continue
    if test3 == 0 and test5 == 0 :
        print(count, "FizzBuzz")
        continue
    
