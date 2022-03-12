import numpy as np

A = np.array([[3,2,-4],[-2,5,2],[4,-2,1]])

print(A)

if len(A) != len(A[0]) :
    print("matrix A is not a skew-symmetric matrix")
    quit()
else :
    for i in range (len(A)):
        for j in range (len(A[i])):
            if i != j :
                if A[i][j] != - A[j][i] :
                    print (A[i][j],-A[j][i])
                    print("matrix A is not a skew-symmetric matrix")
                    quit()
    print("matrix A is a skew-symmetric matrix")   
