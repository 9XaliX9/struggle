# # Logs

# NumPy provides functions to perform log at the base 2, e and 10.
# All of log functions will place -inf or inf in elements if log can not be computed.

# Log at Base 2
# Use the log2() function to perform log at the base 2.


import numpy as np

print("\033[96m\n{------------------------------")

arr = np.arange(1,10)

print(arr)
print("\n")

print(np.log2(arr)) 
print("\n")  

print(np.log10(arr))
print("\n")

print(np.log(arr))
print("\n")

#Log at Any Base:

# NumPy does not provide any function to take log at any base,
#  so we can use the frompyfunc() function along with inbuilt 
# function math.log() with two input parameters and one output parameter:

from math import log

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

print("\n------------------------------}\n\033[0m")

# ********* Complete ***********