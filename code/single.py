
# -*- coding: utf-8 -*-
from numpy import *
from numpy.linalg import *
from numpy.fft import *

import matplotlib as mpl
mpl.use("pgf")
pgf_with_pdflatex = {
    "font.family": "serif",
    "font.serif": [],
    "font.size" : 11.0,
    "pgf.preamble": [
         r"\usepackage[utf8]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
         r"\usepackage{newtxtext}",
         r"\usepackage{bm}",
         r"\usepackage{amsmath,amsthm}"
         ]
}
mpl.rcParams.update(pgf_with_pdflatex)
# blue, violet, green, brown, red ,orange
mpl.rcParams['axes.color_cycle'] = ['k', 'k', 'k', 'k', '#d30704' ,'#ff6100']

import matplotlib.pyplot as plt
from os import popen, remove
from numpy import *
from numpy.random import *

I = 1 # I stamples, 2 T, 2 t matriser
y = zeros((I, 2, 2, 3, I))
x = zeros((I, 2, 2, I))
betas = [1/1., 1/2.4]
As = [0,1]
N = 1e5

Ns = logspace(1,log10(N),500, dtype=int)
distr = zeros( ( 2*(N-1000),2) )
accepts = zeros( (len(Ns),2,2 ))
Es = zeros((len(Ns), 2,2))
Ms = zeros((len(Ns), 2,2))

for j in range(len(betas)):
    for k in range(len(As)):
        beta,A0 = betas[j], As[k] # A0 = 1 random matrix
        A = popen("./research.x %i %f %i" % (N,beta,A0) )
        print A.readlines()
        tmp = zeros((N,3))

        infile = open("temp.txt")
        for l, line in zip(range(int(N)), infile.readlines()):
            tmp[l] = array(line.strip('\n').split()).astype(float)
        Es[:,j,k] = (cumsum(tmp[:,0])*arange(1,N+1, dtype=float)**(-1))[Ns-1]
        Ms[:,j,k] = (cumsum(abs(tmp[:,1]))*arange(1,N+1, dtype=float)**(-1))[Ns-1]
        accepts[:,j,k] = tmp[Ns-1,2]

        if j == 0:
            if k == 0:
                distr[:N-1000,0] = tmp[1000:,0]
            if k == 1:
                distr[N-1000:,0] = tmp[1000:,0]
        if j == 1:
            if k == 0:
                distr[:N-1000,1] = tmp[1000:,0]
            if k == 1:
                distr[N-1000:,1] = tmp[1000:,0]
        remove("temp.txt")

f, ax = plt.subplots(4,2,figsize=(2*0.8*4,3.4*0.8*3))


print var(distr[:,0]), var(distr[:,0])/20**2
print var(distr[:,1]), var(distr[:,1])/2.4**2/20**2

ax[0,0].semilogx(Ns,Es[:,0,0],'k')
ax[0,0].semilogx(Ns,Es[:,0,1],'k', dashes=[2,2])
ax[0,0].set_ylim(-850, 0.8*max(Es[:,0,1]) )
ax[0,0].set_xlabel(ur"Iteration $n$")
ax[0,0].set_ylabel(ur"$\langle E \rangle$\quad[$J$]")

ax[0,1].semilogx(Ns,Es[:,1,0],'k', label="Ordered start values")
ax[0,1].semilogx(Ns,Es[:,1,1],'k', dashes=[2,2], label="Random start values")
ax[0,1].legend(fontsize=11)
ax[0,1].set_xlabel(ur"Iteration $n$")
ax[0,1].set_ylabel(ur"$\langle E \rangle$\quad[$J$]")
ax[0,1].set_ylim(-650,-300)

ax[0,1].set_title(ur"Observables, $T=2.4$", fontsize=11)
ax[0,0].set_title(ur"Observables, $T=1$", fontsize=11)


ax[1,0].semilogx(Ns,Ms[:,0,0],'k')
ax[1,0].semilogx(Ns,Ms[:,0,1],'k', dashes=[2,2])
ax[1,0].set_ylim(0.8*min(Ms[:,0,1]), 1.2*max(Ms[:,0,0]) )
ax[1,0].set_xlabel(ur"Iteration $n$")
ax[1,0].set_ylabel(ur"$\langle M \rangle$\quad[ $\cdot$ ]")

ax[1,1].semilogx(Ns,Ms[:,1,0],'k')
ax[1,1].semilogx(Ns,Ms[:,1,1],'k', dashes=[2,2])
ax[1,1].set_xlabel(ur"Iteration $n$")
ax[1,1].set_ylabel(ur"$\langle M \rangle$\quad[ $\cdot$ ]")

ax[2,0].semilogx(Ns,accepts[:,0,0],'k')
ax[2,0].semilogx(Ns,accepts[:,0,1],'k', dashes=[2,2])
ax[2,0].set_xlabel(ur"Iteration $n$")
ax[2,0].set_ylabel(ur"Num accepts\quad[ $\cdot$ ]")

ax[2,1].semilogx(Ns[::4],accepts[::4,1,0],'k')
ax[2,1].semilogx(Ns[::4],accepts[::4,1,1],'k', dashes=[2,2])
ax[2,1].set_xlabel(ur"Iteration $n$")
ax[2,1].set_ylabel(ur"Num accepts\quad[ $\cdot$ ]")

ax[3,0].hist(distr[:,0], normed=True,facecolor="white")
ax[3,0].set_xlabel(ur"$E$\quad[ $J$ ]")
ax[3,0].set_ylabel(ur"P(E)")
ax[3,1].hist(distr[:,1], normed=True,facecolor="white")
ax[3,1].set_xticks([-900, -700, -500, -300, -100])
ax[3,1].set_xlabel(ur"$E$\quad[ $J$ ]")
ax[3,1].set_ylabel(ur"P(E)")

plt.tight_layout(0.5)
plt.savefig("../benchmark/2020.pgf")
plt.savefig("../benchmark/2020.png")
