#2. convert a floating point number (base-10) into IEEE-754 and test with the floating point number (base-10) 58.5625.
#Siranut A. 6388117
import math

#Find Sign of IEEE754
def FindSign(n) :
    if n > 0 :
        return '0'
    else :
        return '1'
    
def IntToBinary(n):
    n = int(n)
    str1 = ''
    i = 0
    
    if n == 0 :
        return str1
    
    binaryNum = [0] * int(n)

    while(n > 0):
        binaryNum[i] = n%2
        n = int(n/2)
        i += 1
        
    for j in range(i-1,-1,-1):
        str1 += str(int(binaryNum[j]))
        
    return str1

def FloatingPointToBinary(n) :
    str1 = ''
    decimal = n - math.floor(n)
    
    while True:
        decimal = decimal*2
        if decimal>=1.00 :
            str1 += '1'
            decimal = decimal-1
        else :
            str1 += '0'
        if decimal == 0.00 :
            break    
    return str1

def MantissaLow(n):
    count = 0
    if n>= 0.5 :
        return count , n
    while True:
        n = n*2
        count += 1
        if n >= 0.5 and n<=1 :
            return count , n

def ArrangeNumber(string, mantissa):
    if mantissa == True:
        while len(string)<23:
            string += '0'
    return ' '.join(string[i:i+4] for i in range(0,len(string),4))[0:28]

## Main ##
n = float(input("input a floating point number to convert it into IEEE-754(32-bit binary string) :"))

sign = FindSign(n)

n = abs(n)
# 58.625 -> 58 , 0.625
mantissa = IntToBinary(n) + FloatingPointToBinary(n)
mantissa = mantissa[1:]

if n >= 1 :
    expo = IntToBinary(n)
    expo = 127 + len(expo)-1
    expo = IntToBinary(expo)
else :
    times,mantis = MantissaLow(n)
    expo = 127 - times - 1
    expo = "0" + IntToBinary(expo)
    
    if n < 0.5 :
        mantissa = FloatingPointToBinary(mantis)
        mantissa = mantissa[1:]

expo = ArrangeNumber(expo,False)
mantissa = ArrangeNumber(mantissa,True)

ieee754 = sign + expo + mantissa
ieee754 = ieee754.replace(" ","")
ieee754 = ' '.join(ieee754[i:i+4] for i in range(0,len(ieee754),4))

print("==================================================")
print("s = ", sign)
print("e = ", expo)
print("f = ", mantissa)
print("IEEE-754 =",ieee754)
print("==================================================")
