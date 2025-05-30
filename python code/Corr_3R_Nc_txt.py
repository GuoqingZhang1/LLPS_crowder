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
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=40000
Timeall=50001
delta_tamp=1
N_tamp=round((Timeall-begintime)/delta_tamp)

f=open('Restru.lammpstrj','r')
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
        if i < 14800:
            if j <14800:
                xi=i-148*math.floor(i/148)
                yi=j-148*math.floor(j/148)
                for n in range(20):
                    if Saa[n]==AAsequence[xi]:
                        resi=n
                    if Saa[n]==AAsequence[yi]:
                        resy=n
                Sigmma_IJ[i][j]=1.5*0.5*(Sigma[resi]+Sigma[resy])
            else:
                Sigmma_IJ[i][j]=1.5*Sigma_c
        else:
            if j <14800:
                Sigmma_IJ[i][j]=1.5*Sigma_c
            else:
                Sigmma_IJ[i][j]=1.5*16


Q_t=np.zeros([N_tamp,300,300])

H_n=[0,51,74,148]

for i in range(N_tamp):
    distA=pdist(r_all[i],metric='euclidean')
    distB=squareform(distA)

    D_i=np.heaviside(Sigmma_IJ-distB,1)

    for j in range(300-1):
        for k in range(j,300):

            j_l=math.floor(j/3)
            j_n=round(j-3*j_l)
            k_l=math.floor(k/3)
            k_n=round(k-3*k_l)
            
            Q_t[i][j][k]=np.mean(D_i[148*j_l+H_n[j_n]:148*j_l+H_n[j_n+1],148*k_l+H_n[k_n]:148*k_l+H_n[k_n+1]])


# Q2_t=np.zeros([N_tamp,300,6])

# for i in range (N_tamp):
#     for j in range(100):
#         for k in range(3):
#             for l in range(3):
#                 Q2_t[i][j*3+k][0+l]+=Q_t[i][j*3+k][j*3+l]

#                 for n in range(100):
#                     if j<n:
#                         Q2_t[i][j*3+k][3+l]+=Q_t[i][j*3+k][n*3+l]

#                     if j>n:
#                         Q2_t[i][j*3+k][3+l]+=Q_t[i][n*3+k][j*3+l]


Mean=np.zeros([300,300])
Sum=np.zeros([300,300])

for i in range (300):
    for j in range(300):
        Mean[i][j]=np.mean(Q_t[:,i,j])
        
for i in range(N_tamp):
    Sum=Sum+((Q_t[i]-Mean)*(Q_t[i]-Mean))

Sum = np.where(Sum == 0, 1, Sum)
 
Corr_3R=np.zeros([N_tamp-1,300,300]) 
for dt in range(N_tamp-1):
    for i in range(N_tamp-dt):
        Corr_3R[dt]=Corr_3R[dt]+((Q_t[i]-Mean)*(Q_t[i+dt]-Mean))/Sum


np.save(file="Qt_Nc.npy", arr=Q_t)
np.save(file="Qij_Nc.npy", arr=Mean)
np.save(file="Corr_3R_Nc.npy", arr=Corr_3R)