import math
import numpy as np
import matplotlib.pyplot as plt
import sympy

x = sympy.Symbol('x')

fx = x**3 - 4*(x**2) - 6*x + 5
dfx = fx.diff(x)

fx = sympy.lambdify(x,fx)
dfx = sympy.lambdify(x,dfx)

fig = plt.figure(figsize = (10,6))
x = np.arange(-2,6,0.1)
y_fx = fx(x)
y_dfx = dfx(x)

maxx = 0
minn = 0
i = -2

while i < 6 :
    x_fx = fx(i)
    x_dfx = dfx(i)
    #print(i, x_fx, x_dfx)
    if int(x_dfx) == 0 :
        if x_fx < 0 :
            maxx = i
        if x_fx > 0 :
            minn = i
    i += 0.1

plt.plot(x, y_fx, c = 'b',label = 'fx')
plt.plot(x, y_dfx, c = 'r',label = 'dfx')
plt.grid(True,which='both')
plt.axhline(y=0, color='k')
plt.legend()
plt.show()
print("maximum :",maxx)
print("minimun :",minn)