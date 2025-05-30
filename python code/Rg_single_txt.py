import numpy as np
import math
import matplotlib.pyplot as plt #绘图

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Per=PERCENT
BOX=25*25*25

N_PEG=int(BOX*Per*0.001/(4*math.pi*0.8**3/3))
N_atoms=148+N_PEG

if Per==150:
    N_atoms=1237

N_one=N_atoms+9

begintime=0
Timeall=90001
delta_tamp=1
N_tamp=round((Timeall-begintime)/delta_tamp)

if Per==0:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_%.3f_nopb/tdp43_300.000.trj' %(Per*0.001),'r')

if Per==1 or Per==5 or Per==15:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_-%.3f_nopb/tdp43_300.000.trj' %(Per*0.001),'r')
else:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_-%.2f_nopb/tdp43_300.000.trj' %(Per*0.001),'r')
line=f.readlines()
Lmax=len(line)

r_all=np.zeros([N_tamp,N_atoms,3])

type=[]


for i in range(N_tamp):

    print(i)
    for j in range(N_atoms):
        sss=line[round(begintime+i*delta_tamp)*N_one+9+j].split()

        index=float(sss[0])
       
        type.append(float(sss[1]))
        r_all[i][round(index-1)][0]=float(sss[2])
        r_all[i][round(index-1)][1]=float(sss[3])
        r_all[i][round(index-1)][2]=float(sss[4])


for i in range(N_tamp):
        for k in range(1,148):
        
            while r_all[i][k][1]-r_all[i][k-1][1]>240:
                r_all[i][k][1]=r_all[i][k][1]-250
            while r_all[i][k][1]-r_all[i][k-1][1]<-240:
                r_all[i][k][1]=r_all[i][k][1]+250

            while r_all[i][k][2]-r_all[i][k-1][2]>240:
                r_all[i][k][2]=r_all[i][k][2]-250
            while r_all[i][k][2]-r_all[i][k-1][2]<-240:
                r_all[i][k][2]=r_all[i][k][2]+250


mass_sum=0
for i in range(148):
    mass_sum=mass_sum+Mass[round(type[i])]


Rg=[]
for i in range(N_tamp):

        R_c=np.zeros([3])
        for k in range(148):
            R_c[0]=R_c[0]+r_all[i][k][0]*Mass[round(type[k])]/mass_sum
            R_c[1]=R_c[1]+r_all[i][k][1]*Mass[round(type[k])]/mass_sum
            R_c[2]=R_c[2]+r_all[i][k][2]*Mass[round(type[k])]/mass_sum

        Rg_n=0
        for k in range(148):
        
            Rg_n=Rg_n+((r_all[i][k][0]-R_c[0])**2+(r_all[i][k][1]-R_c[1])**2+(r_all[i][k][2]-R_c[2])**2)*Mass[round(type[k])]/mass_sum

        Rg.append(math.sqrt(Rg_n))

np.savetxt('Rg_llps_%d.txt' %(Per), np.c_[Rg],fmt='%f',delimiter='\t')