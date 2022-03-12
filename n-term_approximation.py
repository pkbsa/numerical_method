#Find the n-term approximation of a function (T_n(x)) of sin(x) where n = 2, 4, 6, 8, 10. 
import numpy as np
import matplotlib.pyplot as plt

def fac(n) :
    factorial = 1
    if int(n) >= 1 :
        for i in range (n):
            factorial *= i+1
    return factorial

def plotgraph() :
    x = np.arange(-4,4,0.01)
    
    y1 = x - x**3/fac(3)
    y2 = x - x**3/fac(3) + x**5/fac(5)
    y3 = x - x**3/fac(3) + x**5/fac(5) - x**7/fac(7) 
    y4 = np.sin(x)
    
    plt.plot(x,y1,'black')
    plt.plot(x,y2,'orange')
    plt.plot(x,y3,'cyan')
    plt.plot(x,y4,'purple')
    
    plt.show()
    
## Main ##
input_num = float(input("input first number of sin(x) : "))

n = 0
current = 0.00
for i in range (11) :
    power = n+1
    current += (pow(input_num,power)/fac(power)) * pow(-1,i)
    #print("current :",curr, "x :",pow(input_num,power),"power :",power,"fac",fac(power))
    if i%2 == 0 and i != 0:
        print("T",i,"(",input_num,") :",current)
    n += 2
    
plotgraph()
