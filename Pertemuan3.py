from tools import np, adjoin, inverse

A = np.array([
        [8, 1],
        [7, 6]])

E = np.array([
        [ 6, 1, 3],
        [-1, 1, 2],
        [ 4, 1, 3]])

print(adjoin(A))
print(adjoin(E))

A = np.array([
        [ 2, 4, 6],
        [ 5, 7, 2],
        [-8,-1,-3]])
        
print(inverse(A))