#Iterating

# Iterating means going through elements one by one.
import numpy as np

#  np.nditer  #
"""
print("\033[96m\n{------------------------------")
# 1 D----------------------
arr=np.array([1,2,3])

for x in arr:
    print(x)

# 2 D----------------------
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# for x in arr2:
#     print(x)

# for x in arr2:
#     for y in x:
#         print(y)
# 3 D----------------------
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr3:
#     for y in x:
#         for z in y:
#             print(z)  #below one is short cut

for x in np.nditer(arr3):
    print(x)

print("\n------------------------------}\n\033[0m")
"""
#-------------- ndenumerate() #
"""
print("\033[96m\n{------------------------------")

arr= np.array([ [1,2,3,4],[5,6,7,8]])

print(" c, r")  # column | and rows --
for index, value in np.ndenumerate(arr):
    print(index, "->",value)

print("\n------------------------------}\n\033[0m")
            # *** Iterating complete ***
"""
