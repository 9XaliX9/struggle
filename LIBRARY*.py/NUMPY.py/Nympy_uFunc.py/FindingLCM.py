# Finding LCM (Lowest Common Multiple)

# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

import numpy as np

print("\033[96m\n{------------------------------")

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

# The reduce() method will use the ufunc, in this case the lcm() function,
# on each element, and reduce the array by one dimension.

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)

print("\n------------------------------}\n\033[0m")

# ***************** Complete ********************