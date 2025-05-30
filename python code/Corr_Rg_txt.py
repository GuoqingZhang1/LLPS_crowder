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
f=open('Rg_llps.txt','r')
line=f.readlines()
Lmax=len(line)



Rg=np.zeros([Timeall-begintime,100])
for i in range(Timeall-begintime):
    for j in range(100):

        ss=line[i*100+j].split()
        Rg[i][j]=float(ss[0])

Sum_Auto=np.zeros(100)
Mean_Auto=np.zeros(100)
for j in range(100):
    for i in range(Timeall-begintime-1):
        Sum_Auto[j]+=(Rg[i][j]-np.mean(Rg[:,j]))**2
    Mean_Auto[j]=np.mean(Rg[:,j])

Corr_Rg=np.zeros([Timeall-begintime-1,100])
for dt in range(Timeall-begintime-1):
    
    for i in range(Timeall-begintime-dt):
        Corr_Rg[dt]=Corr_Rg[dt]+(Rg[i]-Mean_Auto)*(Rg[i+dt]-Mean_Auto)/Sum_Auto
        

np.savetxt('Corr_Rg.txt', np.c_[Corr_Rg],fmt='%f',delimiter='\t')