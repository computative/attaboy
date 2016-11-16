from numpy import *
import os

#Ts = linspace(2,2.4,jobs)
#Ts = append(append(linspace(2, 2.225,7), linspace(2.25,2.35,18) ), linspace(2.3625,2.4,5))
#Ts = append(append(linspace(2, 2.2,3), linspace(2.22,2.3,6) ), linspace(2.32,2.4,3))
for j in range(8):
	#for j in range(len(Ts)-1):
    		outfile = open("job%drun.sh" % (j), 'w')
   		outfile.write("#!/bin/bash\n")
    		outfile.write("#SBATCH --partition=normal \n")
    		outfile.write("#SBATCH --nodes=1 \n")
    		outfile.write("#SBATCH --ntasks-per-node=8 \n")
    		outfile.write("#SBATCH --time=24:00:00 \n")
    		outfile.write("#SBATCH --job-name=netflixAndChill \n")
    
    		outfile.write("mpirun -n 1 python runIsing.py \n")
    		outfile.close()
    		print "sbatch job%drun.sh" % (j)
    		os.popen("sbatch job%drun.sh" % (j))
#outfile.close()
