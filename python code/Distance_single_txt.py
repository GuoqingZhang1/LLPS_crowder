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

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

f=open('./trj/tdp43_%.2f_nopb/tdp43_300.000.trj' %(Per*0.01),'r')
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



Sigmma_IJ=np.zeros([N_atoms,N_atoms])

for i in range(N_atoms):
    for j in range(N_atoms):
        if i < 148:
            if j <148:

                for n in range(20):
                    if Saa[n]==AAsequence[i]:
                        resi=n
                    if Saa[n]==AAsequence[j]:
                        resy=n
                Sigmma_IJ[i][j]=1.5*0.5*(Sigma[resi]+Sigma[resy])
            else:
                Sigmma_IJ[i][j]=1.5*Sigma_c
        else:
            if j <14800:
                Sigmma_IJ[i][j]=1.5*Sigma_c
            else:
                Sigmma_IJ[i][j]=1.5*16


Distance=np.zeros([N_atoms,N_atoms])

N_inter=0

for i in range(N_tamp):
    distA=pdist(r_all[i],metric='euclidean')
    distB=squareform(distA)

    D_i=np.heaviside(Sigmma_IJ-distB,1)
 
    Distance+=D_i

    for j in range(100):
        for k in range(100):
            if j!=k and np.mean(D_i[148*j:148*(j+1),148*k:148*(k+1)])!=0:
                N_inter+=1


np.save(file="Distance_%d.npy" %(Per), arr=Distance)
np.save(file="N_inter_%d.npy" %(Per), arr=N_inter)