# Iterating

# ***Numpy Array Indexing***
# Array indexing is the same as accessing an array element.
# You can access array element by referring to its index number.
# Indexes in NumPy arrays start with 0, meaning that first element 
# has index 0, and second has index 1 etc.

import numpy as np
"""
print("\033[96m\n{------------------------------")
#     index:  [0,1,2,3]
arr =np.array([1,2,6,8])

print(arr[0])                                       
print(arr[1])                                       
print(arr[2])                                       
print(arr[3])    

print(arr[2]+arr[3])  # index 2 +3 which is 6+8=14
print("\n---2D:")
#---------------------------------------------------
#accessing 2-D arrays
#              [  0  ],[  1   ]   rows>>  columns\/
#              [0,1,2],[0,1,2] index
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2[0,1])
print(arr2[1,2])
print("\n---3D:")
#---------------------------------------------------
#accessing 3-D arrays

arr3=np.array([[ [1,2,3],[4,5,6]] ,[ [7,8,9],[10,11,12]] ])
#5 #11
print(arr3[0,1,2])#6
print(arr3[1,0,1])#8
print("\n------------------------------}\n\033[0m")
"""
#NEGATIVE INDEXING--------------------------------------
"""
print("\033[96m\n{------------------------------")

arr2= np.array([ [1,2,3,4,5] , [6,7,8,9,10] ])
print(arr2[1,-1])#10

arr3 = np.array([[ [1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3[1,0,-2])#8
print(arr3[1,1,-3])#10

print("\n------------------------------}\n\033[0m")
#                                          **** Indexing complete ****
"""

