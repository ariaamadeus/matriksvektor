from kofaktor1 import np, det

A = np.array([
    [ 1, 2, 2, 1],
    [ 1, 2, 4, 2],
    [ 2, 7, 5, 2],
    [-1, 4,-6, 3]
            ])

'''
R -> baris

R2 = R2-R1
R3 = R3-R1
R4 = R4+R1

  1  2  2  1
  0  0  2  1
  0  3  1  0
  0  6 -4  4

swap

  1  2  2  1
  0  3  1  0
- 0  0  2  1
  0  6 -4  4

R4 = R4 - 2R2
R4 = R4 - 3R3

  1	 2	2  1	
  0	 3	1  0	
- 0	 0	2  1	
  0	 0  0  7
'''

B = np.array([
    [1, 2, 2, 1],
    [0, 3, 1, 0],
    [0, 0, 2, 1],	
    [0, 0, 0, 7]
            ])

print(det(A))
print(-det(B))
