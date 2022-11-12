import numpy as np
import sympy as sp

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
    return (kofaktor(matriks).transpose())