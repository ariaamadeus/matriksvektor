'''
      [3 + 4,-1 + 1, 2 + 2]   [7, 0, 4]
B+C = [4 + 0, 2 + 3, 5 + 2] = [4, 5, 7]
      [2 + 1, 0 - 2, 3 + 3]   [3,-2, 6]

          [1•7 +  2•4 + -3•3, 1•0 +  2•5 + -3•-2, 1•4 +  2•7 + -3•6]   [ 6, 16,  0]
A•(B+C) = [5•7 +  0•4 +  2•3, 5•0 +  0•5 +  2•-2, 5•4 +  0•7 +  2•6] = [41, -4, 32]
          [1•7 + -1•4 +  1•3, 1•0 + -1•5 +  1•-2, 1•4 + -1•7 +  1•6]   [ 6, -7,  3]

      [1 + 3, 2 - 1,-3 + 2]   [4, 1,-1]
A+B = [5 + 4, 0 + 2, 2 + 5] = [9, 2, 7]
      [1 + 2,-1 + 0, 1 + 3]   [3,-1, 4]
'''

import numpy as np

A = np.array([
        [1, 2,-3],
        [5, 0, 2],
        [1,-1, 1]])
B = np.array([
        [3,-1, 2],
        [4, 2, 5],
        [2, 0, 3]])
C = np.array([
        [4, 1, 2],
        [0, 3, 2],
        [1,-2, 3]])
firstState = np.dot(A,B+C)
secondState = np.dot(A,B) + np.dot(A,C)
print(firstState)
print((firstState==secondState).all())
firstState = np.dot(A+B,C)
secondState = np.dot(A,C) + np.dot(B,C)
print((firstState==secondState).all())
