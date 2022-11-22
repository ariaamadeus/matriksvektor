import numpy as np
import sympy as sp

I2x2 = np.array([
        [1, 0],
        [0, 1]])

I3x3 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])

def det(matriks):
    return round(np.linalg.det(matriks))

#https://www.geeksforgeeks.org/how-to-find-cofactor-of-a-matrix-using-numpy/
def kofaktor(matriks):
    try:
        determinan = det(matriks)
        if(determinan!=0):
            kofaktor = None
            kofaktor = np.linalg.inv(matriks).T * determinan
            return kofaktor
        else:
            raise Exception("matriks singular")
    except Exception as e:
        print("could not find cofactor matrix due to",e)

def adjoin(matriks):
    return (kofaktor(matriks).transpose()).round()

def inverse(matriks):
    return (1/det(matriks))*adjoin(matriks)