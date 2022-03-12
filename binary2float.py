#convert a 32-bit binary string in IEEE-754 format into a decimal floating point number (base-10) and test with the floating point number (base-10) 58.5625
#Calculate Base2-Binary To Decimal 
def BinaryToDecimal(n) :
    decimal = 0
    n = n[::-1]
    for i in range (len(n)):
        decimal += int(n[i]) * 2**(i)
    return decimal

#Calculate Base2-Binary To Decimal (of Mantissa)
def BinaryToDecimalMantissa(n) :
    decimal = 0
    for i in range (len(n)):
        decimal += int(n[i]) * 2**((-i-1))
        #print(decimal)
    return decimal

## Main ##
input_binary = str(input("input a 32-bit binary string in IEEE-754 format to convert it into decimal floating point number (base-10):"))
input_binary = input_binary.replace(" ","")

s = input_binary[0:1]
s = int(s)

e = input_binary[1:9]
e = str(int(e))
e = BinaryToDecimal(e) - 127

f = input_binary[9:31]
f = BinaryToDecimalMantissa(f)

decimal_final = pow(-1,s) * (1+f) 

print("==================================================")
print("s :",s)
print("e :",e)
print("f :",f)
print("==================================================")
print("floating point number (base-10):",decimal_final,"x 2^",e)
print("                               :",decimal_final*pow(2,e))
print("==================================================")
