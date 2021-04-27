import sympy as sy
import math

h = 0.5
y = 1
k = h**3/4+h**2/2+h+1
i = 0
while i <= 10:
    print(k*y)
    y = k*y
    i += 1