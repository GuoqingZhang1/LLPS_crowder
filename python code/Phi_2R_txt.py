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
        
            if R_pro[i][j][k][1]-R_pro[i][j][k-1][1]>140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]-150
            elif R_pro[i][j][k][1]-R_pro[i][j][k-1][1]<-140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]+150

            if R_pro[i][j][k][2]-R_pro[i][j][k-1][2]>140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]-150
            elif R_pro[i][j][k][2]-R_pro[i][j][k-1][2]<-140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]+150


Phi=[]
for i in range(Timeall-begintime):
    for j in range(100):
        Phi_ij=[]
        x1=R_pro[i][j][50][1]-R_pro[i][j][0][1]
        y1=R_pro[i][j][50][2]-R_pro[i][j][0][2]
        z1=R_pro[i][j][50][3]-R_pro[i][j][0][3]

        x2=R_pro[i][j][147][1]-R_pro[i][j][74][1]
        y2=R_pro[i][j][147][2]-R_pro[i][j][74][2]
        z2=R_pro[i][j][147][3]-R_pro[i][j][74][3]

        Phi_ij=[z1/math.sqrt(x1**2+y1**+z1**2)]
        Phi_ij=[z2/math.sqrt(x2**2+y2**+z2**2)]
        Phi.append(Phi_ij)


# Start_in=51
# End_in=69
# Phi=[]
# for i in range(Timeall-begintime):
#     for j in range(100):
#         x0=R_pro[i][j][Start_in][1]-R_pro[i][j][End_in][1]
#         y0=R_pro[i][j][Start_in][2]-R_pro[i][j][End_in][2]
#         z0=R_pro[i][j][Start_in][3]-R_pro[i][j][End_in][3]
#         Phi.append(z0/math.sqrt(x0**2+y0**2+z0**2))

np.savetxt('Phi_llps.txt', np.c_[Phi],fmt='%f',delimiter='\t')