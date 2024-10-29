# Array Split
# Splitting is reverse operation of Joining.
# We use np.array_split() for splitting arrays

import numpy as np
"""
print("\033[96m\n{------------------------------")

arr2= np.array([1,2,3,4,5,6,7,8,9 ])

arr=np.array_split(arr2,3) #[array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
print(arr)

# If the array has less elements than required,
# it will adjust from the end accordingly.

newarr= np.array_split(arr2,4) #[array([1, 2, 3]), array([4, 5]), array([6, 7]), array([8, 9])]
print(newarr)

print("\n")
narr = np.array_split(arr2,4)
print(narr[0],narr[1],narr[2])

print("\n------------------------------}\n\033[0m")
"""
# Splitting 2-D Arrays
"""
print("\033[96m\n{------------------------------")

arr2= np.array([ [1,2] ,[3,4] , [5,6] ,[7,8],[9,10] ])

newarr= np.array_split(arr2, 3)
print(newarr[0],newarr[1],newarr[2])

print("\n------------------------------}\n\033[0m")
"""
"""
print("\033[96m\n{------------------------------")

arr2= np.array([ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18] ])

newarr= np.array_split(arr2,3)          # row view
# newarr= np.array_split(arr2,3,axis=1) # column view

print(newarr[0])
print("\n")
print(newarr[1])
print("\n")
print(newarr[2])

print("\n------------------------------}\n\033[0m")
# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().

"""