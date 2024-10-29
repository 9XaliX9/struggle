#Data Distribution

# What is Data Distribution>> is list of all possible values, and how often each occurs.
# important when working with statistics and data science.
# Probability Density Function: A function that describes continuous probability.
# i.e. probability of all values in array.

import numpy as np
from numpy import random

"""
print("\033[96m\n{------------------------------")

x= random.choice([3,5,7,9],p=[.1, .3, .6, .0], size=100) #Sum of all probability numbers should be 1. (.1 +.3+ .6+ .0)
print(x)
#can change shapes
print("\n")
y= random.choice([3,5,7,9],p=[.1, .3, .6, .0], size=(3,5))
print(y)

print("\n------------------------------}\n\033[0m")
"""
#==============================================================================================
#==============================================================================================
#Random Permutation 

# Permutation refers to arrangement of elements. 
# e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

# NumPy Random module provides two methods for this: shuffle() and permutation().

# The shuffle() method makes changes to the original array.
# Permutation() method returns a re-arranged array (and leaves the original array un-changed).

print("\033[96m\n{------------------------------")

arr= np.array([1,2,3,4,5])
random.shuffle(arr)

print(arr)

arr2= np.array([1,2,3,4,5,6,7,8])
print(random.permutation(arr2))

print("\n")
print(arr,"      >changed")
print(arr2,">unchanged")

print("\n------------------------------}\n\033[0m")

#