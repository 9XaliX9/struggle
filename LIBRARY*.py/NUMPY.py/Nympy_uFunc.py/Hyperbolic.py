# Hyperbolic Functions:

# NumPy provides ufuncs sinh(), cosh() and tanh() that take values
# in radians and produce corresponding sinh, cosh and tanh values.

print("\033[96m\n{------------------------------")

import numpy as np

"""
x = np.sinh(np.pi/2)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

y = np.cosh(arr)

print(x)   
print(y)
"""
# =============================================================

# Finding angles from values of hyperbolic sine, cos, tan.
# E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).

# Numpy provides ufuncs arcsinh(), arccosh() and arctanh()
# that produce radian values for sinh, cosh and tanh values given.
"""
x = np.arcsinh(1.0)

print(x)
"""
# ===========================================================
# Angles of Each Value in Arrays:

# arr = np.array([0.1, 0.2, 0.5])
# x = np.arctanh(arr)

# print(x)

print("\n------------------------------}\n\033[0m")
