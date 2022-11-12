from tools import np

hmehms = np.array([
    [12,20,25],
    [10,12,22],
                ])

harga = np.array([
    [3000],
    [5000],
    [2000]
                ])

print(np.dot(hmehms,harga))

'''
hmehms • harga = [12*3000 + 20*5000 + 25*2000]
                 [10*3000 + 12*5000 + 22*2000]

hmehms • harga = [186000]
                 [134000]

'''