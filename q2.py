import numpy as np
import math

def f(x):
    return math.e**x - 50

def bisectionrecursion(f,xl,xu,eps,xr_prev) :
    xr = (xl+xu) / 2
    epa = abs((xr-xr_prev)/xr) * 100
    print('updated to [%3.4f,%3.4f] xr = %3.4f epa = %3.4f' %(xl,xu,xr,epa))  
    if epa > eps :
        if f(xl) * f(xr) < 0 :
            return bisectionrecursion(f,xl,xr,eps,xr)
        else :
            return bisectionrecursion(f,xr,xu,eps,xr) 
    else :
        return xr

def findrange(x):
    n_intervals = len(x) - 1
    xl1 = []
    xu1 = []

    for k in range(0,n_intervals):
        #print('Interval %d: testing [%3.4f,%3.4f]' %(k,x[k],x[k+1]))
        xl = x[k]
        xu = x[k+1]
        if (f(xl) * f(xu) < 0):
            xr = (xl+xu)/2
            xl1.append(xl)
            xu1.append(xu)
            print('There is a root inside [%3.4f,%3.4f] interval.  The estimated root is %3.4f' %(x[k],x[k+1],xr))
    print("==================================================")
    return  xl1,xu1

## Main ##
x = np.arange(0,0.5,0.05)
xl_range,xu_range = findrange(x)

eps = 0.0005
allroot = []
for i in range (len(xl_range)) :
    myroot = bisectionrecursion(f,xl_range[i],xu_range[i],eps,0)
    allroot.append(myroot)
    print("root",i+1,"=",myroot)
    print("------------------")
print("all x's that makes f(x) = 0 are",allroot)