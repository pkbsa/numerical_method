import numpy as np
import math
import sympy

x = sympy.Symbol('x')
f = x**4 - 2*x - 10
df = f.diff(x)
f = sympy.lambdify(x,f)
df = sympy.lambdify(x,df)

x = sympy.Symbol('x')
f1 = math.e**x + sympy.sqrt(x) - 2*x - 5
df1 = f1.diff(x)
f1 = sympy.lambdify(x,f1)
df1 = sympy.lambdify(x,df1)

def newtonraphson(f,df,x0) :
    xr_prev = x0
    epa = 100
    eps = 0.005
    i = 0
    while(epa > eps) :
        i = i+1
        xr = xr_prev - (f(xr_prev)/df(xr_prev))
        epa = abs((xr-xr_prev)/xr) * 100
        xr_prev = xr
        print(i, "xr",xr,"epa",epa)
    return xr
        
x0 = 1
xr = newtonraphson(f,df,x0)
print("==============================")
print("x = ",xr)
print("==============================")
xr1 = newtonraphson(f1,df1,3)
print("==============================")
print("x = ",xr1)

    