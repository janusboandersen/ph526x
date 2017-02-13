#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:36:30 2017

@author: janusboandersen
"""

import random
import matplotlib.pyplot as plt
import numpy as np

#Some examples in random numbers and data visualization

rolls = []

for k in range(1000000):
    rolls.append(random.choice([1,2,3,4,5,6]))

#visualize
plt.hist(rolls, bins = np.linspace(0.5, 6.5, 7), normed=True);
