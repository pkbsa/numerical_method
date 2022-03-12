#A program that can take a cube root of a number using Taylor Series expansion method.   Stop the iteration of the program using stopping criterion.  Test with the square root of the number 58.25.
def Find(x) :
    i=0
    while i < x :
        if i*i*i > x :
            break
        if i*i*i == x:
            print("Sqrt =",i)
            quit()
        i+=1
    return i*i*i

def fac(n) :
    factorial = 1
    if int(n) >= 1 :
        for i in range (n):
            factorial *= i+1
    return factorial

def FindRoot(x, c, input_sign) :
    prevroot = 1
    root = 0
    front = 1
    power = 1/3
    i=0
    
    while True :
        if i == 0 :
            fx = front * pow(x,power)
            front = 1/3
        else :
            fx = front * pow(x,power)
            front *= power
        power = power-1.0
            
        root += 1/fac(i) * fx * pow((c-x),i)
        
        stop = StoppingCriterion(root,prevroot,input_sign)
        print("times",i, "num =",root)
        prevroot = root
        i += 1
        
        if(stop == True):
            print("Sqrt = ",root)
            quit()

def StoppingCriterion(n,oldn,input_sign) :
    es = 0.5 * pow(10,2-input_sign) * 100
    ea = abs((n - oldn)/n)
    if ea<es :
        return True
    else :
        return False


## Main ##
c = float(input("Input a Number :"))
input_sign = int(input("input significant : "))

x = Find(c)
FindRoot(x,c,input_sign)


