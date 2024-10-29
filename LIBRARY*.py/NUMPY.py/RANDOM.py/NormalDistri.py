# * Normal (Gaussian) Distribution

# The Normal Distribution is one of the most important distributions.
# Also called Gaussian Distribution after German mathematician Carl Gauss.
# It fits probability distribution of many events, eg. IQ Scores, Heartbeat etc.
# Use the random.normal() method to get a Normal Data Distribution.

# It has three parameters:
# loc   - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat graph distribution should be.
# size  - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print("\033[96m\n{------------------------------")

x = random.normal(size=(2, 3))
print(x)

print("###########################################")
y = random.normal(loc=1, scale=2, size=(2, 3))
print(y)

print("##### visualize ##### ")

sns.displot(random.normal(size=1000), kind="kde")
plt.show()

print("\n------------------------------}\n\033[0m")

#       uniform distribution complete
