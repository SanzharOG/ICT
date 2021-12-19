from sympy import *
x, z = symbols('x z')
print(diff(sin(x)+0.5*z, z))