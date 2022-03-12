import numpy as np

def matrixtonumpy(A) :
    B = np.reshape(A,(-1,len(A[0])))
    return B

def findB(A) :
    B = []
    for i in range (len(A)):
        BRow = []
        for j in range (len(A)):
            if i == j :
                BRow.append(1)
            else :
                BRow.append(0)
        B.append(BRow)
    return matrixtonumpy(B)

def fwd_gauss(Ab) :
    MAb = Ab.copy()
    [nr_Ab,nc_Ab] = Ab.shape
    for r in range (0,nr_Ab) :
        MAb = checkswap(MAb,r)
        k = MAb[r,r]
        #print(MAb)
        MAb[r,:] = (1/k) * MAb[r,:]
        
        if (r != nr_Ab-1) :
            for i in range(r+1,nr_Ab) :
                #print(MAb[i,r])
                if i == r or MAb[i][r] == 0: continue
                row_factor = 1/MAb[i,r]
                MAb[i,:] = (row_factor) * MAb[i,:]
                MAb[i,:] = MAb[i,:] - MAb[r,:]
    return MAb

def back_gauss(Gab):
    M = Gab
    [nr,nc] = M.shape
    M[nr-1,:] = M[nr-1,:]/M[nr-1,nr-1]
    print(M[nr-1,:])
    for r in reversed(range (nr-1)) :
        for c in range(r+1,nr) :
            M[r,:] = M[r,:] - M[r,c] * M[c,:]
        M[r,:] = M[r,:]/M[r,r]
    return M

def getinverse(A,size):
    B = []
    for i in range (len(A)) :
        BRow = []
        for j in range(len(A[0])) :
            if(j >= size) :
                BRow.append(A[i][j])
        B.append(BRow)
    return matrixtonumpy(B)

def checkswap(a,k) :
    n = len(a)
    for i in range(k+1, n):
        if abs(a[i][k]) > abs(a[k][k]):
            for j in range(k, 2*n):
                a[k][j], a[i][j] = a[i][j], a[k][j] #swapping of rows
            break
    return a
    
## Main ## 
#A = np.array([[4.0,-2.0,1.0],[1.0,1.0,1.0],[9.0,3.0,1.0]])
A = np.array([[3.0,0.0,2.0],[2.0,0.0,-2.0],[0.0,1.0,1.0]])
b = findB(A)

print("Matrix")
print(A)
Ab = np.append(A,b,axis=1)
print("[A|I]")
print(Ab)

print("After Foward Elimination")
GAb = fwd_gauss(Ab)
print(GAb)

print("After Back Substitution")
GAb = back_gauss(GAb)
print(GAb)

print("Inverse Matrix")
GAb = getinverse(GAb,len(A))
print(GAb)

print("Check Answer")
print(np.linalg.inv(A))              
