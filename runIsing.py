from numpy import *
from os import popen
import sys
#from matplotlib.pyplot import *

ns = [20,60,100,140]
N = int(10**6)
Tstart = float(sys.argv[1])
Tstop = float(sys.argv[2])
data = zeros((len(ns)*8,6 ))
for i, n in zip(range(len(ns)),ns):
    A = popen("./attaboy %f %f %i %i" % (Tstart,Tstop,N,n) )
    data[i*8:(i+1)*8] = array([line.strip("\n").split() for line in A], dtype=float)
savetxt("data%f_%f.txt" % (Tstart, Tstop), data)
