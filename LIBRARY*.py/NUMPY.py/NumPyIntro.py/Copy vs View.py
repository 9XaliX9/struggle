#Copy vs view

# Main difference between copy and view of an array is that copy is a new array, and view is just view of original array.
# Copy owns data and any changes made to copy will not affect original array, and any changes made to original array will not affect copy.
# The view does not own data and any changes made to view will affect original array, and any changes made to original array will affect view.

import numpy as np
"""
print("\033[96m\n{------------------------------")

##############copy###############
# arr2= np.array([ 1,2,3,4,5,6,7,8,9,10])

# narr2=arr2.copy()
# arr2[0]=4

# print(arr2)
# print(narr2)

#############view###############
arr2= np.array([1,2,3,4,5,6,7,8,9,10])

newarr2=arr2.view()
arr2[0]=4

print(arr2)
print(newarr2)
#----------------------------------------
print("\n------------------------------}\n\033[0m")

#check if array owns its data
print("\033[96m\n{------------------------------")

arr= np.array([1,2,3,4,5,6,7,8,9,10])

x=arr.copy()
y=arr.view()

print(x.base)# none means own database
print(y.base)# else not owns

print("\n------------------------------}\n\033[0m")
                ***complete***
"""
