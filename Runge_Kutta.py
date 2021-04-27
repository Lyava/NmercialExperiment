import sympy as sy

def Runge_Kutta(a,b,aph,N):
    x0 = a
    y0 = aph
    h = (b-a)/N
    n = 1
    while n<=N:
        
