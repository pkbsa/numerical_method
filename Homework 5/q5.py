import math
import matplotlib.pyplot as plt
import numpy as np

def f(x) :
    return np.e**(x) - x**3

def plotgraph() :
    xl = -6
    xu = 6
    interval = 0.1
    x = np.arange(xl,xu,interval)
    y = f(x)
    plt.grid(True)
    plt.plot(x,y)
    plt.show()

def opt_parabola(x1,x2,x3):
    a1 = (x2-x1)*(x2-x1)*(f(x2)-f(x3))
    a2 = (x2-x3)*(x2-x3)*(f(x2)-f(x1))
    b1 = (x2-x1)*(f(x2)-f(x3))
    b2 = (x2-x3)*(f(x2)-f(x1))
    c = (a1-a2)/(b1-b2)
    x4 = x2 - (0.5*c)
    return float(x4)

def min_parabolic(x1,x2,x3,eps):
    xopt_prev = x2
    x4 = opt_parabola(x1,x2,x3)
    print('x1 = %4.4f\tx2 = %4.4f\tx3 = %4.4f\tx4 = %4.4f' %(x1,x2,x3,x4))
    print('f(x1) = %4.4f\tf(x2) = %4.4f\tf(x3) = %4.4f\tf(x4) = %4.4f' %(f(x1),f(x2),f(x3),f(x4)))
    if (x4 > x2):
        if (f(x4) < f(x2)):
            xmin = x4
            x1 = x2
            x2 = x4
        else: 
            xmin = x2
            x3 = x4
    else: 
        if (f(x4) < f(x2)):
            xmin = x4
            x3 = x2
            x2 = x4
        else: 
            xmin = x2
            x1 = x4
            x4 = x2 
    xopt = xmin
    epa = np.abs((xopt-xopt_prev)/xopt)*100
    print('xopt = %4.4f\tepa = %4.4f' %(xopt,epa), end = ' ')
    if (epa < eps):
        return xopt
    else:
        return min_parabolic(x1,x2,x3,eps)
    
def max_parabolic(x1,x2,x3,eps):
    xopt_prev = x2
    x4 = opt_parabola(x1,x2,x3)
    print('x1 = %4.4f\tx2 = %4.4f\tx3 = %4.4f\tx4 = %4.4f' %(x1,x2,x3,x4))
    print('f(x1) = %4.4f\tf(x2) = %4.4f\tf(x3) = %4.4f\tf(x4) = %4.4f' %(f(x1),f(x2),f(x3),f(x4)))
    if (x4 > x2):
        if (f(x4) > f(x2)):
            xmax = x4
            x1 = x2
            x2 = x4
        else: 
            xmax = x2
            x3 = x4
    else: 
        if (f(x4) > f(x2)):
            xmax = x4
            x3 = x2
            x2 = x4
        else: 
            xmax = x4
            x1 = x4
    xopt = xmax
    epa = np.abs((xopt-xopt_prev)/xopt)*100
    print('xopt = %4.4f\tepa = %4.4f' %(xopt,epa), end = ' ')
    if (epa < eps):
        return xopt
    else:
        return max_parabolic(x1,x2,x3,eps)

plotgraph()
x1 = 2
x2 = 3
x3 = 5
eps = 0.005
xmin = min_parabolic(x1,x2,x3,eps)
#xmax = max_parabolic(x1,x2,x3,eps)

        