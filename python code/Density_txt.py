import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]
Mass_PEG=1500

# f=open('ul11stll.lammpstrj','r')
f=open('Final.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

N_m=100
N_res=148

Per=PERCENT
BOX=15*15*50

N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))

N_atoms=int(N_m*N_res)+N_PEG

durtime=10000
alltime=50000
N_time=int(alltime/durtime)

ratom=np.full([alltime,N_atoms,4],np.nan)           

for t in range(alltime):
    for i in range(N_atoms):
    
        sx=line[t*(N_atoms+9)+i+9].split()
        ratom[t][int(sx[0])-1][0]=float(sx[1])      #1-3为坐标，0为类型
        ratom[t][int(sx[0])-1][1]=float(sx[2])
        ratom[t][int(sx[0])-1][2]=float(sx[3])
        ratom[t][int(sx[0])-1][3]=float(sx[4])


for i in range(N_time):
    begintime=0+i*durtime
    
    Density_res=np.zeros([500])
    Density_peg=np.zeros([500])
    for t in range(durtime):
        for j in range(N_atoms):
            for k in range(500):
                if k<ratom[begintime+t][j][3]<k+1:
                    if ratom[begintime+t][j][0]==21:
                        Density_peg[k]=Density_peg[k]+Mass_PEG/durtime
                    else :
                        Density_res[k]=Density_peg[k]+Mass[round(ratom[begintime+t][j][0])]/durtime

    np.savetxt('Density_res_%d.txt' %(begintime), np.c_[Density_res],fmt='%f',delimiter='\t')
    np.savetxt('Density_peg_%d.txt' %(begintime), np.c_[Density_peg],fmt='%f',delimiter='\t')