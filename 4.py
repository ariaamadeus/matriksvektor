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
adj A = [ d,-b]
        [-c, a]

adj A = [0 -1]
        [7 12]

adj B = [-2, 4, 2]
        [-5, 1, 2]
        [ 7, 8,-9]

adj B = transpose kof B
kof B = [B11 B12 B13]
        [B21 B22 B23]
        [B31 B32 B33]

B11 = +( 1*-9 -  8*2)
B12 = -(-5*-9 -  7*2)
B13 = +(-5* 8 -  7*1)
B21 = -( 4*-9 -  8*2)
B22 = +(-2*-9 -  7*2)
B23 = -(-2* 8 -  7*4)
B31 = +( 4* 2 -  1*2)
B32 = -(-2* 2 - -5*2)
B33 = +(-2* 1 - -5*4)

kof B = [-25,-31,-47]
        [ 52,  4, 44]
        [  6, -6, 18]

adj B = transpose kof B

adj B = [-25, 52,  6]                                                                                                        
        [-31,  4, -6]                                                                                                        
        [-47, 44, 18]

'''

print(adjoin(A))
print(adjoin(B))