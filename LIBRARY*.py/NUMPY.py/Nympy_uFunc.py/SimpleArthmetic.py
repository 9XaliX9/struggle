# Simple Arithmetic

# You could use arithmetic operators ( + - * / ^ %)directly between NumPy arrays,
# but this section discusses an extension of the same where we have functions
# that take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.


import numpy as np

print("\033[96m\n{------------------------------")


x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])
z = np.array([-1,-44,4,10,-500])


a = np.add(x, y)
s = np.subtract(x, y)
m = np.multiply(x, y)
d = np.round(np.divide(x, y), 2)
p = np.power(x, y)
r = np.mod(y, x)
q = np.divmod(y, x)
abs= np.absolute(z)


print (f"add:       {a}\n" 
       f"sub:       {s}\n"
       f"mult:      {m}\n"
       f"divide:    {d}\n"
       f"power:     {p}\n" 
       f"remainder: {r}\n"
       f"quotient:  {q}\n" 
       f"absolute:  {abs}"
)

print("\n------------------------------}\n\033[0m")

# Output:   ********** Simple Arithmetic complete***********