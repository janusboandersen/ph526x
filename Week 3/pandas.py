#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:53:14 2017

@author: janusboandersen
"""

import math as m
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create columns
cols = ("x", "sinx", "cosx", "tanx", "sinx * cosx")

#Create a dataframe
data = pd.DataFrame(columns = cols)

x_range = np.linspace(0, 2 * m.pi, 50)

for i, x in enumerate(x_range):
    data.loc[i] = x, m.sin(x), m.cos(x), m.tan(x), m.cos(x)*m.sin(x)
#end for


#Plot
plt.figure(figsize=(10,10))
subset = data[["x", "cosx"]]
