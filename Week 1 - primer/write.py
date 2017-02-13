#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:19:11 2016

@author: janusboandersen
"""

F = open("input.txt", "w") 
F.write("Hello\nWorld") 
F.close() 
lines = [] 
for line in open("input.txt"): 
    lines.append(line.strip()) 
print(lines) 



def is_vowel(letter):
   if letter in "aeiouy":
     return(True)
   else:
     return(False)
     
     
def is_vowel(letter): 
    if type(letter) == int: 
        letter = str(letter) 
    if letter in "aeiouy": 
        return(True) 
    else: 
        return(False)


        