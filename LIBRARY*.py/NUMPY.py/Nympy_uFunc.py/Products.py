# Products: 
# To find the product of the elements in an array, use the prod() function.

import numpy as np

print("\033[96m\n{------------------------------")
                                        
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)

print(x)  #Returns: 24 because 1*2*3*4 = 24

print("\n------------------------------}\n\033[0m")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

y = np.prod([arr1, arr2])

print(y)
#Returns: 40320 because 1*2*3*4*5*6*7*8 = 40320
print("\n------------------------------}\n\033[0m")

# Product Over an Axis
# If you specify axis=1, NumPy will return the product of each array.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)   #Returns: [24 1680]
print("\n------------------------------}\n\033[0m")

#Cummulative product means taking the product partially.

#E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
# Perfom partial sum with the cumprod() function.

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)

print(newarr)
#Returns: [5 30 210 1680]
print("\n------------------------------}\n\033[0m")
