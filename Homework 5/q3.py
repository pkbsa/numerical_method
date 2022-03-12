def f(x) :
    return x**3 - 6*(x**2) + 4*x + 12

def equal_interval_max(a,b,prev_xmax) :
    xm = (a+b)/2
    epsilon = 0.0005
    eps = 0.005
    xml = xm - (epsilon/2)
    xmr = xm + (epsilon/2)
    #print("initial interval = (%3.3f,%3.3f) prev_xmax = %3.3f" %(a,b,prev_xmax))
    if f(xml) > f(xmr) :
        xmax = xml
        b = xmr
    else :
        xmax = xmr
        a = xml
    epa = abs((xmax - prev_xmax)/xmax)*100
    #print("found xmax = %3.3f new interval = (%3.3f,%3.3f) epa = %3.4f" %(xmax,a,b,epa))
    if(epa < eps):
        return xmax
    else :
        return equal_interval_max(a,b,xmax)

def f(x) :
    return x**3 - 6*(x**2) + 4*x + 12

def equal_interval_min(a,b,prev_xmin) :
    xm = (a+b)/2
    epsilon = 0.0005
    eps = 0.005
    xml = xm - (epsilon/2)
    xmr = xm + (epsilon/2)
    #print("initial interval = (%3.3f,%3.3f) prev_xmax = %3.3f" %(a,b,prev_xmax))
    if f(xml) < f(xmr) :
        xmin = xml
        b = xmr
    else :
        xmin = xmr
        a = xml
    epa = abs((xmin - prev_xmin)/xmin)*100
    #print("found xmax = %3.3f new interval = (%3.3f,%3.3f) epa = %3.4f" %(xmax,a,b,epa))
    if(epa < eps):
        return xmin
    else :
        return equal_interval_min(a,b,xmin)
    
print("maximum = ",equal_interval_max(-2,6,0))
print("minimum = ",equal_interval_min(-2,6,0))

equal_interval_max(-2,6,0)