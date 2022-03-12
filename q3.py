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
    epa = 1
    eps = 0.005
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

def launch():
    x = np.arange(-2,6,0.5)
    xl_range,xu_range = findrange(x)

    allrootbi = []
    allrootfalse = []
    countbisec = []
    countbi = 0
    countfalsepo = []
    countfalse = 0
    
    for i in range (len(xl_range)) :
        myroot,countbi = bisection(f,xl_range[i],xu_range[i])
        allrootbi.append(myroot)
        countbisec.append(countbi)

    for i in range (len(xl_range)) :
        myroot,countfalse = false_position(f,xl_range[i],xu_range[i])
        allrootfalse.append(myroot)
        countfalsepo.append(countfalse)
        
    print("step :",countbisec,"|bisection method :",allrootbi)
    print("step :",countfalsepo,"|false position method :",allrootfalse)
    
def f(x) :
    return x**13 - 5*x - 9
launch()