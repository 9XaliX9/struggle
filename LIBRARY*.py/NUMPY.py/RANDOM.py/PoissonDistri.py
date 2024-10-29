# Poisson Distribution

from numpy import random
import seaborn as sb
import matplotlib.pyplot as plot

""""
print("\033[96m\n{------------------------------")

# sb.displot(random.poisson(lam=3,size=1000),)
# plot.show()

#--------------------------------------------------

# Difference Between Normal and Poisson Distribution
# Normal distribution is continuous whereas poisson is discrete.

# But we can see that similar to binomial for a large enough poisson distribution 
#it will become similar to normal distribution with certain std dev and mean.

sb.displot(random.normal(loc=50,scale=7,size=1000),kind='kde')
sb.displot(random.poisson(lam=50,size=1000),kind='kde')

plot.show()
#-----------------------------------------------------

# Difference Between Binomial and Poisson Distribution
# Binomial distribution only has two possible outcomes, 
#whereas poisson distribution can have unlimited possible outcomes.

# But for very large n and near-zero p binomial distribution is near 
#identical to poisson distribution such that n * p is nearly equal to lam.

sb.displot(random.binomial(n=1000, p=0.01, size=1000), kind='kde')
sb.displot(random.poisson(lam=10, size=1000),kind='kde')

plot.show()

print("\n------------------------------}\n\033[0m")
"""