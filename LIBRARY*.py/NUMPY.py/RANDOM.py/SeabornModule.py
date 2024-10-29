#SEABORN

# Seaborn is a library that uses Matplotlib underneath to plot graphs.
# It will be used to visualize random distributions.



import numpy as np
from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb


"""
print("\033[96m\n{------------------------------")
# use displot instead of distplot and 
# 'kind='ked' for graph
# 'kind'='hist' for histogram

data =[1,2,3,4,5,6]

sb.displot(data, kind="kde")  # histogram and KDE
plot.show()

print("\n------------------------------}\n\033[0m")
"""

"""
print("\033[96m\n{------------------------------")
#Gaussian (Normal) distribution

# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:

# loc   - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat graph distribution should be.
# size  - The shape of the returned array.

sb.displot(random.normal(size=1000),kind='kde')
plot.show()

print("\n------------------------------}\n\033[0m")
#                 **** Normal distribuiton complete ****
"""
