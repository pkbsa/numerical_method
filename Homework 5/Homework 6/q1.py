import numpy as np

A = np.array([[1,0],[0,1]])

print(A)

if len(A) != len(A[0]) :
    print("matrix A is not diagonal matrix")
    quit()
else :
    for i in range (len(A)):
        for j in range (len(A[i])):
            if i != j :
                if A[i][j] != 0 :
                    print("matrix A is not diagonal matrix")
                    quit()
    print("matrix A is a diagonal matrix")   