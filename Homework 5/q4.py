import math
import matplotlib.pyplot as plt
import numpy as np

def f(x) :
    return x**3 - 6*(x**2) + 4*x + 12

def plotgraph() :
    xl = -6
    xu = 6
    interval = 0.1
    x = np.arange(xl,xu,interval)
    y = f(x)
    plt.grid(True)
    plt.plot(x,y)
    plt.show()

def golden_min(f,xl,xu) :
    eps = 0.005
    phi = (1+np.sqrt(5))/2
    d = (phi-1)*(xu-xl)
    x1 = xl + d
    x2 = xu - d
    #print("x1 = %4.5f\tf(x1) = %4.5f\tx2 %4.5f\tf(x2) = %4.5f" %(x1,f(x1),x2,f(x2)))
    xmin = xl
    if f(x1) < f(x2) :
        xl = x2
        xmin = x1
    else :
        xu =  x1
        xmin = x2
    #print("xmin = %4.4f" %(xmin))
    epa = (2-phi)*np.abs((xu-xl)/xmin)*100
    if(epa < eps):
        return xmin
    else :
        return golden_min(f,xl,xu)

def golden_max(f,xl,xu) :
    eps = 0.005
    phi = (1+np.sqrt(5))/2
    d = (phi-1)*(xu-xl)
    x1 = xl + d
    x2 = xu - d
    #print("x1 = %4.5f\tf(x1) = %4.5f\tx2 %4.5f\tf(x2) = %4.5f" %(x1,f(x1),x2,f(x2)))
    xmin = x1
    if f(x1) < f(x2) :
        xu = x1
        xmax = x2
    else :
        xl =  x2
        xmax = x1
    #print("xmax = %4.4f" %(xmax))
    epa = (2-phi)*np.abs((xu-xl)/xmax)*100
    if(epa < eps):
        return xmax
    else :
        return golden_max(f,xl,xu)
    
plotgraph()
xmin = golden_min(f,-2,6)
xmax = golden_max(f,-2,6)
print("minimum :",xmin)
print("maximum :",xmax)