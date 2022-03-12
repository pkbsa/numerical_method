def getMaxDP(A,n):
    if(n==1):
        return A[0]
    elif(n == 2):
        if(A[0] > A[1]) :
            return A[0]
        else :
            return A[1]
    else :
        mid = n//2
        A_left = A[:mid].copy()
        A_right = A[mid:].copy()
        max_left = getMaxDP(A_left, len(A_left))
        max_right = getMaxDP(A_right, len(A_right))
        if(max_left > max_right) :
            #print(max_left)
            return max_left
        else :
            #print(max_right)
            return max_right

A = [1,4,45,6,-50,10,2]
n = len(A)
maxA = getMaxDP(A,n)
print("Max A = ",maxA)