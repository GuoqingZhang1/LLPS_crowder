import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Saa=['A','D','E','F','G','I','K','L','M','N','P','Q','R','S','W','Y']

Na=len(Saa)

Per_0=0
BOX=15*15*50
N_PEG_0=round(BOX*Per_0*0.01/(4*math.pi*0.8**3/3))
N_atoms_0=14800+N_PEG_0
N_one_0=N_atoms_0+9

begintime=10000
Timeall=50001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

f=open('../Crowd_%d/Distance_%d.txt' %(0,0),'r')
line=f.readlines()

Matric_0=np.zeros([N_atoms_0,N_atoms_0])
for i in range(N_atoms_0):
    ss=line[i].split()
    for j in range(N_atoms_0):
        Matric_0[i][j]=float(ss[j])/N_tamp

Inter_0=np.zeros([Na,Na])
Intra_0=np.zeros([Na,Na])
Inter_res_0=np.zeros([Na])
Intra_res_0=np.zeros([Na])

for i in range(100):
    for j in range(145):
        for k in range(j+3,148):
            for n in range(Na):
                if AAsequence[j]==Saa[n]:
                    ni=n
                if AAsequence[k]==Saa[n]:
                    nj=n
            Intra_0[ni][nj]=Intra_0[ni][nj]+Matric_0[i*148+j][i*148+k]/100
            Intra_0[nj][ni]=Intra_0[nj][ni]+Matric_0[i*148+k][i*148+j]/100

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                for l in range(Na):
                    if AAsequence[j]==Saa[l]:
                        ni=l
                    if AAsequence[n]==Saa[l]:
                        nj=l
                Inter_0[ni][nj]=Inter_0[ni][nj]+Matric_0[i*148+j][m*148+n]/100

for i in range(Na):
    Inter_res_0[i]=np.sum(Inter_0[i,:])
    Intra_res_0[i]=np.sum(Intra_0[i,:])

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9


f=open('Distance_%d.txt' %(Per),'r')
line=f.readlines()

Matric=np.zeros([N_atoms,N_atoms])
for i in range(N_atoms):
    ss=line[i].split()
    for j in range(N_atoms):
        Matric[i][j]=float(ss[j])/N_tamp

Inter=np.zeros([Na,Na])
Intra=np.zeros([Na,Na])
Inter_res=np.zeros([Na])
Intra_res=np.zeros([Na])
Cow=np.zeros([Na])

for i in range(100):
    for j in range(145):
        for k in range(j+3,148):
            for n in range(Na):
                if AAsequence[j]==Saa[n]:
                    ni=n
                if AAsequence[k]==Saa[n]:
                    nj=n
            Intra[ni][nj]=Intra[ni][nj]+Matric[i*148+j][i*148+k]/100
            Intra[nj][ni]=Intra[nj][ni]+Matric[i*148+k][i*148+j]/100

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                for l in range(Na):
                    if AAsequence[j]==Saa[l]:
                        ni=l
                    if AAsequence[n]==Saa[l]:
                        nj=l
                Inter[ni][nj]=Inter[ni][nj]+Matric[i*148+j][m*148+n]/100

for i in range(100):
    for j in range(148):
        for n in range(Na):
            if Saa[n]==AAsequence[j]:
                ni=n
            for k in range(14800,N_atoms):
                Cow[ni]=Cow[ni]+(Matric[i*148+j][k]+Matric[k][i*148+j])/200

for i in range(Na):
    Inter_res[i]=np.sum(Inter[i,:])
    Intra_res[i]=np.sum(Intra[i,:])


fig=plt.figure(figsize=(8,6),dpi=1000)
plt.bar(np.arange(Na),Inter_res-Inter_res_0)
plt.xlabel('Residues',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(u'$\mathregular{N_{residues}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(np.arange(Na),Saa,fontproperties='Arial',fontsize=26)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-1,Na)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,6)
plt.savefig('Inter_res_delta_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig=plt.figure(figsize=(8,6),dpi=1000)
plt.bar(np.arange(Na),Intra_res-Intra_res_0)
plt.xlabel('Residues',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(u'$\mathregular{N_{residues}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(np.arange(Na),Saa,fontproperties='Arial',fontsize=26)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-1,Na)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,6)
plt.savefig('Intra_res_delta_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Inter-Inter_0,cmap='BrBG',origin='lower')

cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([0.00001,0.0001,0.001,0.01,0.1])
# cb5.locator = tick_locator
im5.set_clim(-5,5)
cb5.update_ticks()
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues',fontsize=30)
plt.ylabel('Residues',fontsize=30)
plt.xticks(np.arange(Na),labels=Saa,size=24)
plt.yticks(np.arange(Na),labels=Saa,size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Inter_res_map_delta_%d.png' %(Per))
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Intra-Intra_0,cmap='BrBG',origin='lower')
cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([0.00001,0.0001,0.001,0.01,0.1])
# cb5.locator = tick_locator
im5.set_clim(-1,1)
cb5.update_ticks()
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues',fontsize=30)
plt.ylabel('Residues',fontsize=30)
plt.xticks(np.arange(Na),labels=Saa,size=24)
plt.yticks(np.arange(Na),labels=Saa,
           size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Intra_res_map_delta_%d.png' %(Per))
plt.close()
