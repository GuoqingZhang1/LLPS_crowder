import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=20001

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]

# f=open('ul11stll.lammpstrj','r')
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

Z_pro=np.zeros([Timeall-begintime,100,4])
for i in range(Timeall-begintime):
    for j in range(100):
        Zm=R_pro[i,j,:,3]*Mass_res
        Z_pro[i][j][0]=np.sum(Zm[0:51])/np.sum(Mass_res[0:51])
        Z_pro[i][j][1]=np.sum(Zm[51:74])/np.sum(Mass_res[51:74])
        Z_pro[i][j][2]=np.sum(Zm[74:148])/np.sum(Mass_res[74:148])
        Z_pro[i][j][3]=np.sum(Zm[:])/np.sum(Mass_res[:])


MSD_4=np.zeros([Timeall-begintime-1,3])
MSD_all=[]

N_mean=10
MSD100=np.zeros([N_mean])

for tau in range(Timeall-begintime-1):
    Dz0=0
    Dz1=0
    Dz2=0
    Dz=0
    Dz3=0
    for i in range(Timeall-begintime-tau):
        for j in range(100):
            Dz0=Dz0+(Z_pro[i+tau][j][0]-Z_pro[i][j][0])**2
            Dz1=Dz1+(Z_pro[i+tau][j][1]-Z_pro[i][j][1])**2
            Dz2=Dz2+(Z_pro[i+tau][j][2]-Z_pro[i][j][2])**2
            Dz=Dz+(Z_pro[i+tau][j][3]-Z_pro[i][j][3])**2
    
            if tau==100:
                for k in range(N_mean):
                    if 10*k<=j<10*(k+1):
                        MSD100[k]+=(Z_pro[i+tau][j][3]-Z_pro[i][j][3])**2/((Timeall-begintime-tau)*10)
    
    MSD_4[tau][0]=Dz0/((Timeall-begintime-tau)*100)
    MSD_4[tau][1]=Dz1/((Timeall-begintime-tau)*100)
    MSD_4[tau][2]=Dz2/((Timeall-begintime-tau)*100)
    MSD_all.append(Dz/((Timeall-begintime-tau)*100))

MSD_100=[]
MSD_100.append(np.mean(MSD100))
MSD_100.append(np.std(MSD100))

np.savetxt('MSD_4R_llps.txt', np.c_[MSD_4],fmt='%f',delimiter='\t')
np.savetxt('MSD_all_llps.txt', np.c_[MSD_all],fmt='%f',delimiter='\t')
np.savetxt('MSD_100.txt', np.c_[MSD_100],fmt='%f',delimiter='\t')