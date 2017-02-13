#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:29:01 2017

@author: janusboandersen
"""

#Euclidian distance for the k-nearest neighbours (kNN) implementation
import numpy as np

#Euclidian distance                      
def distance(p1, p2):
    """
    Computes the Euclidian distance between two points p1 and p2.
    The points p1 and p2 should be equal-sized numpy arrays
    """ 
    return np.sqrt(np.sum(np.power(p2-p1, 2)))
#End of function def

#Try it out
p1 = np.array([1,1])
p2 = np.array([4,4])

print(distance(p1,p2))
