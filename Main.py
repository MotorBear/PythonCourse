#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@course: Python is Easy

@assignment: Homework #1

@description: Defines and display metadata for a single composition

@created: on Thu Feb 11 07:33:32 2021

@author: Claus Derlien

@title: Metadata for music
"""
# defines name of artist/group/band
Artist = "Pink Floyd"
# defines music style/genre
Genre = "Progressive Rock"
# defines Album name
Album = "The Dark Side of the Moon"
# defines year of release
ReleasedYear = 1973
# defines album side of this song 
Side = "A"
# defines number on song for this side
SongNumber = 1
# defines title of song
SongTitle = "Speak to Me"
# defines Author of song
SongAuthor = "Mason"
# defines Lead vocal on this song, nb. if no vocals use Instrumental
LeadVocal = "Instrumental"
# defines song durations in seconds as an integer
DurationInSeconds = 90
# defines song duration as a string in whole minutes using floor division
DurationMinutes = str(DurationInSeconds // 60) + " min. "
# defines song duration as a float in minutes
DurationInMinutes = DurationInSeconds / 60
# defines remaining seconds as a string using modulus
DurationSeconds = str(DurationInSeconds % 60) + " secs."
#
# Print defined variables
#
print(Artist)
print(Genre)
print(Album)
print(ReleasedYear)
print(Side)
print(str(SongNumber) + ". " + SongTitle)
print("Author : " + SongAuthor)
print("Lead vocal : " + LeadVocal)
print("Duration in minutes :",DurationInMinutes )
print("Duration In Seconds :", DurationInSeconds)
print("Duration : " + DurationMinutes + DurationSeconds)
