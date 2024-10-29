# * Differences:

# A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
# To find the discrete difference, use the diff() function.

import numpy as np

print("\033[96m\n{------------------------------")

arr = np.array([10, 15, 25, 40, 5])

newarr = np.diff(arr, n=2)  # n 2 mean done twice
print(newarr)

print("\n------------------------------}\n\033[0m")

#       ******* Complete ***********

