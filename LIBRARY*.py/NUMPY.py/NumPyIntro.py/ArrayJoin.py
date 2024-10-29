#Joining

# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass sequence of arrays that we want to join to concatenate() function, along with axis.
# If axis is not explicitly passed, it is taken as 0.

import numpy as np
"""
print("\033[96m\n{------------------------------")

#---------------------------------
#joining 1d arrays

# arr1= np.array( [1,2,3,4,5  ])
# arr2= np.array( [6,7,8,9,10 ])

# arr = np.concatenate((arr1,arr2))
# print(arr)
#---------------------------------
#joining 2d arrays

arr1= np.array([ [1, 2, 3, 4, 5 ] , [6, 7, 8, 9, 10]   ])   #   []+[]
arr2= np.array([ [11,12,13,14,15] , [16,17,18,19,20]  ])  #   []+[]

arr = np.concatenate((arr1,arr2))
#arr = np.concatenate((arr1,arr2),axis=1) #if i did this it would have printed 
#->[ 1  2  3  4  5 11 12 13 14 15  6  7  8  9 10 16 17 18 19 20]
print(arr)

x = np.concatenate((arr))
print(x)

print("\n------------------------------}\n\033[0m")
"""
# Joining Arrays Using Stack Functions

# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We Concatenate two 1D arrays along second axis which would result in putting them one over other-> stacking.
# If axis is not explicitly passed it is taken as 0.
"""
print("\033[96m\n{------------------------------")

arr1= np.array( [1,2,3])
arr2= np.array( [4,5,6])

arrs=np.stack((arr1,arr2))         #--> arrv=np.vstack((arr1,arr2))
arrs1=np.stack((arr1,arr2),axis=1) #--> arrd=np.dstack((arr1,arr2))
arrh=np.hstack((arr1,arr2))        #--> arrc8=np.concatenate((arr1,arr2))
# above three are same as below 
arrv=np.vstack((arr1,arr2))
arrd=np.dstack((arr1,arr2))
arrc8=np.concatenate((arr1,arr2))

print("\n" + str(arrs) + "\n\n"+str(arrs1) + "\n\n" + str(arrh) + 
      "\n\n" + str(arrv) + "\n\n" + str(arrd) +
       "\n\n" + str(arrc8))

print("\n------------------------------}\n\033[0m")
"""
"""   **** Array join complete ****     """
