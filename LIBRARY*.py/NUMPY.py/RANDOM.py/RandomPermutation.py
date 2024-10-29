# *Random Permutations of Elements

# Permutation refers to arrangement of elements. e.g. [3, 2, 1] is permutation of [1, 2, 3] and vice-versa.
# NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays:
# Shuffle means changing arrangement of elements in-place. i.e. in array itself.

from numpy import random
import numpy as np

print("\033[96m\n{------------------------------")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

random.shuffle(arr1)         #1 way
random.permutation(arr2)     #2 way

print(arr1)
print(arr2)

#The permutation() method returns a re-arranged array (and leaves the original array un-changed).

print("\n------------------------------}\n\033[0m")
