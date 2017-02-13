#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:18:59 2017

@author: janusboandersen
"""

#random walk
import numpy as np
import matplotlib.pyplot as plt

#delta_X is the displacement: row0=x-direction, row1=y-direction
delta_X = np.random.normal(0,1,(2,1000))

#plot the displacements
#plt.plot(delta_X[0], delta_X[1], "go");

#position of random-walker; cumulative sum
X = np.array([[0], [0]]) #start position (0,0)
X = np.append(X,np.cumsum(delta_X, axis=1),axis=1)  #add together all the columns

#Plot the position at time t=1..n
plt.plot(X[0], X[1], "b-");