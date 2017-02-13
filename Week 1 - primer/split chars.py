#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:44:00 2016

@author: janusboandersen
"""

import string
alphabet = list(string.ascii_letters)

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

#count_letters = dict()
#count_set = set(list(sentence))

#for char in count_set:
#    count_letters[char] = sentence.count(char)

    
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    
