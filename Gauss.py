import numpy as np

def Gauss(A,b):
    n = A.shape(0)  #阶数
    for k in range(n - 1):
        maxAk = 0


        for p in range(k,n):  #p遍历得到最大主元
            if abs(A[p,k]) > maxAk:
                maxAk = abs(A[p,k])
                p_value = p           #p_value表示所在行


        if maxAk == 0:
            return False
        elif p_value != k:
            A[[k,p_value],:] = A[[p_value,k],:]#交换
            b[p_value],b[k] = b[k],b[p_value]


        for i in range(k+1, n):
            temp = A[i, k]/A[k, k]  #系数
            b[i] = b[i] - b[k]*temp
            for j in range(k+1, n):
                A[i, j] = A[i, j] - A[k, j]*temp

    if A[n][n] == 0: return False

    x = np.zeros(n-1)
    x[n-1] = b[n-1]/A[n-1][n-1]
    for k in range(n-2,0):
        axsum = 0
        for j in range(k+1,n-1):
            axsum += A[k][j]*x[j]
        x[k] = (b[k] - axsum)/A[k][k]

if __name__ == '__main__':
    A = 1
