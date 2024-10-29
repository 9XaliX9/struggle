#Slicing

# Slicing means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start(inclusive):end(exclusive)].
# We can also define the step, like this: [start:end:step].
# If we dont pass end its considered length of array in that dimension.

import numpy as np

"""
print("\033[96m\n{------------------------------")
#              [0, 1, 2, 3, 4, 5, 6] 
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#             [-7 -6 -5 -4 -3 -2 -1]

print(arr[4:6]) #5 6
print(arr[3:])# 45 6 7 
print(arr[:-5])# removes last 5
print(arr[::2])# skips every second 
print(arr[-3:-1])#5 6
print(arr[1:5:2])#2 4

print("\n------------------------------}\n\033[0m")
"""
# 2D slicing----------------------------------
"""
print("\033[96m\n{------------------------------")

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr2[1,1:4])
# print(arr2[0,1:3])
# print(arr2[0:2,1])
# print(arr2[0:2, 1:4])

print("\n------------------------------}\n\033[0m")
            **** Slicing complete ****
"""
