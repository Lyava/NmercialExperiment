import sympy as sy
import numpy as np

def LagangeInterpolation(dPs,n,x):  #dPs为离散的点，N为点的个数
    y = 0
    k = 0
    N = n+1
    while(k<=n):
        l = 1
        for j in range(N):
            if j == k: j++
            l = l*(x - dPs[j,0])/(dPs[k,0]-dPs[j,0]
        y = y+l*dPs[k,1]
        k+=1
    return y


    
if _name_ == '__main__':
    x = sy.Symbol('x')
    
    f1 = 1/(1+x**2)
    xmi1 = -5
    xma1 = 5
    n = [5,10,20]

    _dps = np.zeros(n[0]+1,2)
    h = (xma1 - xmin1)/n[0]
    for k in range(n[0]+1):
        _dps[k,0] = xmi1+k*h
        _dps[k,1] = f1.evalf(subs = {x:dps[k,0]})
    x = [0.75,1.75,2.75,3.75,4.75]    
    print(LagangeInterpolation(_dps,n[0],x[0])
    print(LagangeInterpolation(_dps,n[0],x[1])

