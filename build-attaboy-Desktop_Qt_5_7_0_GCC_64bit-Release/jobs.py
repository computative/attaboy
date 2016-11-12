from numpy import *

jobs = 31
for j in range(len(Ts)-1):
    outfile = open("job%i.sh" % j, 'w')
    outfile.write("#!/bin/bash\n")
    outfile.write("#SBATCH --partition=normal \n")
    outfile.write("#SBATCH --nodes=1 \n")
    outfile.write("#SBATCH --ntasks-per-node=8 \n")
    outfile.write("#SBATCH --time=08:00:00 \n")
    outfile.write("#SBATCH --job-name=whatever \n")
    
    outfile.write("mpirun -n 1 python runIsing.py %f %f \n" % (Ts[j], Ts[j+1]))
    print "sbatch job%i.sh" % (j)
    
outfile.close()
