def FirstCurrentValue(n) :
    n = int(n)
    for i in range(n) :
        if i*i < n :
            current_compute = i
        elif i*i == n:
            print("The square root of",n ,"is",i)
            quit()
    return current_compute

def Heron(input_sign,current_compute) :
    es = 0.5 * pow(10,2-input_sign)
    ea = 1
    previous_compute = 0
    while es < ea :
        current_compute = float(0.5*(current_compute+n/current_compute))
        ea = abs((current_compute - previous_compute)/current_compute)
        previous_compute = current_compute
    return current_compute

## Main ##
n = float(input("input number to find a square root (Using Heron's Method) : "))
input_sign = int(input("input significant : "))

current_compute = FirstCurrentValue(n)
current_compute = Heron(input_sign,current_compute)

print("=========================================")
print("The square root of",n ,"is",current_compute)
print("=========================================")