# Summations:

# What is the difference between summation and addition?
# Addition is done between two arguments whereas summation happens over n elements.

import numpy as np
print("\033[96m\n{------------------------------")

"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)
"""
# ===================================================
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)
"""
# ====================================================
# Cummulative sum means partially adding the elements in array.

# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
# Perfom partial sum with the cumsum() function.

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)

print(newarr)

print("\n------------------------------}\n\033[0m")