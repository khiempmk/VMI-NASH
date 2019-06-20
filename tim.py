def cal(x,a,b,c):
    return a*x*x+b*x+c
def timmax(xmin,xmax,a,b,c):
    if (a<0):
        p = -b/(2*a)
        if (xmin<=p and p<=xmax):
            return p
    w1 = cal(xmin,a,b,c)
    w2 = cal(xmax,a,b,c)
    if (w1>w2):
        return xmin
    else:
        return xmax
    
    