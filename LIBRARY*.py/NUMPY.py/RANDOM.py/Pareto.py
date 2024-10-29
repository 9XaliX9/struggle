# #Pareto Distribution
# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# It has two parameter:

# a - shape parameter.
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb

print("\033[96m\n{------------------------------")

x = random.pareto(a=2, size=(2, 3))
print(x)

# visualization

sb.displot(random.pareto(a=2, size=1000), kde=True)
plot.show()

print("\n------------------------------}\n\033[0m")
#