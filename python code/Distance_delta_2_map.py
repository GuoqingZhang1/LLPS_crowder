import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)


Matric_single_0=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Single/Distance_%d.npy" %(0))
# Matric=Matric/N_tamp


Intra_single_0=np.zeros([148,148])

Intra_index_single_0=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(1):  
    for j in range(145):
        for k in range(j+3,148):
            Intra_single_0[j][k]=Intra_single_0[j][k]+Matric_single_0[i*148+j][i*148+k]/(N_tamp)
            Intra_single_0[k][j]=Intra_single_0[k][j]+Matric_single_0[i*148+k][i*148+j]/(N_tamp)


# Inter=Inter/np.mean(N_inter)

for i in range(148):
    
    Intra_index_single_0[i]=np.sum(Intra_single_0[i,:])



Matric_single=np.load(file="../Single/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp


Intra_single=np.zeros([148,148])

Intra_index_single=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(1):  
    for j in range(145):
        for k in range(j+3,148):
            Intra_single[j][k]=Intra_single[j][k]+Matric_single[i*148+j][i*148+k]/(N_tamp)
            Intra_single[k][j]=Intra_single[k][j]+Matric_single[i*148+k][i*148+j]/(N_tamp)


# Inter=Inter/np.mean(N_inter)

for i in range(148):
    
    Intra_index_single[i]=np.sum(Intra_single[i,:])

Matric_double_0=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Double/Distance_%d.npy" %(0))
# Matric=Matric/N_tamp

Inter_double_0=np.zeros([148,148])

Inter_index_double_0=np.zeros([148])

# N_inter=np.zeros([148,148])


for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter_double_0[j][n]=Inter_double_0[j][n]+Matric_double_0[i*148+j][m*148+n]/(N_tamp)


# Inter=Inter/np.mean(N_inter)

for i in range(148):
    Inter_index_double_0[i]=np.sum(Inter_double_0[i,:])



Matric_double=np.load(file="../Double/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

Inter_double=np.zeros([148,148])

Inter_index_double=np.zeros([148])

# N_inter=np.zeros([148,148])


for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter_double[j][n]=Inter_double[j][n]+Matric_double[i*148+j][m*148+n]/(N_tamp)


# Inter=Inter/np.mean(N_inter)

for i in range(148):
    Inter_index_double[i]=np.sum(Inter_double[i,:])



begintime=10000
Timeall=50001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric_0=np.load(file="../Crowd_0/Distance_%d.npy" %(0))
# Matric=Matric/N_tamp

# N_inter=np.load(file="N_inter_%d.npy" %(Per))

Inter_0=np.zeros([148,148])
Intra_0=np.zeros([148,148])
Inter_index_0=np.zeros([148])
Intra_index_0=np.zeros([148])
Cow_0=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(100):  
    for j in range(145):
        for k in range(j+3,148):
            Intra_0[j][k]=Intra_0[j][k]+Matric_0[i*148+j][i*148+k]/(N_tamp*100)
            Intra_0[k][j]=Intra_0[k][j]+Matric_0[i*148+k][i*148+j]/(N_tamp*100)

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter_0[j][n]=Inter_0[j][n]+Matric_0[i*148+j][m*148+n]/(N_tamp*100)


# Inter=Inter/np.mean(N_inter)

for i in range(148):
    Inter_index_0[i]=np.sum(Inter_0[i,:])
    Intra_index_0[i]=np.sum(Intra_0[i,:])



Matric=np.load(file="Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

# N_inter=np.load(file="N_inter_%d.npy" %(Per))

Inter=np.zeros([148,148])
Intra=np.zeros([148,148])
Inter_index=np.zeros([148])
Intra_index=np.zeros([148])
Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(100):  
    for j in range(145):
        for k in range(j+3,148):
            Intra[j][k]=Intra[j][k]+Matric[i*148+j][i*148+k]/(N_tamp*100)
            Intra[k][j]=Intra[k][j]+Matric[i*148+k][i*148+j]/(N_tamp*100)

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter[j][n]=Inter[j][n]+Matric[i*148+j][m*148+n]/(N_tamp*100)

for i in range(100):
    for j in range(148):
        for k in range(14800,N_atoms):
            Cow[j]=Cow[j]+(Matric[i*148+j][k]+Matric[k][i*148+j])/200

# Inter=Inter/np.mean(N_inter)

for i in range(148):
    Inter_index[i]=np.sum(Inter[i,:])
    Intra_index[i]=np.sum(Intra[i,:])

Inter_2=np.zeros([148,148])

Inter_2=Inter_double-Inter_double_0
for i in range(148):
    for j in range(148):
        if j>i:
            Inter_2[i][j]=Inter[i][j]-Inter_0[i][j]

fig5 = plt.figure(figsize=(8,6),dpi=1000)

plt.rcParams['font.size'] = 20
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# 定义自定义的对数归一化
class SymLogNorm(mcolors.SymLogNorm):
    def __init__(self, linthresh, linscale=1.0, base=10, vmin=None, vmax=None, clip=False):
        super().__init__(linthresh, linscale=linscale, base=base, vmin=vmin, vmax=vmax, clip=clip)
        
# 使用SymLogNorm进行绘图
norm = SymLogNorm(linthresh=0.001, base=10)

ax5 = fig5.gca()
im5 = ax5.imshow(Inter_2,cmap='BrBG',origin='lower',norm=norm)

cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

bwith = 1.5 #边框宽度设置为2
cb5.ax.spines['bottom'].set_linewidth(bwith)
cb5.ax.spines['left'].set_linewidth(bwith)
cb5.ax.spines['top'].set_linewidth(bwith)
cb5.ax.spines['right'].set_linewidth(bwith)

# tick_locator = ticker.MaxNLocator(nbins=5)
im5.set_clim(-0.01,0.01)
cb5.set_ticks([-0.01,-0.001,0,0.001,0.01])
# cb5.locator = tick_locator
cb5.update_ticks()

ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.tick_params(length=5,pad=10,width = 1.5,direction='out')
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues index',fontproperties='Arial',fontsize=30)
plt.ylabel('Residues index',fontproperties='Arial',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Delta_Inter_2_map_%d.png' %(Per))
plt.close()

Intra_2=np.zeros([148,148])

Intra_2=Intra_single-Intra_single_0
for i in range(148):
    for j in range(148):
        if j>i:
            Intra_2[i][j]=Intra[i][j]-Intra_0[i][j]

fig5 = plt.figure(figsize=(8,6),dpi=1000)

plt.rcParams['font.size'] = 20
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

ax5 = fig5.gca()
im5 = ax5.imshow(Intra_2,cmap='BrBG',origin='lower',norm=norm)
cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

bwith = 1.5 #边框宽度设置为2
cb5.ax.spines['bottom'].set_linewidth(bwith)
cb5.ax.spines['left'].set_linewidth(bwith)
cb5.ax.spines['top'].set_linewidth(bwith)
cb5.ax.spines['right'].set_linewidth(bwith)

# tick_locator = ticker.MaxNLocator(nbins=5)
im5.set_clim(-0.01,0.01)
cb5.set_ticks([-0.01,-0.001,0,0.001,0.01])
# cb5.locator = tick_locator
cb5.update_ticks()

ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.tick_params(length=5,pad=10,width = 1.5,direction='out')
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues index',fontproperties='Arial',fontsize=30)
plt.ylabel('Residues index',fontproperties='Arial',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Delta_Intra_2_map_%d.png' %(Per))
plt.close()

fig=plt.figure(figsize=(8,2),dpi=1000)
for i in range(148):
    dQ=Inter_index_double[i]-Inter_index_double_0[i]
    if dQ>0:
        color='teal'
    else:
        color='peru'
    plt.bar(i,dQ,color=color)

plt.xlabel('Residues index',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(916)+u'$\mathregular{N_{c}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 2,direction='in')
bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Delta_Inter_index_double_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig=plt.figure(figsize=(8,2),dpi=1000)
for i in range(148):
    dQ=Inter_index[i]-Inter_index_0[i]
    if dQ>0:
        color='teal'
    else:
        color='peru'
    plt.bar(i,dQ,color=color)

plt.xlabel('Residues index',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(916)+u'$\mathregular{N_{c}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 2,direction='in')
bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Delta_Inter_index_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig=plt.figure(figsize=(8,2),dpi=1000)
for i in range(148):
    dQ=Intra_index_single[i]-Intra_index_single_0[i]
    if dQ>0:
        color='teal'
    else:
        color='peru'
    plt.bar(i,dQ,color=color)

plt.xlabel('Residues index',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(916)+u'$\mathregular{N_{c}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 2,direction='in')
bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Delta_Intra_index_single_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig=plt.figure(figsize=(8,2),dpi=1000)
for i in range(148):
    dQ=Intra_index[i]-Intra_index_0[i]
    if dQ>0:
        color='teal'
    else:
        color='peru'
    plt.bar(i,dQ,color=color)
plt.xlabel('Residues index',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(916)+u'$\mathregular{N_{c}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 2,direction='in')
bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Delta_Intra_index_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()