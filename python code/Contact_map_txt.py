import numpy as np
import math
import matplotlib.pyplot as plt #绘图
import random

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=50001
delta_tamp=1000
N_tamp=round((Timeall-begintime)/delta_tamp)

Mass_c=1500
Sigma_c=3.82/2+8

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]

# f=open('ul11stll.lammpstrj','r')
f=open('Restru.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

R_pro=np.zeros([N_tamp,100,148,4])     #0: type 1: x 2: y 3: z
R_cro=np.zeros([N_tamp,N_PEG,4])

for i in range(N_tamp):
    for j in range(N_atoms):
        sss=line[round(begintime+i*delta_tamp)*N_one+9+j].split()
        type=float(sss[1])
        index=float(sss[0])
        if type==21:
            R_cro[i][round(index-14800-1)][0]=round(type)
            R_cro[i][round(index-14800-1)][1]=float(sss[2])
            R_cro[i][round(index-14800-1)][2]=float(sss[3])
            R_cro[i][round(index-14800-1)][3]=float(sss[4])

        else:
            n_l=math.floor((index-1)/148)
            n_b=round(index-1-148*n_l)
            R_pro[i][n_l][n_b][0]=round(type)
            R_pro[i][n_l][n_b][1]=float(sss[2])
            R_pro[i][n_l][n_b][2]=float(sss[3])
            R_pro[i][n_l][n_b][3]=float(sss[4])

Intra_map=np.zeros([148,148])
Inter_map=np.zeros([148,148])
Crowd_map=np.zeros([148])

for i in range(N_tamp):

    for m in range(100):
        for j in range(146):
            for k in range(j+2,148):
                Cutoff=1.5*0.5*(Sigma[int(R_pro[i][m][j][0])]+Sigma[int(R_pro[i][m][k][0])])
                d_jk=math.sqrt((R_pro[i][m][j][1]-R_pro[i][m][k][1])**2+(R_pro[i][m][j][2]-R_pro[i][m][k][2])**2+(R_pro[i][m][j][3]-R_pro[i][m][k][3])**2)
                Intra_map[j][k]=Intra_map[j][k]+0.5*(math.tanh(Cutoff-d_jk)+1)

        for n in range(100):
            if n!=m:
                for j in range(148):
                    for k in range(148):
                        Cutoff=1.5*0.5*(Sigma[int(R_pro[i][m][j][0])]+Sigma[int(R_pro[i][n][k][0])])
                        d_jk=math.sqrt((R_pro[i][m][j][1]-R_pro[i][n][k][1])**2+(R_pro[i][m][j][2]-R_pro[i][n][k][2])**2+(R_pro[i][m][j][3]-R_pro[i][n][k][3])**2)
                        Inter_map[j][k]=Inter_map[j][k]+0.5*(math.tanh(Cutoff-d_jk)+1)

        for j in range(148):
            for k in range(N_PEG):
 
                Cutoff=1.5*Sigma_c
                d_jk=math.sqrt((R_pro[i][m][j][1]-R_cro[i][k][1])**2+(R_pro[i][m][j][2]-R_cro[i][k][2])**2+(R_pro[i][m][j][3]-R_cro[i][k][3])**2)
                Crowd_map[j]=Crowd_map[j]+0.5*(math.tanh(Cutoff-d_jk)+1)

np.savetxt('Intra_map.txt', np.c_[Intra_map],fmt='%f',delimiter='\t')
np.savetxt('Inter_map.txt', np.c_[Inter_map],fmt='%f',delimiter='\t')
np.savetxt('Crowd_map.txt', np.c_[Crowd_map],fmt='%f',delimiter='\t')