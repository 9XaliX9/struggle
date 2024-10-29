# Logistic Distribution (very important)

#:is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:

# loc   - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size  - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb

"""
print("\033[96m\n{------------------------------")

# x= random.logistic(loc=1,scale=2, size=(2,3))
# print(x)

sb.displot(random.logistic(size=1000),kind='kde')
plot.show()

print("\n------------------------------}\n\033[0m")
"""
#=============================================================
# Difference Between Logistic and Normal Distribution

# Both distributions are near identical, but logistic distribution 
#represents more possibility of occurrence of an event further away from mean.

# For higher value of scale (standard deviation) normal and 
#logistic distributions are near identical apart from peak.
#=============================================================
"""
print("\033[96m\n{------------------------------")

sb.displot(random.normal(scale=2, size=1000),kind='kde')
sb.displot(random.logistic(size=1000),kind='kde' )

plot.show()

print("\n------------------------------}\n\033[0m")
# logistic complete
"""
