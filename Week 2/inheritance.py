#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 12:05:45 2016

@author: janusboandersen
"""

class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))
    
x = [10,3,5,1,2,7,6,4,8]
y = MyList(x)
dir(x)
dir(y)