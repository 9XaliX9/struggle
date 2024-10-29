# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb

print("\033[96m\n{------------------------------")

x = random.rayleigh(scale=2, size=(2, 3))
print(x)

# visualization

sb.displot(random.rayleigh(size=1000), kind="kde")
plot.show()

print("\n------------------------------}\n\033[0m")

# Similarity Between Rayleigh and Chi Square Distribution
# At unit stddev and 2 degrees of freedom rayleigh and chi square represent same distributions.
