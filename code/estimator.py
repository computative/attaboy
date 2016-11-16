from numpy import *

data = loadtxt("../resources/biggdat.txt")

T = data[:,0]
Tc = array([0.,0.,0.,0.])
L  = array([20.,60.,100.,140.])

Tc[0] = mean([T[argmax(data[:,1])], T[argmax(data[:,5])] ])
Tc[1] = mean([T[argmax(data[:,2])], T[argmax(data[:,6])] ])
Tc[2] = mean([T[argmax(data[:,3])], T[argmax(data[:,7])] ])
Tc[3] = mean([T[argmax(data[:,4])], T[argmax(data[:,8])] ])

a = array([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]])

for i in range(4):
    for j in range(4):
        if i != j:
            a[i][j] = (1/12.)*(Tc[i] - Tc[j])/(float(L[i])**-1 - float(L[j])**-1 )
        else:
            a[i][j] = 0
a = sum(a)

print 2./log(1 + 2**.5)
print sum((Tc - a*L**-1)/4)
print 2./log(1 + 2**.5) - sum((Tc - a*L**-1)/4)
