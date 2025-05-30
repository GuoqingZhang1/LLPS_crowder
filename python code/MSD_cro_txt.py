import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=11001

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]

# f=open('ul11stll.lammpstrj','r')
f=open('Restru.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

R_cro=np.zeros([Timeall-begintime,N_PEG,4])

for i in range(Timeall-begintime):
    for j in range(N_atoms):
        sss=line[(begintime+i)*N_one+9+j].split()
        type=float(sss[1])
        index=float(sss[0])
        if type==21:
            R_cro[i][round(index-14800-1)][0]=round(type)
            R_cro[i][round(index-14800-1)][1]=float(sss[2])
            R_cro[i][round(index-14800-1)][2]=float(sss[3])
            R_cro[i][round(index-14800-1)][3]=float(sss[4])

for k in range(N_PEG):
    for i in range(Timeall-begintime-1):
        while(R_cro[i+1][k][3]-R_cro[i][k][3]>400):
            R_cro[i+1][k][3]-500
        while(R_cro[i+1][k][3]-R_cro[i][k][3]<-400):  
            R_cro[i+1][k][3]+500        

MSD_cro=[]
for tau in range(Timeall-begintime-1):
    Dz=0
    for i in range(Timeall-begintime-tau):
        for k in range(N_PEG):
            Dz=Dz+((R_cro[i+tau,k,3])-(R_cro[i,k,3]))**2
    

    MSD_cro.append(Dz/(N_PEG*(Timeall-begintime-tau)))

np.savetxt('MSD_cro_llps.txt', np.c_[MSD_cro],fmt='%f',delimiter='\t')