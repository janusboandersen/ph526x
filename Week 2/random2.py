#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:44:41 2017

@author: janusboandersen
"""

#simulate sum of rolling multiple dice
import random
import matplotlib.pyplot as plt
import numpy as np

#Some examples in random numbers and data visualization

ys = []
for j in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y += x
    ys.append(y)

    
#visualize
#By the Central Limit Theorem (CLT), a large sum of random variables will 
#converge to follow a normal distribution
plt.hist(ys, normed=True);
