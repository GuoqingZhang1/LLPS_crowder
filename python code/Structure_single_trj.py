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

Rotation=np.load(file="Rotation_%d.npy" %(Per))

r_all=np.zeros([N_tamp,N_atoms,3])

for i in range(N_tamp):
    for j in range(N_atoms):
        sss=line[round(begintime+i*delta_tamp)*N_one+9+j].split()

        index=float(sss[0])
       
        r_all[i][round(index-1)][0]=float(sss[2])
        r_all[i][round(index-1)][1]=float(sss[3])
        r_all[i][round(index-1)][2]=float(sss[4])

r_re=np.zeros([N_tamp,148,3])

for i in range(N_tamp):
    for j in range(148):
        for k in range(3):
            r_re[i][j][0]+=Rotation[i][0][k]*(r_all[i,j,k]-np.mean(r_all[i,:,k]))
            r_re[i][j][1]+=Rotation[i][1][k]*(r_all[i,j,k]-np.mean(r_all[i,:,k]))
            r_re[i][j][2]+=Rotation[i][2][k]*(r_all[i,j,k]-np.mean(r_all[i,:,k]))

f_pro=open('Rg_llps_%d.txt' %(10*Per),'r')
line_pro=f_pro.readlines()

Rg=[]

for i in range(len(line_pro)):
    Rg.append(float(line_pro[i]))

dRg=0.001

Ind=[]
for i in range(len(line_pro)):
    if np.abs(Rg[i]-np.mean(Rg))<dRg:
        Ind.append(i)
        break

r_f=np.zeros([148,3])
for i in Ind:
    for j in range(148):
        for k in range(3):
            r_f[j][k]+=r_re[i][j][k]/len(Ind)

f_data=open('Structure_mean_%d.lammpstrj' %(Per),'w')

f_data.write('ITEM: TIMESTEP\n')
f_data.write('0\n')
f_data.write('ITEM: NUMBER OF ATOMS\n')
f_data.write('148\n')
f_data.write('ITEM: BOX BOUNDS pp pp pp\n')
f_data.write('-50 50 \n')
f_data.write('-50 50 \n')
f_data.write('-50 50 \n')
f_data.write('ITEM: ATOMS id type x y z\n')

for i in range(148):
    for j in range(20):
        if AAsequence[i]==Saa[j]:
            break

    f_data.write('%3d %2d %f %f %f\n' %(i+1,j+1,r_f[i][0],r_f[i][1],r_f[i][2]))
