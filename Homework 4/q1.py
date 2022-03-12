import math
import matplotlib.pyplot as plt
import numpy as np

def f(x) :
    return x**4 - (2*x) - 10

def g(x) :
    return np.sqrt(10/(x**2 - (2/x)))

def plotgraph (xl,xu):
    x = np.arange(xl,xu,0.05)
    y = f(x)
    z = [0 for i in range(0,len(x))]

    plt.plot(x,y,'b',x,z,'k')
    plt.show()
    
def fixed_point(g,x0) :
    xr_prev = x0
    epa = 100
    eps = 0.5
    while(epa > eps) :
        xr = g(xr_prev)
        epa = abs((xr-xr_prev)/xr) * 100
        xr_prev = xr
        print("xr = ",xr,"epa =",epa)
    return(xr)

plotgraph(-6,6)
print(fixed_point(g,1))
         