import numpy as np

Ai = [[1,2,3,4,5,6],[2,6,9,12,15,18],[3,10,18,24,30,36],[4,14,27,40,50,60],[5,18,36,56,75,90],[6,22,45,72,100,126]]

bi=[-12,20,3]

def ret(U,b):
  n=len(b)
  x=np.zeros(n)
  x[n-1]=b[n-1]/U[n-1][n-1]

  for i in range(n-2,-1,-1):
    s=b[i]
    for j in range(i,n):
      s=s-(U[i][j]*x[j])
    x[i]=s/U[i][i]
  return x

x=ret(U,y)
print("%s^T" % x)