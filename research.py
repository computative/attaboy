from os import popen, remove
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

I = 8 # I stamples, 2 T, 2 t matriser
y = zeros((I, 2, 2, 3, I))
x = zeros((I, 2, 2, I))
betas = [1/2., 1/2.3]
As = [0,1]


for i in range(I):
    for j in range(2):
        for k in range(2):
            N,beta,A0 = int(1e3), betas[j], As[k] # A0 = 1 random matrix
            A = popen("./research2.x %i %f %i" % (N,beta,A0) )
            print A.readlines()

            tmp = zeros((N,3))

            infile = open("temp.txt")
            for l, line in zip(range(N), infile.readlines()):
                tmp[l] = array(line.strip('\n').split()).astype(float)
            E = cumsum(tmp[:,0])*arange(1,N+1, dtype=float)**(-1)
            M = cumsum(abs(tmp[:,1]))*arange(1,N+1, dtype=float)**(-1)
            accept = tmp[:,2]
            var = sort(append(exp(3*log(10)*rand(I-1)),0.95e3)).astype(int)
            x[i,j,k] = var
            y[i,j,k,:] = [E[var],M[var],accept[var]]
            remove("temp.txt")

scatter( x[:,0,0].reshape(I**2),y[:,0,0,0].reshape(I**2))
show()
savetxt('researchdata.txt', array([
    x[:,0,0].reshape(I**2),y[:,0,0,0].reshape(I**2),y[:,0,0,1].reshape(I**2),y[:,0,0,2].reshape(I**2),
    x[:,0,1].reshape(I**2),y[:,0,1,0].reshape(I**2),y[:,0,1,1].reshape(I**2),y[:,0,1,2].reshape(I**2),
    x[:,1,0].reshape(I**2),y[:,1,0,0].reshape(I**2),y[:,1,0,1].reshape(I**2),y[:,1,0,2].reshape(I**2),
    x[:,1,1].reshape(I**2),y[:,1,1,0].reshape(I**2),y[:,1,1,1].reshape(I**2),y[:,1,1,2].reshape(I**2),
                       ]).T )
