# * Multinomial distribution is generalization of binomial distribution.

# It describes outcomes of multinomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

# It has three parameters:

# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals[] - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.
#-------------------------------
# Note: 

# 1) Multinomial samples will NOT produce single value! They will produce one value for each pval.
# 2) As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as of multiple binomial distributions.
#-------------------------------

from numpy import random

print("\033[96m\n{------------------------------")
x=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])

print(x)

print("\n------------------------------}\n\033[0m")
#
