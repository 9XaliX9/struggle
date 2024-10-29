# Filtering

# Getting some elements out of an existing array and
# creating new array out of them is called filtering.

# In NumPy, you filter an array using boolean index list.

# If value at index is True that element is contained in filtered array,
# if value at that index is False that element is excluded from filtered array.

import numpy as np

"""
print("\033[96m\n{------------------------------")

arr2= np.array( [41,42,43,44] )

x=[True,False,True,False] # [41 43]

newarr=arr2[x]
print(newarr)
print("\n------------------------------}\n\033[0m")
"""
# Create a filter array that will return only values higher than 42:
"""
print("\033[96m\n{------------------------------")

arr2= np.array([ 41,42,43,44] )

filter_arr=[]

for x in arr2:
    if x>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr=arr2[filter_arr]

print(filter_arr)
print(newarr)

#easy way down===================================

arr2= np.array([ 41,42,43,44] )

filter_arr=arr2>42
newarr=arr2[filter_arr]

print(filter_arr)
print(newarr)

print("\n------------------------------}\n\033[0m")
"""
# Create filter array that will return even elements from original array:
"""
print("\033[96m\n{------------------------------")

arr=np.array([1,2,3,4,5,6,7,8,9])

filter_arr=[]

for x in arr:
    if (x%2==0):
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr=arr[filter_arr]

print(filter_arr)
print(newarr)

# easy down==========================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("\n------------------------------}\n\033[0m")
#               **** Filters complete ****
"""
