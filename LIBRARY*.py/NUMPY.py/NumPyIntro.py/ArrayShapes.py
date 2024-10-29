# Shapes + Reshapes

# The shape of an array is the number of elements in each dimension.
# The shape of an array is represented as a tuple of integers.

import numpy as np

"""
print("\033[96m\n{------------------------------")

# arr2= np.array([ [1,2,3,4,5] , [6,7,8,9,10] ])
# print(arr2.shape) # [2, 5] element in first [] and then in second []

arr = np.array([1,2,3,4],ndmin=5)

print(arr)
print("shape of array",arr.shape)

print("\n------------------------------}\n\033[0m")
"""
# Reshaping
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

"""
print("\033[96m\n{------------------------------")

arr = np.array([1,2,3,4, 5,6,7,8, 9,10,11,12])

# narr=arr.reshape(4,3) # 1d -> 2D
# print(narr)

# narr2=arr.reshape(2,3,2)# block,rows,columns
# print(narr2)

arr2= np.array([1,2,3,4,5,6,7,8])

print(arr2.reshape(2,4).base) #view

print("\n------------------------------}\n\033[0m")
"""
# unknown dimension
"""
print("\033[96m\n{------------------------------")

# arr=np.array([1,2,3,4,5,6,7,8])
# narr=arr.reshape(2,2,-1)
# print(narr)
# -------------------------------------------
# arr2= np.array([[1,2,3],[4,5,6]])

# narr2=arr2.reshape(-1,2,3) # same
# narr3=arr2.reshape(2,1,3)  # same

# print(narr2)
# print("\n")
# print(narr3)
# ------------------------------------------
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
narr2 = arr2.reshape(-1)
print(narr2)

# *** Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.***

print("\n------------------------------}\n\033[0m")
#      **** Shaping an Reshaping complete ****
"""
