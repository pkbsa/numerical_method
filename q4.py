import numpy as np

def bisection (f,xl,xu) :
    eps = 0.005
    epa = 1
    xr_prev = 0
    xr = 0
    count = 0
    while epa > eps :
        xr = (xl+xu)/2
        if f(xl) * f(xr) < 0 :
            xu = xr
        else :
            xl = xr
        epa = abs((xr-xr_prev)/xr) * 100
        xr_prev = xr
        count+= 1
    return xr,count

def false_position(f,xl,xu) :
    epa = 0
    eps = 0.5 * pow(10,2-4)
    xr_prev = 0
    count = 0
    while epa > eps :
        xr = xu - (f(xu)*((xu-xl)/(f(xu)-f(xl))))
        if f(xl) * f(xr) < 0 :
            xu = xr
        else :
            xl = xr
        epa = abs((xr-xr_prev)/xr) * 100
        xr_prev = xr
        count += 1
    return xr,count

def findrange(x):
    n_intervals = len(x) - 1
    xl1 = []
    xu1 = []

    for k in range(0,n_intervals):
        xl = x[k]
        xu = x[k+1]
        if (f(xl) * f(xu) < 0):
            xr = (xl+xu)/2
            xl1.append(xl)
            xu1.append(xu)
            print('There is a root inside [%3.4f,%3.4f] interval.  The estimated root is %3.4f' %(x[k],x[k+1],xr))
    print("==================================================")
    return  xl1,xu1

def f(x) :
    return x**2 - 3*x - 1

x = np.arange(0,0.5,0.005)
xl_range,xu_range = findrange(x)

allrootbi = []
allrootfalse = []
countbi = 0
countfalse = 0

for i in range (len(xl_range)) :
     myroot,countbi = bisection(f,xl_range[i],xu_range[i])
     allrootbi.append(myroot)

for i in range (len(xl_range)) :
     myroot,countfalse = false_position(f,xl_range[i],xu_range[i])
     allrootfalse.append(myroot)
     
print("step :",countbi,"|bisection method :",allrootbi)
print("step :",countfalse,"|false position method :",allrootfalse)