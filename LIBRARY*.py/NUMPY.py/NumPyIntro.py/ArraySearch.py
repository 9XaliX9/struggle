# Search
# To search an array, use the where() method.
import numpy as np
"""
print("\033[96m\n{------------------------------")

arr2= np.array([ 1,2,6,4,3,427,4,432,6 ])

x=np.where(arr2==4) #(array([3, 5, 8]),) 3,5,8 are indexes
print(x)

even=np.where(arr2%2==0)
print(even)

odd=np.where(arr2%2==1)
print(odd)

print("\n------------------------------}\n\033[0m")
"""
# search sorted
"""
print("\033[96m\n{------------------------------")
#              [0,1,2,3,4, 5]
arr = np.array([5,6,7,8,9,10])

x = np.searchsorted(arr,8) # 3 -> index
print(x)

print("\n------------------------------}\n\033[0m")
"""
"""
print("\033[96m\n{------------------------------")

arr2= np.array([1,3,5,7])
x = np.searchsorted(arr2, [2,4,6]) 

# Return value is an array: [1 2 3] containing three indexes where 2, 4, 6 
# would be inserted in original array to maintain order.

print(x)
print("\n------------------------------}\n\033[0m")
#           *** Search completed ***
"""
