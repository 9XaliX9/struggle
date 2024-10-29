# Uniform Distribution

# Used to describe probability where every event has equal chances of occuring.

# i.e Generation of random numbers.
# It has three parameters:

# a    - lower bound - default 0 .0.
# b    - upper bound - default 1.0.
# size - The shape of the returned array.
"""
print("\033[96m\n{------------------------------")

from numpy import random
import seaborn as sb
import matplotlib.pyplot as plot

# x= random.uniform(size=(2,3)) #size(a,b)
# print(x)

sb.displot(random.uniform(size=1000),kind='kde')
plot.show()

print("\n------------------------------}\n\033[0m")
#       uniform distribution complete
"""