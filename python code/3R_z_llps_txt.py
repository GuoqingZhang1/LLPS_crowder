import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

begintime=10000
Timeall=50001

f=open('Restru.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

R_pro=np.zeros([Timeall-begintime,100,148,4])     #0: type 1: x 2: y 3: z
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

        else:
            n_l=math.floor((index-1)/148)
            n_b=round(index-1-148*n_l)
            R_pro[i][n_l][n_b][0]=round(type)
            R_pro[i][n_l][n_b][1]=float(sss[2])
            R_pro[i][n_l][n_b][2]=float(sss[3])
            R_pro[i][n_l][n_b][3]=float(sss[4])

for i in range(Timeall-begintime):
    for j in range(100):
        for k in range(1,148):
        
            if R_pro[i][j][k][1]-R_pro[i][j][k-1][1]>140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]-150
            elif R_pro[i][j][k][1]-R_pro[i][j][k-1][1]<-140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]+150

            if R_pro[i][j][k][2]-R_pro[i][j][k-1][2]>140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]-150
            elif R_pro[i][j][k][2]-R_pro[i][j][k-1][2]<-140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]+150

Mass_res=np.zeros([148])

for i in range(148):
    Mass_res[i]=Mass[round(R_pro[0][0][i][0])]

Rm_z=np.zeros([Timeall-begintime,100,148])

for i in range(Timeall-begintime):
    for j in range(100):
        Rm_z[i][j]=R_pro[i,j,:,3]*Mass_res

R1_z=[]
R2_z=[]
R3_z=[]
for i in range(Timeall-begintime):
    for j in range(100):
        r_1=np.sum(Rm_z[i,j,0:51])/np.sum(Mass_res[0:51])
        r_2=np.sum(Rm_z[i,j,51:74])/np.sum(Mass_res[51:74])
        r_3=np.sum(Rm_z[i,j,74:148])/np.sum(Mass_res[74:148])
        R1_z.append(r_1)
        R2_z.append(r_2)
        R3_z.append(r_3)

N_c=500
R1_dis=np.zeros([N_c,3])


for i in range(len(R1_z)):
    
    j=math.floor((R1_z[i]+250))
    R1_dis[j][0]=R1_dis[j][0]+1

    k=math.floor((R2_z[i]+250))
    R1_dis[k][1]=R1_dis[k][1]+1
    
    l=math.floor((R3_z[i]+250))
    R1_dis[l][2]=R1_dis[l][2]+1
        
np.savetxt('3R_z_llps.txt', np.c_[R1_dis],fmt='%f',delimiter='\t')