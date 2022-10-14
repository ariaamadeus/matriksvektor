#1
'''
det A = 8*6 - 7*1 = 41
'''
#2
'''
det B = 4*2 - 0*-1 = 8
'''
#3
'''
det C = 6*(3*-7 - -6*5) - 11*(8*-7 - 5*-10) + 4*(8*-6 - -10*3) = 48
'''
#4
'''
det E = 6*(1*3 - 1*2) - 1*(-1*3 - 2*4) + 3*(-1*1 - 4*1) = 2
'''
#5
'''
det D = 1*(0*4 - 2*1) - 5*(-1*4 - 1*3) + 2*(-1*2 - 3*0) = 29
'''
import numpy as np

A = np.array([
    [8, 1],
    [7, 6]
            ])

B = np.array([
    [4,-1],
    [0, 2]
            ])

C = np.array([
    [  6,11, 4],
    [  8, 3, 5],
    [-10,-6,-7],
            ])

E = np.array([
    [ 6, 1, 3],
    [-1, 1, 2],
    [ 4, 1, 3],
            ])

D = np.array([
    [ 1, 5, 2],
    [-1, 0, 1],
    [ 3, 2, 4],
            ])

def det(matriks):
    return round(np.linalg.det(matriks))

if __name__ == "__main__":
    print('1:',det(A))
    print('2:',det(B))
    print('3:',det(C))
    print('4:',det(E))
    print('5:',det(D))