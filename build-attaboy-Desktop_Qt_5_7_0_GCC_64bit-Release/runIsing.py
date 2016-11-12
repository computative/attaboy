from numpy import *
from os import popen
from matplotlib.pyplot import *
ns = [20,60,100,140]
Ts = [2,2.4]
#ns = [20,40]
N  = int(10**6)

data = zeros((len(ns)*8,6 ))
for T in Ts:
    for n in ns:
        A = popen("./attaboy %f %i %i %i" % (T,N,n,1000 ) )
