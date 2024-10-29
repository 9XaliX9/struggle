# What is a Set
# A set in mathematics is collection of unique elements.

# Sets are used for operations involving frequent intersection, union and difference operations.

# Create Sets in NumPy
# We can use NumPys unique() method to find unique elements from any array.
#  E.g. create a set array, but remember that set arrays should only be 1-D arrays.

import numpy as np

print("\033[96m\n{------------------------------")
"""                                   
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)

print(x)

print("\n------------------------------}\n\033[0m")
"""
# =======================================================================
# Finding Union:
# To find unique values of two arrays, use union1d() method.
"""
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)
                                        
print("\n------------------------------}\n\033[0m")"""

# =========================================================

# Finding Intersection
# To find only values that are present in both arrays, use intersect1d() method.
"""
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)
"""
# Note: intersect1d() method takes an optional argument assume_unique, which ifset to True
# can speed up computation. It should always be set to True when dealing with sets.

# =========================================================

# Finding Difference:
# To find only values in the first set that is NOT present in seconds set, use setdiff1d() method.
"""
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)

# Note: the setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.

# """
# Finding Symmetric Difference:
# To find only values that are NOT present in BOTH sets, use setxor1d() method.
"""
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)
"""

print("\n------------------------------}\n\033[0m")
