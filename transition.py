from numpy import *
from os import popen
from matplotlib.pyplot import *
dt = 0.05
N = int(10**5)
n = 20
A = popen("/home/marius/Dokumenter/fys4150/attaboy/build-attaboy-Desktop_Qt_5_7_0_GCC_64bit-Release/attaboy %f %i %i" % (dt,N,n) )
raw = array([line.strip("\n").split() for line in A], dtype=float)
keys = argsort(raw[:,0])
raw = raw[keys]

T = linspace(2+dt, 2 + len(raw)*dt, len(raw) )
print raw

plot(T, raw[:,5])
show()
plot(T, raw[:,4])
show()
plot(T, raw[:,3])
show()
plot(T, raw[:,2])
show()

