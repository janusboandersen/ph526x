#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:29:31 2017

@author: janusboandersen
"""

#text = "This is my test text. We're keeping this short to keep things manageable."

from collections import Counter


#this implemention is based on the Counter object from collections
def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Returns a dictionary
    where keys are unique words and values are word counts. Skips punctuations.
    """
    
    #Various steps to prevent inflated word count
    #Lower case
    text = text.lower()
    
    #Characters to skip
    skips = list(".,;:'\"")
#    skips.append('"')
    
    for s in skips:
        text = text.replace(s, "")
    
    word_counts = Counter(text.split(" "))

    #print(word_counts)
    
    return word_counts;




#this implementation relies on a Python dict and a manual splitting and looping over the word list
def count_words(text):
    """
    Count the number of times each word occurs in text (str). Returns a dictionary
    where keys are unique words and values are word counts. Skips punctuations.
    """
    
    #Various steps to prevent inflated word count
    #Lower case
    text = text.lower()
    
    #Characters to skip
    skips = list(".,;:'\"")
#    skips.append('"')
    
    for s in skips:
        text = text.replace(s, "")
    
    word_counts = {}
    for word in text.split(" "):
        #known word
        if word in word_counts:
            word_counts[word] += 1
        #unknown word
        else:
            word_counts[word] = 1
        #end if
    #end for

    #print(word_counts)
    
    return word_counts;
#end count_words



def word_stats(word_counts):
    """
    Returns summary statistics for the word count in a tuple.
    Number of unique words
    Word frequencies
    """
    #Count unique words
    num_unique = len(word_counts)
    
    #Return word count for every single unique word in the dictionary
    counts = word_counts.values()
    
    #Return
    return (num_unique, counts)
    
#end word_stats


