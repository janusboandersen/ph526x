#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:55:18 2017

@author: janusboandersen
"""

#Create Caesar cipher algorithm

#build dictionary of all lowercase English letters (26: 0..25)
#letters = {key-97: chr(key) for key in range(97,97+26)}


def caesar(message, key):
    # return the encoded message as a single string!

    alphabet = string.ascii_lowercase + " "
    letters = dict(enumerate(alphabet)) 

    #Build dict for encoding - shift alphabet by key and wrap around
    encode = {char: (value + key) % (26+1) for (value, char) in enumerate(alphabet)}

    #Build string by mapping into encoded keyset and back to letters
    code = ""
    for c in message:
        code += letters[encode[c]]
        
    return code;

    
message = "hi my name is caesar"
key = 3

coded_message = caesar(message, key)
print(coded_message)

decoded_message = caesar(coded_message, -3)
print(decoded_message)
    
