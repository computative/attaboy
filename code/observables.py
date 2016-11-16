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
mpl.rcParams['axes.color_cycle'] = ['b', '#800080', '#009900', '#964B00', '#d30704' ,'#ff6100']

import matplotlib.pyplot as plt

data = loadtxt("../resources/biggdat.txt")
T = data[:,0]

f, ax = plt.subplots(2,2,figsize=(2*0.8*4,2*0.8*3))


ax[0][1].plot(T, data[:,9] ,'k', dashes=[8, 4, 2, 4, 2, 4])
ax[0][1].plot(T, data[:,10] ,'k--')
ax[0][1].plot(T, data[:,11] ,'k', dashes=[2,2])
ax[0][1].plot(T, data[:,12] ,'k')
ax[0][0].plot(T, data[:,13] ,'k', dashes=[8, 4, 2, 4, 2, 4])
ax[0][0].plot(T, data[:,14] ,'k--')
ax[0][0].plot(T, data[:,15] ,'k', dashes=[2,2])
ax[0][0].plot(T, data[:,16] ,'k')
ax[0][0].set_xticks([2,2.1,2.2,2.3,2.4])
ax[0][1].set_xticks([2,2.1,2.2,2.3,2.4])

ax[0][0].set_ylabel(ur'$\langle E \rangle$\quad[ $J$ ]')
ax[0][0].set_xlabel(ur'$k_bT$\quad[ $J$ ]')
ax[0][1].set_ylabel(ur'$\langle |M| \rangle$\quad[ $\cdot$ ]')
ax[0][1].set_xlabel(ur'$k_BT$\quad[  $J$ ]')
ax[0][0].set_title(ur"Energy vs thermal energy",fontsize=11)
ax[0][1].set_title(ur"Magnetization vs thermal energy",fontsize=11)

ax[1][1].plot(T, data[:,1] ,'k', dashes=[8, 4, 2, 4, 2, 4])
ax[1][1].plot(T, data[:,2] ,'k--')
ax[1][1].plot(T, data[:,3] ,'k', dashes=[2,2])
ax[1][1].plot(T, data[:,4] ,'k')
ax[1][0].plot(T, data[:,5] ,'k', dashes=[8, 4, 2, 4, 2, 4])
ax[1][0].plot(T, data[:,6] ,'k--')
ax[1][0].plot(T, data[:,7] ,'k', dashes=[2,2])
ax[1][0].plot(T, data[:,8] ,'k')
ax[1][0].set_xticks([2,2.1,2.2,2.3,2.4])
ax[1][1].set_xticks([2,2.1,2.2,2.3,2.4])

ax[1][0].set_ylabel(ur'$\chi$\quad[ $\cdot$ ]')
ax[1][0].set_xlabel(ur'$k_bT$\quad[ $J$ ]')
ax[1][1].set_ylabel(ur'$C_V/k_B$\quad[ $\cdot$ ]')
ax[1][1].set_xlabel(ur'$k_BT$\quad[ $J$ ]')
ax[1][0].set_title(ur"Magnetic succeptability vs thermal energy",fontsize=11)
ax[1][1].set_title(ur"Heat capacity vs thermal energy",fontsize=11)



plt.tight_layout(0.5)
plt.savefig("../benchmark/obs3.pgf")
plt.savefig("../benchmark/obs3.png")



