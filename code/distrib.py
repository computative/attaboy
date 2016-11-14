from numpy import *

temp1 = loadtxt("../resources/variance_temp1.000000.txt")
temp2 = loadtxt("../resources/variance_temp2.400000.txt")

from matplotlib.pyplot import *

hist(temp1, normed=True)
show()

hist(temp2, normed = True)
show()
