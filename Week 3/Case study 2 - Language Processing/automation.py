#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:15:50 2017

@author: janusboandersen
"""

#Working with the OS
import os
book_dir = "./Books"

#Working with DataFrames
import pandas as pd
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))

#Keep track of the titles (DataFrame index)
title_num = 1

#Nested loop over language->author->title
for language in os.listdir(book_dir)[1:]:
    for author in os.listdir(book_dir + "/" + language)[1:]:
        for title in os.listdir(book_dir + "/" + language + "/" + author)[1:]:
            #
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            
            #Insert the data into a DataFrame
            stats.loc[title_num] = language, author, title, sum(counts), num_unique
            title_num += 1
            
        #end title
    #end author
#end language

