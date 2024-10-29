# Random numbers

# Random number does NOT mean different number every time.
# Random means something that can not be predicted logically.

# Random numbers generated through a generation algorithm are called pseudo random. >> working on this

import numpy as np
from numpy import random

"""
print("\033[96m\n{------------------------------")

x =random.randint(100) # generates an int
print(x)
print("\n")

a=np.random.seed(5)
b=np.random.rand(5) # random float size 5
c=np.random.randint(1,101,3) #(start, end, size)
random.randint

print(a)
print(b)
print(c)

print("\n------------------------------}\n\033[0m")
"""
"""
print("\033[96m\n{------------------------------")

x= np.random.randint(50,100,size=5)
print(x)

print("\n")
y=np.random.randint(100,size=(3,5)) #rows,colums -|
print(y)
print("\n")

z=np.random.rand(5)
print(np.round(z,4))

x=np.random.choice([5,3,2]) # allows to generate random value based on array of values.
print(x)

x=np.random.choice([2,4,6,8],size=(3,3))
print(x)

print("\n------------------------------}\n\033[0m")

                **** intro complete ****
"""
#