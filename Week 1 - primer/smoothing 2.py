#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 00:00:34 2016

@author: janusboandersen
"""

#Smoothing by symmetric average of neighbors
def MA_sym(x,symmetric_points=1):
    n = len(x)  #original list size
    bandwidth = symmetric_points * 2 + 1  #width of the moving MA band
    x = [x[0]]*symmetric_points + x  #padding the left boundary for MA
    x = x + [x[-1]]*symmetric_points #padding the right boundary
    MA = [sum(x[i:i+bandwidth])/bandwidth for i in range(n)]  #slice out the relevant points and average them
    return MA    

x=[0,10,5,3,1,5]
print(MA_sym(x,1))