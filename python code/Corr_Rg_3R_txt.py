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

# f=open('ul11stll.lammpstrj','r')
f=open('Rg_3R.txt','r')
line=f.readlines()
Lmax=len(line)


Rg=np.zeros([Timeall-begintime,2,100])
for i in range(Timeall-begintime):
    for j in range(100):

        ss=line[i*100+j].split()
        Rg[i][0][j]=float(ss[0])
        Rg[i][1][j]=float(ss[2])

Sum_Auto=np.zeros([2,100])
Mean_Auto=np.zeros([2,100])
for j in range(100):
    for i in range(Timeall-begintime-1):
        Sum_Auto[0][j]+=(Rg[i][0][j]-np.mean(Rg[:,0,j]))**2
        Sum_Auto[1][j]+=(Rg[i][1][j]-np.mean(Rg[:,1,j]))**2
    Mean_Auto[0][j]=np.mean(Rg[:,0,j])
    Mean_Auto[1][j]=np.mean(Rg[:,1,j])

Corr_0_Rg=np.zeros([Timeall-begintime-1,100])
Corr_1_Rg=np.zeros([Timeall-begintime-1,100])
for dt in range(Timeall-begintime-1):
    
    for i in range(Timeall-begintime-dt):
        Corr_0_Rg[dt]=Corr_0_Rg[dt]+(Rg[i][0]-Mean_Auto[0])*(Rg[i+dt][0]-Mean_Auto[0])/Sum_Auto[0]
        Corr_1_Rg[dt]=Corr_1_Rg[dt]+(Rg[i][1]-Mean_Auto[1])*(Rg[i+dt][1]-Mean_Auto[1])/Sum_Auto[1]

np.savetxt('Corr_0_Rg.txt', np.c_[Corr_0_Rg],fmt='%f',delimiter='\t')
np.savetxt('Corr_1_Rg.txt', np.c_[Corr_1_Rg],fmt='%f',delimiter='\t')