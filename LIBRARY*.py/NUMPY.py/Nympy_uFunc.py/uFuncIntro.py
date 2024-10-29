# What are ufuncs?
# ufuncs stands for "Universal Functions" and are NumPy functions that operate on ndarray object.

# Why use ufuncs?
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

# ufuncs also take additional arguments, like:

# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.

# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.
# It is faster as modern CPUs are optimized for such operations.
#                               ======================================================
"""
print("\033[96m\n{------------------------------")

x = [1, 2, 3, 4, 5]
y = [5, 5, 5, 5, 5]
z = []

for i, j in zip(x, y):  # zip is python build in function
    z.append(i + j)
print(z)

# but NumPy has ufunc for this, called add(x, y) that will produce same result.
# ---------------------------------------------------------------------------------
import numpy as np

a = np.add(x, y)
print(a)

print("\n------------------------------}\n\033[0m")
"""

print("\033[96m\n{------------------------------")

# To create your own ufunc, you have to define function,
# like you do with normal functions in Python,
# then add it to your NumPy ufunc library with frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs   - the number of input arguments (arrays).
# outputs  - the number of output arrays.

import numpy as np

def myMultiply(x, y, z):
    return x * y * z

myMultiply = np.frompyfunc(myMultiply, 3, 1)

print(myMultiply([1, 2, 3], [5, 6, 7], [3, 3, 3]))

# check if function is a function >>>>> A ufunc should return <class 'numpy.ufunc'>.
# If it's not a ufunc, it'll return another type, like built-in NumPy function for joining two or more arrays.

print(type(np.add))

print("\n------------------------------}\n\033[0m")
#        ***************** Complete *****************