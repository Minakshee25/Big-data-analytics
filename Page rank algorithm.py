import copy
import numpy as np
def teleport(beta,n):
    K=np.array([1/n for i in range(n)])
    L = np.array([[1/n for i in range(n)] for j in range(n)])
    for i in range(10):
        L = beta*M + (1-beta)*L
        Knew = np.dot(L,K)
        l = Knew-K
        if(any(abs(x) < 0.0001 for x in l)):
            break
        K=Knew
    return K

n = int(input("Enter number of pages = "))
c = int(input("Enter number of links = "))
w=[[0 for i in range(n)] for j in range(n)]

for i in range(c):
    a,b = map(int,input("Enter link = ").split())
    w[a][b] = 1

M = copy.deepcopy(w)

for i in range(n):
    x =1/sum(w[i])
    M[i] = [x if j==1 else 0 for j in M[i]]

M=np.array(M).T
K = np.array([[1/n] for k in range(n)])
for i in range(10):
    Knew = np.dot(M,K)
    l = Knew-K
    if(any(abs(x) < 0.0001 for x in l)):
        break
    K=Knew
print("Rank using simple page rank = ",K.T)
print("Rank using teleport 0.7 = ",teleport(0.7,n))
print("Rank using teleport 0.8 = ",teleport(0.8,n))
print("Rank using teleport 0.9 = ",teleport(0.9,n))
