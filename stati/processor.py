from numpy import *
import os
files = os.listdir("/home/marius/Dokumenter/fys4150/attaboy/stati/")

N = 248
data = zeros((815*N, 2))
i = 0
for f in files:
    if (("file_140" in f) and ("2.000000" in f) ):
        tmp = loadtxt("/home/marius/Dokumenter/fys4150/attaboy/stati/" + f)
        data[i*815:(i+1)*815,0] = tmp[:,0]
        data[i*815:(i+1)*815,1] = tmp[:,3]
        i += 1
savetxt('/home/marius/Dokumenter/fys4150/attaboy/resources/S140_2T0.txt', data)
