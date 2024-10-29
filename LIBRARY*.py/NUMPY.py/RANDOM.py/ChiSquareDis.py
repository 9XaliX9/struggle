#
# * Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).
# size - The shape of the returned array.

from numpy import random
import matplotlib.pyplot as plot
import seaborn as sb

print("\033[96m\n{------------------------------")

x = random.chisquare(df=2, size=(2, 3))
print(x)

# visualization

sb.displot(random.chisquare(df=1, size=1000), kind="kde")
plot.show()

print("\n------------------------------}\n\033[0m")
#