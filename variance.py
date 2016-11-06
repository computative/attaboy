from os import popen, remove
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

N = int(1e5)
T = [1,2.4]
for t in T:
    N,beta,A0 = N, 1./t, 0 # A0 = 1 random matrix
    A = popen("./research.x %i %f %i" % (N,beta,A0) )
    print A.readlines()

    tmp = zeros((N,3))

    infile = open("temp.txt")
    for l, line in zip(range(N), infile.readlines()):
        tmp[l] = array(line.strip('\n').split()).astype(float)
    E = tmp[:,0]
    remove("temp.txt")
    print var(E[10000:])
    print mean(E[10000:])
    savetxt("variance_temp%f.txt" % (t), E[10000:])
