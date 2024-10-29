# Data Types in Python:

# strings - used to represent text data         ->  "ABCD"
# integer - used to represent integer numbers.  -> -1, -2, -3
# float   - used to represent real numbers.     -> 1.2, 42.42
# boolean - used to represent  True or False.
# complex - used to represent complex numbers.  -> 1.0 + 2.0j


# Data Types in NumPy

# i - integer                   f - float
# b - boolean                   c - complex float
# u - unsigned integer          m - timedelta

# M - datetime                  U - unicode string
# O - object                    V - fixed chunk of memory for other type (void)
# S - string

import numpy as np
"""
print("\033[96m\n{------------------------------")

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2.dtype)


arr3 = np.array(["apple", "banana", "orange", 9.9])
print(arr3.dtype)
print(len(arr3))

print("\n------------------------------}\n\033[0m")
"""
#Creating Array with a defined Data type
"""
print("\033[96m\n{------------------------------")
                                        
# arr2= np.array([1,2,8,4,5,6,7,8,9,10], dtype ='S')
# print(arr2)
# print(arr2.dtype)

arr2= np.array([1,2,3,4,5,6,7], dtype='i4')
print(arr2.dtype)

print("\n------------------------------}\n\033[0m")
"""
#what if a value cannot be converted
# In Python ValueError/TypeError is raised when type of passed argument to function is incorrect.
"""
print("\033[96m\n{------------------------------")

#Converting Data Type on Existing Arrays
# Best way to change data type of an existing array, is to make copy of the array with astype() method.

# astype() function creates copy of array, and allows you to specify data type as parameter.

# Data type can be specified using string, like 'f' for float, 'i' for integer etc. or use the data type directly like float for float and int for integer.

arr2= np.array([ 1.2, 23.3, 23.1, 5.6 ])

# newarr=arr2.astype('int')
# print(newarr)
# print(newarr.dtype)

newarr = arr2.astype(bool)
print(newarr)
print(newarr.dtype)

print("\n------------------------------}\n\033[0m")
#               **** DataTypes complete ****
"""
