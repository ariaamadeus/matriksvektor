from tools import np, inverse, I2x2,I3x3,det,adjoin

A = np.array([
        [3, 1],
        [-5, 2]])

B = np.array([
        [  1,-2, 3],
        [  5, 0, 2],
        [-12, 8,-9]])

print(np.linalg.inv(A))
print(inverse(A))
print(np.abs(np.dot(A,inverse(A)).round()))
print()
print(np.linalg.inv(B))
print(inverse(B))
print(np.absolute(np.dot(B,inverse(B)).round()))