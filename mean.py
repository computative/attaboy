from os import popen
A = popen("./mean.x")
print A.readlines()[0].strip('\n').split()
