#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:55:09 2016

@author: janusboandersen
"""

def update(n,x):
    n = 2
    x.append(4)
    print("update: ", n, x)
    
    
def main():
    n = 1
    x = [0, 1, 2, 3]
    print("main: ", n, x)
    update(n,x)
    print("main: ", n, x)
    
main()



    