from numpy import *
from numpy.random import *

def S(A):
    s = 0
    for i in range(m):
        for j in range(n):
            s += A[i,j]*A[i,(j+1) % (n)] + A[i,j]*A[(i+1) % (m),j]
    return -s

m,n = 20, 20
A = 2.*randint(0,2,size=(m,n))-1.
A = ones((m,n))
N = 10000
beta = 1

avg = [0,0,0,0]
E = S(A)
M = sum(A)
for k in range(N):
    for i in range(m):
        for j in range(n):
            u = randint(0,m)
            v = randint(0,n)
            dE = 2*(A[u,v]*A[u,(v+1) % n] + A[u,v]*A[(u+1) % m,v] + \
                   A[u,v]*A[u,abs((v-1) % n)] + A[u,v]*A[abs((u-1) % m),v])
            if exp( -beta*dE ) > rand():
                A[u,v] = -A[u,v]
                E += dE
                M += 2*A[u,v]
    avg[0] += E
    avg[1] += E**2
    avg[2] += abs(M)
    avg[3] += M**2

print "Energy:", avg[0]/N
print "Magn:",   avg[2]/N
print "Cv:",     avg[1]/N - (avg[0]/N)**2
print "X:",      avg[3]/N - (avg[2]/N)**2

