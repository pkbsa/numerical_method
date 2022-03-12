def StoppingCriterion(n,oldn,input_sign) :
    es = 0.5 * pow(10,2-input_sign)
    ea = abs((n - oldn)/n) * 100
    if ea<es :
        return True
    else :
        return False
    
def fac(n) :
    factorial = 1
    if int(n) >= 1 :
        for i in range (n):
            factorial *= i+1
    return factorial    
    
def finde() :
    x = 1
    e = 1
    for i in range (100) :
        e += pow(x,i+1)/fac(i+1)
    #print(e)
    return e

def Findln1(x) :
    n = 1
    e = finde()
    num = x
    while True :
        num = x/pow(e,n)
        #print(num)
        if num <= 2 :
            #print(num,n)
            return num,n
        n += 1

def Findln2(num,input_sign) :
    n = 1
    prev = 0
    current = 0
    
    while True :
        curr = pow(-1,n-1) * pow(num,n)/n
        current += curr
        stop = StoppingCriterion(current,prev,input_sign)
        prev = current
        #print("tnum :",curr)
        #print("sumnum :",current)
        n += 1
        
        if(stop == True):
            break
        
    return current

## Main ## 
input_num = float(input("input number : "))
input_sign = int(input("input significant : "))

num,times = Findln1(input_num)
#print(num-1)
ans = Findln2(num-1,input_sign)

ans = ans + times
print("natural log :",ans)

    