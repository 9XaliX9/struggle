3
#   NumPy is used for working with arrays.
#   It also has functions for working in domain of linear algebra,
#    fourier transform, and matrices.

#   NumPy was created in 2005 by Travis Oliphant.
#   An open source project and you can use it freely.

# Why Use NumPy?#
# In Python we have lists that serve the purpose of arrays, but are slow to process.

# NumPy provides an array object that is up to 50x faster than traditional lists.

# The array object NumPy is called ndarray, it provides lot of supporting
# functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.

import numpy as np

"""
print("\033[95m\n{------------------------------")
                                        
import numpy as np
print("version",np.__version__,"\n") #checking numpy version.

arrr=[1,2,3,4,5]

arr1 = np.array([1,2,3,4,5])
arr2 = np.array((1,2,3,4,5))

print(arrr,"< different")

print("arr1->",arr1)
print("arr2->",arr2)

print(type(arr1))
print(type(arr2))

# To create an ndarray, we can pass a list, tuple or 
# any array-like object into the array() method, and 
# it will be converted into an ndarray:
                                 
print("\n------------------------------}\n\033[0m")
"""
#============================================================================================
"""
print("\033[96m\n{------------------------------")
# Dimensions in Arrays: A dimension in arrays is one level of array depth (nested arrays).
#------------------------------
# 0-D arrays
arr0 = np.array(42)

print("\033[92m0-D:", arr0)
# -----------------------------
# 1-D arrays
arr1 = np.array([1, 2, 3, 4, 5])

print("\033[94m1-D:", arr1)
# -----------------------------
# 2-d Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("\033[93m2-D:",arr2)
# -----------------------------
# 3-D Array
arr3 = np.array([ [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]] ])

print("\033[95m3-D:",arr3)
#------------------------------

print("\n\033[96m------------------------------}\n\033[0m")
"""
#=====================================================================
"""
print("\033[96m\n{------------------------------")

#check the dimension? use : .ndim

a= np.array(42)
b=np.array([1,2,3])
c=np.array([[1,2,3],[1,2,3]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print("Dimensions:",a.ndim)
print("Dimensions:",b.ndim)
print("Dimensions:",c.ndim)
print("Dimensions:",d.ndim)
print("\n")

# Higher Dimensional Arrays

# An array can have any number of dimensions.
# When array is created, you can define the number of dimensions using the ndmin .

arr =np.array([1,2,3,4], ndmin=5)
print(arr)
print(arr.ndim)

print("\n------------------------------}\n\033[0m")

#                                             ***complete basics*** 
"""










#### merge
#### merge
#### merge
#### merge