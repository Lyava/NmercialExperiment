import sympy as sy
import math


x = sy.symbols("x")


def FunValue(x0, f):
    result = f.subs(x, x0)
    return result


def Newton(f, x0, e1, e2, N):
    n = 1
    while n <= N:
        F = FunValue(x0,f)
        DF = FunValue(x0,sy.diff(f))
        if abs(F) < e1:
            return x0
        if abs(DF) <e2:
            return False
        x1 = x0 - F/DF
        Tol = abs(x1-x0)
        if Tol < e1:
            return x1
        n = n+1
        x0 = x1
    return False


if __name__ == '__main__':  # 当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。

        #x = sy.symbols("x")
        f = sy.cos(x) - x  # 公式
        x0 = math.pi/4
        e1 = 1e-6
        e2 = 1e-4
        N = 10
        ans = Newton(f, x0, e1, e2, N)
        print(ans)
        print(math.sin(math.pi/12))