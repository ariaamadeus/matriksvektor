#https://stackoverflow.com/questions/31547657/how-can-i-solve-system-of-linear-equations-in-sympy

from tools import np, sp

a, b, c, d = sp.symbols('a b c d')

A = sp.Matrix([
        [2-a,-2-b],
        [3+c, 5-d]])
B = sp.Matrix([
        [5, 7],
        [0,-2]])
C = np.array([
        [13, 22],
        [-9, 12]])

D = np.array([
        [0, 5],
        [2, 7]])

A3B2C = A+3*B-2*C
'''
3B = 15 21
      0 -6

2C = 26 44
    -18 24

A+3B-2C = [2+15-26-a = -9-a, -2+21-44-b = -25-b]
          [3+ 0+18+c = 21+c,  5- 6+24-d = -25-d]
'''


print(A3B2C)
print(sp.solve(A3B2C-D, (a, b, c, d))) #A+3B-2C = D -> A+3B-2C-D = 0

'''
A = [-9-a = 0, -25-b = 5]
    [21+c = 2, -25-d = 7]

a = -9, b = -30, c = -19, d = -32
'''