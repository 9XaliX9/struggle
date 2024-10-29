#Binomial distribution

# Binomial Distribution is a Discrete Distribution.
# It describes outcome of binary scenarios,ie toss of a coin, 
# it will either be head or tails.

# It has three parameters:

# n    - number of trials.
# p    - probability of occurence of each trial (toss of a coin 0.5 each). means 50% chance~ .5
# size - The shape of the returned array.

from numpy import random
import seaborn as sb
import matplotlib.pyplot as plot
"""
print("\033[96m\n{------------------------------")

# x=random.binomial(n=10,p=0.5,size=10)
# print(x,'\n')

#--------------------------------------
# sb.displot(random.binomial(n=10,p=.5,size=1000),kind='hist')
# plot.show()

#======================================
#diff between normal vs binomial

sb.displot(random.normal(loc=50, scale=5, size=1000), kind='kde', label='normal')
sb.displot(random.binomial(n=100, p=0.5, size=1000), kind='kde', label='binomial')

plot.show()

print("\n------------------------------}\n\033[0m")
#           *** Binomial complete ***
"""
#
