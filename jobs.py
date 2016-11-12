from numpy import *
import os
jobs = 30
Ts = linspace(2,2.4,jobs)
#Ts = append(append(linspace(2, 2.225,7), linspace(2.25,2.35,18) ), linspace(2.3625,2.4,5))
for j in range(len(Ts)-1):
    outfile = open("job%d.sh" % j, 'w')
    outfile.write("#!/bin/bash\n")
    outfile.write("#SBATCH --partition=normal \n")
    outfile.write("#SBATCH --nodes=1 \n")
    outfile.write("#SBATCH --ntasks-per-node=8 \n")
    outfile.write("#SBATCH --time=12:00:00 \n")
    outfile.write("#SBATCH --job-name=whatever \n")
    
    outfile.write("mpirun -n 1 python runIsing.py %f %f \n" % (Ts[j], Ts[j+1]))
    outfile.close()
    print "sbatch job%d.sh" % (j)
    os.popen("sbatch job%d.sh" % j)
#outfile.close()
