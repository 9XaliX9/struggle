# Trigonometric Functions:
# NumPy provides ufuncs sin(), cos() and tan() that take values in radians and produce corresponding sin, cos and tan values.

import numpy as np

print("\033[96m\n{------------------------------")
"""
a = np.sin(np.pi/2)
print(a)
"""
# ===============================================
"""
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
b = np.sin(arr)
print(b)
"""
# ===============================================
# Convert Degrees Into Radians:
"""
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)

print(x)
"""
# ================================================
# Radians to Degrees
"""
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)

print(x)
"""
# =================================================
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

# NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values.

# x = np.arcsin(1.0)
# print(x)
# ==================================================

# Finding hypotenues using pythagoras theorem in NumPy.

# NumPy provides the hypot() function that takes the base and
# perpendicular values and produces hypotenues based on pythagoras theorem.
"""
base = 3
perp = 4

x = np.hypot(base, perp)

print(x)
"""
print("\n------------------------------}\n\033[0m")
