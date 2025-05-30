import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import random

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD
Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]
Saa=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
Sigma_c=3.82/2+8

Per=PERCENT
BOX=25*25*25
N_PEG=int(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=148+N_PEG
if Per==15:
    N_atoms=1237

N_one=N_atoms+9

begintime=0
Timeall=90001
delta_tamp=1
N_tamp=round((Timeall-begintime)/delta_tamp)

f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_%.2f_nopb/tdp43_300.000.trj' %(Per*0.01),'r')
line=f.readlines()
Lmax=len(line)

r_all=np.zeros([N_tamp,N_atoms,3])

for i in range(N_tamp):
    for j in range(N_atoms):
        sss=line[round(begintime+i*delta_tamp)*N_one+9+j].split()

        index=float(sss[0])
       
        r_all[i][round(index-1)][0]=float(sss[2])
        r_all[i][round(index-1)][1]=float(sss[3])
        r_all[i][round(index-1)][2]=float(sss[4])

r_re=np.zeros([N_tamp,23,3])

for i in range(N_tamp):
    for j in range(23):
        r_re[i][j][0]=r_all[i,51+j,0]-np.mean(r_all[i,51:74,0])
        r_re[i][j][1]=r_all[i,51+j,1]-np.mean(r_all[i,51:74,1])
        r_re[i][j][2]=r_all[i,51+j,2]-np.mean(r_all[i,51:74,2])

H_m=np.zeros([N_tamp,3,3])
for i in range(N_tamp):
    for j in range(3):
        for k in range(3):
            H_m[i][j][k]=np.sum(r_re[i,:,j]*r_re[0,:,k])

Rotation=np.zeros([N_tamp,3,3])
for i in range(N_tamp):
    U, S, Vt = np.linalg.svd(H_m[i], full_matrices=False)

    Rotation[i]=np.dot(Vt.T,U.T)


np.save(file="Rotation_%d.npy" %(Per), arr=Rotation)
