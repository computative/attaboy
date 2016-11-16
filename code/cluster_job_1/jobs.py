from numpy import *
import os
jobs = 30
#Ts = linspace(2,2.4,jobs)
#Ts = append(append(linspace(2, 2.225,7), linspace(2.25,2.35,18) ), linspace(2.3625,2.4,5))
Ts = append(append(linspace(2, 2.2,3), linspace(2.22,2.3,6) ), linspace(2.32,2.4,3))
for k in range(3):
	for j in range(len(Ts)-1):
    		outfile = open("job%drun%d.sh" % (j,k), 'w')
   		outfile.write("#!/bin/bash\n")
    		outfile.write("#SBATCH --partition=normal \n")
    		outfile.write("#SBATCH --nodes=1 \n")
    		outfile.write("#SBATCH --ntasks-per-node=8 \n")
    		outfile.write("#SBATCH --time=12:00:00 \n")
    		outfile.write("#SBATCH --job-name=whatever \n")
    
    		outfile.write("mpirun -n 1 python runIsing.py %f %f \n" % (Ts[j], Ts[j+1]))
    		outfile.close()
    		print "sbatch job%drun%d.sh" % (j,k)
    		os.popen("sbatch job%drun%d.sh" % (j,k))
#outfile.close()
