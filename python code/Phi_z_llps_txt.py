import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=50001

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

Rc_z=[]
for i in range(Timeall-begintime):
    for j in range(100):
        ri_z=[]
        ri_z.append(np.sum(Rm[i,j,0:51,2])/np.sum(Mass_res[0:51]))
        ri_z.append(np.sum(Rm[i,j,51:74,2])/np.sum(Mass_res[51:74]))
        ri_z.append(np.sum(Rm[i,j,74:148,2])/np.sum(Mass_res[74:148]))
        Rc_z.append(ri_z)



f_Phi=open('Phi_llps.txt','r')
line_Phi=f_Phi.readlines()

Phi_min=0
Phi_max=math.pi
delta=0.01
N_bins=math.ceil((Phi_max-Phi_min)/delta)

Dr0=np.zeros([500,N_bins])
Dr1=np.zeros([500,N_bins])
Dr2=np.zeros([500,N_bins])

for i in range(len(Rc_z)):
    ss=line_Phi[i].split()
    xi=math.floor(Rc_z[i][0]+250)
    yi=math.floor(np.arccos(float(ss[0]))/delta)

    Dr0[xi][yi]+=1

    xi=math.floor(Rc_z[i][1]+250)
    yi=math.floor(np.arccos(float(ss[1]))/delta)

    Dr1[xi][yi]+=1

    xi=math.floor(Rc_z[i][2]+250)
    yi=math.floor(np.arccos(float(ss[2]))/delta)

    Dr2[xi][yi]+=1

np.savetxt('Phi_0_z_llps.txt', np.c_[Dr0],fmt='%f',delimiter='\t')
np.savetxt('Phi_1_z_llps.txt', np.c_[Dr1],fmt='%f',delimiter='\t')
np.savetxt('Phi_2_z_llps.txt', np.c_[Dr2],fmt='%f',delimiter='\t')

# Rc_min=np.min(Rc_z)
# Rc_max=np.max(Rc_z)
# delta_Rc=1
# N_c=math.ceil((Rc_max-Rc_min)/delta_Rc)

# Phi_z=np.zeros([N_c,3])
# for i in range(len(Rc_z)):

#     if Rc_min<=Rc_z[i]<Rc_max:
#         j=math.floor((Rc_z[i]-Rc_min)/delta_Rc)
#         Phi_z[j][0]=Rc_min+j*delta_Rc
#         Phi_z[j][1]=Phi_z[j][1]+np.arccos(float(line_Phi[i]))
#         Phi_z[j][2]=Phi_z[j][2]+1

# np.savetxt('Phi_z_llps.txt', np.c_[Phi_z],fmt='%f',delimiter='\t')
