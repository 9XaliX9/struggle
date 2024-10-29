# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term.
# E.g.the 5th most common word in English occurs nearly 1/5 times as often as most common word.

# It has two parameters:

# a - distribution parameter.
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb

print("\033[96m\n{------------------------------")

x = random.zipf(a=2, size=1000)
print(x)

# visualization

sb.displot(x[x < 10], kind="hist")
plot.show()

print("\n------------------------------}\n\033[0m")
