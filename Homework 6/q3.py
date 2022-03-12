import numpy as np

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def findDeternminant(m):
    return np.linalg.det(m)

def findminor(m):
    count = 0
    if len(m) == 2:
        return [[m[1][1], m[0][1]],
                [m[1][0], m[0][0]]]
    else :
        minormatrix = []
        for i in range(len(m)):
            minormatrixRow = []
            for j in range(len(m)):
                minor = getMatrixMinor(m,i,j)
                minormatrixRow.append(findDeternminant(minor))
                count += 1
            minormatrix.append(minormatrixRow)
        print(count)
        return minormatrix

def findcofactor(A) :
    for i in range (len(A)):
        for j in range (len(A[0])):
            if (i + j)%2 != 0 :
                A[i][j] = A[i][j] * -1
    return A

def findtranspose(matrix):
    return np.transpose(matrix)

def findInverse(m,det):
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = m[i][j]/det
    return m

def matrixtonumpy(A) :
    B = np.reshape(A,(-1,len(A[0])))
    return B

## Main ##
A = [[3,2,-4],[-2,5,2],[4,-2,1]]
print("Matrix")
print(matrixtonumpy(A))
print("Minor Matrix")
B = findminor(A)
print(matrixtonumpy(B))
print("CoFactor Matrix")
B = findcofactor(B)
print(matrixtonumpy(B))
print("Tranpose Matrix")
B = findtranspose(B)
print(matrixtonumpy(B))
print("Inverse Matrix")
print(findInverse(B,findDeternminant(A)))

print("Check Answer")
print(np.linalg.inv(A))
