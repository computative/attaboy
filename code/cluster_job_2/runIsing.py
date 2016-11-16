from numpy import *
from os import popen
ns = [20,60,100,140]
Ts = [2, 2.1, 2.2, 2.3, 2.4]
N  = int(10**6)

for T in Ts:
    for n in ns:
        A = popen("./attaboy %f %i %i %i" % (T,N,n,1000 ) )
