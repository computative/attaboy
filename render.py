from numpy import *
import os
files = os.listdir("/home/marius/Dokumenter/fys4150/attaboy/runs/")
N = len(files)

data = zeros((4*8*N,6))


for i, f in zip(range(N), files):
    tmp = loadtxt("/home/marius/Dokumenter/fys4150/attaboy/runs/" + f)
    data[4*i*8     : 8*(4*i+1)] = tmp[0:8]*(array([1,1,0,0,0,0]) +  array([0,0,1,1,1,1])/20.**2)
    data[8*(4*i+1) : 8*(4*i+2)] = tmp[8:16]*(array([1,1,0,0,0,0]) +  array([0,0,1,1,1,1])/60.**2) 
    data[8*(4*i+2) : 8*(4*i+3)] = tmp[16:24]*(array([1,1,0,0,0,0]) +  array([0,0,1,1,1,1])/100.**2)
    data[8*(4*i+3) : 8*(4*i+4)] = tmp[24:32]*(array([1,1,0,0,0,0]) +  array([0,0,1,1,1,1])/140.**2)

savetxt('/home/marius/Dokumenter/fys4150/attaboy/resources/bigdata.txt',data)

exit()

from matplotlib.pyplot import *

plot(T,data[0,keys,5],T,data[1,keys,5],T,data[2,keys,5],T,data[3,keys,5])
show()
plot(T,data[0,keys,5],T,data[1,keys,5],T,data[2,keys,5],T,data[3,keys,5])
show()
plot(T,1./4*(data[0,keys,4]+data[1,keys,4]+data[2,keys,4]+data[3,keys,4]))
show()
plot(T,data[0,keys,3],T,data[1,keys,3],T,data[2,keys,3],T,data[3,keys,3])
show()
plot(T,data[0,keys,2],T,data[1,keys,2],T,data[2,keys,2],T,data[3,keys,2])
show()
