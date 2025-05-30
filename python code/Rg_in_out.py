import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from sklearn import neighbors

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Per=PERCENT
BOX=25*25*25

N_PEG=int(BOX*Per*0.001/(4*math.pi*0.8**3/3))
N_atoms=148+N_PEG

# if Per==150:
#     N_atoms=1237

N_one=N_atoms+9

begintime=0
Timeall=90001
delta_tamp=1
N_tamp=round((Timeall-begintime)/delta_tamp)

if Per==0:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_%.2f_nopb/tdp43_300.000.trj' %(Per*0.001),'r')

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

f_pro=open('Rg_llps_%d.txt' %(Per),'r')
line_pro=f_pro.readlines()

Rg=[]

for i in range(len(line_pro)):
    Rg.append(float(line_pro[i]))

mass_sum=0
for i in range(148):
    mass_sum=mass_sum+Mass[round(type[i])]

R_np=1.5*(3.82/2+8)

per_in=[]
per_out=[]

for i in range(N_tamp):
    knn = neighbors.NearestNeighbors(algorithm='kd_tree',radius=R_np) 
    knn.fit(r_all[i])
    N_all=[]
    N_in=[]

    R_c=np.zeros([3])

    for j in range(148):

        R_c[0]=R_c[0]+r_all[i][j][0]*Mass[round(type[j])]/mass_sum
        R_c[1]=R_c[1]+r_all[i][j][1]*Mass[round(type[j])]/mass_sum
        R_c[2]=R_c[2]+r_all[i][j][2]*Mass[round(type[j])]/mass_sum

        result = knn.radius_neighbors_graph([r_all[i][j]],mode  ='distance')
        ls=result.tocoo().col
        
        for k in ls:
            if k >147:
                if k not in N_all:
                    N_all.append(k)
                
                if ((r_all[i][k][0]-R_c[0])**2+(r_all[i][k][1]-R_c[1])**2+(r_all[i][k][2]-R_c[2])**2)**0.5<Rg[i]:
                    if k not in N_in:
                        N_in.append(k)
            
    per_in.append(len(N_in))
    per_out.append((len(N_all)-len(N_in)))

np.savetxt('Rg_per_in_%d.txt' %(Per), np.c_[per_in],fmt='%f',delimiter='\t')

np.savetxt('Rg_per_out_%d.txt' %(Per), np.c_[per_out],fmt='%f',delimiter='\t')