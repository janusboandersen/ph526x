#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:57:55 2017

@author: janusboandersen
"""

#Implementation fo function(s) to read books
def read_book(title_path):
    """
    This function will read a book and return it as a string
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        
    #Replace special line break characters
    text = text.replace("\n", "").replace("\r", "")
    
    #Return the cleaned text
    return text;
#end of read_book
        
        