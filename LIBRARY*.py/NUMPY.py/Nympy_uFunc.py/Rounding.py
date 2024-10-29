# *Rounding Decimals

# There are primarily five ways of rounding off decimals in NumPy:

# 1) truncation
# 2) fix
# 3) rounding
# 4) floor
# 5) ceil

import numpy as np

print("\033[96m\n{------------------------------")

arr = np.trunc([-3.9666, 3.6667])
print(arr)

arr2 = np.around(-3.199, 2)  # 3 here is sig fig
print(arr2)

arr3 = np.floor(3.9)
print(arr3)

arr4 = np.ceil(3.1)
print(arr4)

print("\n------------------------------}\n\033[0m")
#       ************** Complete *************