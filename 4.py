# from torch import adjoint, from_numpy
from tools import adjoin, np, kofaktor
A = np.array([
        [12, 1],
        [-7, 0]])

B = np.array([
        [-2, 4, 2],
        [-5, 1, 2],
        [ 7, 8,-9]])

'''
adj A = [0 -7] (cukup jelas)
        [1 12]

adj B = [-2, 4, 2]
        [-5, 1, 2]
        [ 7, 8,-9]

adj B = transpose kof B
kof B = [B11 B12 B13]
        [B21 B22 B23]
        [B31 B32 B33]

B11 = +(1*-9 - 8*2)
B12 = -(-5*-9 - 7*2)
B13 = +(-5*8 - 7*1)
B21 = -(*-9 - 8*2)
B22 = +(1*-9 - 8*2)
B23 = -(1*-9 - 8*2)
B31 = +(1*-9 - 8*2)
B32 = -(1*-9 - 8*2)
B33 = +(1*-9 - 8*2)


adj B = [-2, 4, 2]
        [-5, 1, 2]
        [ 7, 8,-9]
  

'''

print(adjoin(A))
print(adjoin(B))