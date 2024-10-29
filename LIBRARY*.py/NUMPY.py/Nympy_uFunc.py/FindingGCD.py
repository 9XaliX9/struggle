# Finding GCD (Greatest Common Denominator)

# The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor)
# is the biggest number that is a common factor of both of the numbers.
print("\033[96m\n{------------------------------")
"""
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)
"""
# Returns: 3 because that is the highest number
# both numbers can be divided by (6/3=2 and 9/3=3).
# ====================================================================

# The reduce() method will use the ufunc, in this case the gcd() function,
# on each element, and reduce the array by one dimension.

import numpy as np

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)

print(x)

print("\n------------------------------}\n\033[0m")
