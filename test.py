from numpy import *
from numpy.random import *

def S(M):
    s = 0
    for i in range(m):
        for j in range(n):
            s += M[i,j]*M[i,(j+1) % (n)] + M[i,j]*M[(i+1) % (m),j]
    return -s

m,n = 2,2
M = 2.*randint(0,2,size=(m,n))-1.
o = 100000
beta = 1
ener = 0
ener2 = 0
absmagn = 0
magn = 0
magn2 = 0

for k in range(o):
    for i in range(m):
        for j in range(n):
            u = randint(0,m)
            v = randint(0,n)
            dE = 2*(M[u,v]*M[u,(v+1) % (n)] + M[u,v]*M[(u+1) % (m),v] + M [u,v]*M[u,(v-1) % (n)] + M[u,v]*M[(u-1) % (m),v])
            if exp( -beta*dE ) > rand():
                M[u,v] = -M[u,v]
    
    ener += S(M)
    ener2 += S(M)**2
    magn += sum(M)
    absmagn += abs(sum(M))
    magn2 += sum(M)**2


print "Energy:", ener/o
print "Magn:",   absmagn/o
print "Cv:",     ener2/o - (ener/o)**2
print "X:",      magn2/o - (absmagn/o)**2
