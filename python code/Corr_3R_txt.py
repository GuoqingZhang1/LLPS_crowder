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
        
            while R_pro[i][j][k][1]-R_pro[i][j][k-1][1]>140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]-150
            while R_pro[i][j][k][1]-R_pro[i][j][k-1][1]<-140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]+150

            while R_pro[i][j][k][2]-R_pro[i][j][k-1][2]>140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]-150
            while R_pro[i][j][k][2]-R_pro[i][j][k-1][2]<-140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]+150

Mass_res=np.zeros([148])

for i in range(148):
    Mass_res[i]=Mass[round(R_pro[0][0][i][0])]

Rm=np.zeros([Timeall-begintime,100,148,3])

for i in range(Timeall-begintime):
    for j in range(100):
        Rm[i,j,:,0]=R_pro[i,j,:,1]*Mass_res
        Rm[i,j,:,1]=R_pro[i,j,:,2]*Mass_res
        Rm[i,j,:,2]=R_pro[i,j,:,3]*Mass_res


# Distance_t=np.zeros([Timeall-begintime,300,300])

# H_n=[0,51,74,148]


# for i in range(Timeall-begintime):
#     for j in range(300-1):
#         for k in range(j,300):
#             j_l=math.floor(j/3)
#             j_n=round(j-3*j_l)
#             k_l=math.floor(k/3)
#             k_n=round(k-3*k_l)

#             Distance_t[i][j][k]=math.sqrt((np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],0])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],0])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2+(np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],1])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],1])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2+(np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],2])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],2])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2)

Q_t=np.zeros([Timeall-begintime,300,300])

H_n=[0,51,74,148]

f_Rg3R=open('Rg_3R.txt','r')
line_Rg3R=f_Rg3R.readlines()

Rg_3R=np.zeros([3])
for i in range(len(line_Rg3R)):
    ss=line_Rg3R[i].split()
    for j in range(3):
        Rg_3R[j]+=float(ss[j])/len(line_Rg3R)
f_Rg3R.close()

for i in range(Timeall-begintime):
    for j in range(300-1):
        for k in range(j,300):
            j_l=math.floor(j/3)
            j_n=round(j-3*j_l)
            k_l=math.floor(k/3)
            k_n=round(k-3*k_l)

            dij=math.sqrt((np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],0])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],0])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2+(np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],1])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],1])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2+(np.sum(Rm[i,j_l,H_n[j_n]:H_n[j_n+1],2])/np.sum(Mass_res[H_n[j_n]:H_n[j_n+1]])-np.sum(Rm[i,k_l,H_n[k_n]:H_n[k_n+1],2])/np.sum(Mass_res[H_n[k_n]:H_n[k_n+1]]))**2)

            d0=Rg_3R[j_n]+Rg_3R[k_n]

            Q_t[i][j][k]=0.5*(math.tanh(1.2*d0-dij)+1)


Mean=np.zeros([300,300])
Sum=np.zeros([300,300])
for j in range(300-1):
    for k in range(j,300):
        Mean[j][k]=np.mean(Q_t[:,j,k])
        for n in range(Timeall-begintime-1):
            Sum[j][k]=Sum[j][k]+(Q_t[n][j][k]-Mean[j][k])*(Q_t[n][j][k]-Mean[j][k])

Sum = np.where(Sum == 0, 1, Sum)

Corr_3R=np.zeros([Timeall-begintime-1,300,300])
for dt in range(Timeall-begintime-1):
    for i in range(Timeall-begintime-dt):
        Corr_3R[dt]=Corr_3R[dt]+((Q_t[i]-Mean)*(Q_t[i+dt]-Mean))/Sum

np.save(file="Qij.npy", arr=Mean)
np.save(file="Corr_3R.npy", arr=Corr_3R)