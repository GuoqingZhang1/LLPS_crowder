import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from scipy import optimize as op
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import random

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Saa=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Per=PERCENT
BOX=12.5*12.5*12.5
N_PEG=int(BOX*Per*0.001/(0.8**3))
N_atoms=148*2+N_PEG
N_one=N_atoms+9

def f_x(x,a,b):
    return a*x+b

begintime=10000
Timeall=100001
delta_tamp=1
N_tamp=round((Timeall-begintime)/delta_tamp)

if Per==1 or Per==5 or Per==15:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_wall_-%.3f/tdp43_300.000.trj' %(Per*0.001),'r')
elif Per==0:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_wall_%.2f/tdp43_300.000.trj' %(Per*0.001),'r')
else:
    f=open('/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/trj/tdp43_wall_-%.2f/tdp43_300.000.trj' %(Per*0.001),'r')
line=f.readlines()
Lmax=len(line)

r_all=np.zeros([N_tamp,N_atoms,3])

for i in range(N_tamp):
    for j in range(N_atoms):
        sss=line[round(i*delta_tamp)*N_one+9+j].split()

        index=float(sss[0])
       
        r_all[i][round(index-1)][0]=float(sss[2])
        r_all[i][round(index-1)][1]=float(sss[3])
        r_all[i][round(index-1)][2]=float(sss[4])

mlist=[]
for i in range(148):
    for j in range(20):
        if Saa[j]==AAsequence[i]:
            jst=j
    mlist.append(Mass[jst])

Rc=np.zeros([2,N_tamp,3])
for i in range(N_tamp):
    Rc[0][i][0]=(np.sum(r_all[i,0:148,0]*mlist))/np.sum(mlist)
    Rc[0][i][1]=(np.sum(r_all[i,0:148,1]*mlist))/np.sum(mlist)
    Rc[0][i][2]=(np.sum(r_all[i,0:148,2]*mlist))/np.sum(mlist)

    Rc[1][i][0]=(np.sum(r_all[i,148:296,0]*mlist))/np.sum(mlist)
    Rc[1][i][1]=(np.sum(r_all[i,148:296,1]*mlist))/np.sum(mlist)
    Rc[1][i][2]=(np.sum(r_all[i,148:296,2]*mlist))/np.sum(mlist)

d_bin=0.05
N_bins=math.ceil(15/d_bin)
p_r=np.zeros([N_bins])
rou_r=np.zeros([N_bins])

for i in range(N_tamp):

    d=0.1*0.5*math.sqrt((Rc[0][i][0]-Rc[1][i][0])**2+(Rc[0][i][1]-Rc[1][i][1])**2+(Rc[0][i][2]-Rc[1][i][2])**2)
    p_r[math.floor(d/d_bin)]+=2
    rou_r[math.floor(d/d_bin)]+=2/(4*math.pi*((i+0.5)*d_bin)**2*d_bin)

# cut_r=4
cut_r=6
# for i in range(5,N_bins-5):
#     k,b=op.curve_fit(f_x,d_bin*np.arange(i-5,i+5),rou_r[i-5:i+5])[0]
#     if i>2/d_bin and -0.0001<k<0.0001:
#         cut_r=i*d_bin
#         break

N_cut=math.ceil(cut_r/d_bin)

g_r=rou_r/np.mean(rou_r[N_cut-10:N_cut+10])

B22=0
for i in range(N_cut):
    B22+=(1-g_r[i])*((i+0.5)*d_bin)**2*d_bin

np.savetxt('B22_%d.txt' %Per, np.c_[B22],fmt='%f',delimiter='\t')
np.save(file="p_r_%d.npy" %(Per), arr=p_r)
np.save(file="rou_r_%d.npy" %(Per), arr=rou_r)
np.save(file="g_r_%d.npy" %(Per), arr=g_r)