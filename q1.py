import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - 6*x**2 + 4*x +12

def plotgraph (xl,xu):
    x = np.arange(xl,xu,0.5)
    y = f(x)
    z = [0 for i in range(0,len(x))]

    plt.plot(x,y,'b',x,z,'k')
    plt.show()

def function1(xl,xu,times) :
    xl1 = []
    xu1 = []
    root1 = []
    x = np.arange(xl,xu,times)
    n_intervals = len(x) - 1
    i = 0
    for k in range(0,n_intervals):
        print('Interval %d: testing [%3.4f,%3.4f]' %(k,x[k],x[k+1]))
        xl = x[k]
        xu = x[k+1]
        if (f(xl) * f(xu) < 0):
            xr = (xl+xu)/2
            print('\tThere is a root inside this interval.  The estimated root is %3.4f' %(xr))
            #print('[%3.4f]'%(xl))
            xl1.append(float('%3.4f'%(xl)))
            xu1.append(float('%3.4f'%(xu)))
            root1.append(float('%3.4f'%(xr)))
    return xl1,xu1,root1

def function2(xl,xu,times) :
    for i in range(len(xl)) :
        xl[i],xu[i],root[i] = function1(xl[i],xu[i],times)
        xl[i] = ArrangeNumber(xl[i])
        xu[i] = ArrangeNumber(xu[i])
        root[i] = ArrangeNumber(root[i])
    return xl,xu,root

def ArrangeNumber(string):
    tmp = str(string)
    tmp = tmp.replace('[','')
    tmp = tmp.replace(']','')
    return float(tmp)

## Main ##
plotgraph(-2,6)
xl,xu,root = function1(-2,6,0.5)
print("==========================================")
xl,xu,root = function2(xl,xu,0.05)
print("==========================================")
xl,xu,root = function2(xl,xu,0.005)
print("==========================================")
# xl,xu,root = function2(xl,xu,0.0005)
# print("==========================================")
print("all x's that makes f(x) = 0 are",root)