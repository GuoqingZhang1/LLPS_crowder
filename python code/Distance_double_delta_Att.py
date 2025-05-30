import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors

Per=0
BOX=12.5*12.5*12.5
N_PEG=int(BOX*Per*0.01/(0.8**3))
N_atoms=148*2+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)



Matric_0=np.load(file="../../Double/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

N_inter=np.load(file="../../Double/N_inter_%d.npy" %(Per))


Inter_0=np.zeros([148,148])
Intra_0=np.zeros([148,148])
Inter_index_0=np.zeros([148])
Intra_index_0=np.zeros([148])


for i in range(2):
    for j in range(145):
        for k in range(j+3,148):
            Intra_0[j][k]=Intra_0[j][k]+Matric_0[i*148+j][i*148+k]/(N_tamp*2)
            Intra_0[k][j]=Intra_0[k][j]+Matric_0[i*148+k][i*148+j]/(N_tamp*2)

for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    Inter_0[j][n]=Inter_0[j][n]+Matric_0[i*148+j][m*148+n]/(N_tamp)



for i in range(148):
    Inter_index_0[i]=np.sum(Inter_0[i,:])
    Intra_index_0[i]=np.sum(Intra_0[i,:])

Per=PERCENT
BOX=12.5*12.5*12.5
N_PEG=int(BOX*Per*0.01/(0.8**3))
N_atoms=148*2+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)



Matric=np.load(file="Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

N_inter=np.load(file="N_inter_%d.npy" %(Per))

Inter=np.zeros([148,148])
Intra=np.zeros([148,148])
Inter_index=np.zeros([148])
Intra_index=np.zeros([148])
Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(2):  
    for j in range(145):
        for k in range(j+3,148):
            Intra[j][k]=Intra[j][k]+Matric[i*148+j][i*148+k]/(N_tamp*2)
            Intra[k][j]=Intra[k][j]+Matric[i*148+k][i*148+j]/(N_tamp*2)

for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter[j][n]=Inter[j][n]+Matric[i*148+j][m*148+n]/(N_tamp)

for i in range(2):
    for j in range(148):
        for k in range(148*2,N_atoms):
            Cow[j]=Cow[j]+(Matric[i*148+j][k]+Matric[k][i*148+j])/2

# Inter=Inter/np.mean(N_inter)

for i in range(148):
    Inter_index[i]=np.sum(Inter[i,:])
    Intra_index[i]=np.sum(Intra[i,:])



fig=plt.figure(figsize=(8,2),dpi=1000)
for i in range(148):
    dQ=Inter_index[i]-Inter_index_0[i]
    if dQ>0:
        color='teal'
    else:
        color='peru'
    plt.bar(i,dQ,color=color)
plt.xlabel('Residues index',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(916)+u'$\mathregular{_{N_{c}}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks([-0.2,-0.1,0.0],fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Inter_index_delta_%d.png' %(Per),dpi=1000,bbox_inches='tight')
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
plt.ylabel(u'$\mathregular{N_{c}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,2)
plt.savefig('Intra_index_delta_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()




fig5 = plt.figure(figsize=(8,6),dpi=1000)
plt.rcParams['font.size'] = 20
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# 定义自定义的对数归一化
class SymLogNorm(mcolors.SymLogNorm):
    def __init__(self, linthresh, linscale=1.0, base=10, vmin=None, vmax=None, clip=False):
        super().__init__(linthresh, linscale=linscale, base=base, vmin=vmin, vmax=vmax, clip=clip)
        
# 使用SymLogNorm进行绘图
norm = SymLogNorm(linthresh=0.0001, base=10)

ax5 = fig5.gca()
im5 = ax5.imshow(Inter-Inter_0,cmap='BrBG',origin='lower',norm=norm)
cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

bwith = 1.5 #边框宽度设置为2
cb5.ax.spines['bottom'].set_linewidth(bwith)
cb5.ax.spines['left'].set_linewidth(bwith)
cb5.ax.spines['top'].set_linewidth(bwith)
cb5.ax.spines['right'].set_linewidth(bwith)

# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([-1.0,-0.5,0.0,0.5,1.0])
# cb5.locator = tick_locator
 
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.subplots_adjust(bottom=0.2,left=0.2)

ax = plt.gca()#获取边框
# ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.tick_params(length=5,pad=10,width = 1.5,direction='out')

im5.set_clim(-0.001,0.001)
cb5.set_ticks([-0.001,-0.0001,0,0.0001,0.001])
cb5.update_ticks()  # 更新刻度

cb5.ax.yaxis.get_offset_text().set_fontsize(20)

plt.xlabel('Residues index',fontproperties='Arial',fontsize=30)
plt.ylabel('Residues index',fontproperties='Arial',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
fig5.savefig('Inter_map_delta_%d.png' %(Per))
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Intra-Intra_0,cmap='BrBG',origin='lower')
cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)
 
# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([-1.0,-0.5,0.0,0.5,1.0])
# cb5.locator = tick_locator
 
# plt.title(r'$U_{LJ}$',fontsize=32)

plt.subplots_adjust(bottom=0.2,left=0.2)

plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24

im5.set_clim(-0.01,0.01)
cb5.set_ticks([-0.01,-0.005,0,0.005,0.01])
cb5.formatter = ticker.ScalarFormatter(useMathText=True)

cb5.ax.yaxis.get_offset_text().set_fontsize(20)

plt.xlabel('Residues index',fontproperties='Arial',fontsize=30)
plt.ylabel('Residues index',fontproperties='Arial',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],fontproperties='Arial',size=24)

fig5.savefig('Intra_map_delta_%d.png' %(Per))
plt.close()
