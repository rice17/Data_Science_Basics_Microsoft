# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:28:09 2016

@author: abhishar
"""

import pandas as pd

data = pd.read_csv("students.data")
my_data = data[["G1", "G2", "G3"]]

import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

#my_data.plot.hist(title = "G1", bins = 10, alpha = 0.5)
"""my_data.G2.plot.hist(title = "G2", bins = 10, alpha = 0.5)
my_data.G3.plot.hist(title = "G3", bins = 10, alpha = 0.5)
"""
plt.scatter(x = my_data.G1, y = my_data.G2)
plt.show()