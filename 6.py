from tools import np, adjoin

A = np.array([
        [ 4, 0, 1],
        [-6,-1, 3],
        [-4, 2,-4]])

B = np.array([
        [-2, 4, 2],
        [-5, 1, 2],
        [ 7, 8,-9]])

print((np.dot(A,B)))
print(adjoin(np.dot(A,B)))
print(np.dot(adjoin(B),adjoin(A)))

