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

def fwd_gauss_recursive(Ab):
    [nr,nc] = Ab.shape
    print("nr = ",nr)
    if nc == nr +1:
        print("Error")
    else:
        if(nr ==1) :
            GEM = Ab
        else :
            for r in range(1,nr):
                row_factor = Ab[r,0]/Ab[0,0]
                Ab[r,:] = Ab[r,:] - row_factor * Ab[0,:]
            GEM = Ab
            
            GEM_next_input = GEM[1:nr,1:nc]
            GEM_next_output = fwd_gauss_recursive(GEM_next_input)
    print(GEM)
    return GEM

A = np.array([[4.0,-2.0,1.0],[1.0,1.0,1.0],[9.0,3.0,1.0]])
#A = np.array([[3.0,0.0,2.0],[2.0,0.0,-2.0],[0.0,1.0,1.0]])
b = findB(A)

print("Matrix")
print(A)
Ab = np.append(A,b,axis=1)
print(Ab)
GAb = fwd_gauss_recursive(Ab)