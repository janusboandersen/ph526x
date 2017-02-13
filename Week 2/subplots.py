#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:09:42 2017

@author: janusboandersen
"""
import numpy as np
import matplotlib.pyplot as plt

#generate rns
x = np.random.gamma(2, 3, 100000)

#generate a figure
plt.figure()

#subplot 1
plt.subplot(2,2,1)
plt.hist(x, bins=30)

#subplot 2
plt.subplot(2,2,2)
plt.hist(x, bins=30, normed=True)

#subplot 3
plt.subplot(2,2,3)
plt.hist(x, bins=30, normed=True, cumulative=True)

#subplot 4
plt.subplot(2,2,4)
plt.hist(x, bins=30, normed=True, cumulative=True, histtype="step")

