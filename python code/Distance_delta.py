import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
import matplotlib.colors as mcolors

Per_0=0
BOX=15*15*50
N_PEG_0=round(BOX*Per_0*0.01/(4*math.pi*0.8**3/3))
N_atoms_0=14800+N_PEG_0
N_one_0=N_atoms_0+9

begintime=10000
Timeall=50001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

f_0=open('../Crowd_%d/Distance_%d.txt' %(0,0),'r')
line_0=f_0.readlines()

Matric_0=np.zeros([N_atoms_0,N_atoms_0])
for i in range(N_atoms_0):
    ss=line_0[i].split()
    for j in range(N_atoms_0):
        Matric_0[i][j]=float(ss[j])/N_tamp

Inter_0=np.zeros([148,148])
Intra_0=np.zeros([148,148])
Inter_index_0=np.zeros([148])
Intra_index_0=np.zeros([148])


for i in range(100):
    for j in range(145):
        for k in range(j+3,148):
            Intra_0[j][k]=Intra_0[j][k]+Matric_0[i*148+j][i*148+k]/100
            Intra_0[k][j]=Intra_0[k][j]+Matric_0[i*148+k][i*148+j]/100

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    Inter_0[j][n]=Inter_0[j][n]+Matric_0[i*148+j][m*148+n]/100



for i in range(148):
    Inter_index_0[i]=np.sum(Inter_0[i,:])
    Intra_index_0[i]=np.sum(Intra_0[i,:])


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

Inter=np.zeros([148,148])
Intra=np.zeros([148,148])
Inter_index=np.zeros([148])
Intra_index=np.zeros([148])
Cow=np.zeros([148])

for i in range(100):
    for j in range(145):
        for k in range(j+3,148):
            Intra[j][k]=Intra[j][k]+Matric[i*148+j][i*148+k]/100
            Intra[k][j]=Intra[k][j]+Matric[i*148+k][i*148+j]/100

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    Inter[j][n]=Inter[j][n]+Matric[i*148+j][m*148+n]/100

for i in range(100):
    for j in range(148):
        for k in range(14800,N_atoms):
            Cow[j]=Cow[j]+(Matric[i*148+j][k]+Matric[k][i*148+j])/200

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
plt.yticks([-4.0,-2.0,0.0],fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 2 #边框宽度设置为2
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
plt.ylabel(chr(916)+u'$\mathregular{_{N_{c}}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,49,99,147],['1','50','100','148'],fontproperties='Arial',fontsize=36)
plt.yticks([-0.4,-0.2,0.0],fontproperties='Arial',fontsize=36)
# plt.ylim(0,0.0002)
plt.xlim(-2,150)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 2 #边框宽度设置为2
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
norm = SymLogNorm(linthresh=0.001, base=10)

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

im5.set_clim(-0.1,0.1)
cb5.set_ticks([-0.1,-0.01,-0.001,0,0.001,0.01,0.1])

# cb5.formatter = ticker.ScalarFormatter(useMathText=True)
# cb5.formatter.set_powerlimits((0,10))  # 设置科学计数法的范围
# cb5.update_ticks()  # 更新刻度

plt.xlabel('Residues index',fontsize=30)
plt.ylabel('Residues index',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],size=24)
fig5.savefig('Inter_map_delta_%d.png' %(Per))
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
norm = SymLogNorm(linthresh=0.001, base=10)

ax5 = fig5.gca()
im5 = ax5.imshow(Intra-Intra_0,cmap='BrBG',origin='lower',norm=norm)
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

im5.set_clim(-0.01,0.01)
cb5.set_ticks([-0.01,-0.001,0,0.001,0.01])
# cb5.formatter = ticker.ScalarFormatter(useMathText=True)
# cb5.formatter.set_powerlimits((0,10))  # 设置科学计数法的范围
# cb5.update_ticks()  # 更新刻度

plt.xlabel('Residues index',fontsize=30)
plt.ylabel('Residues index',fontsize=30)
plt.xticks([0,49,99,147],labels=['1','50','100','148'],size=24)
plt.yticks([0,49,99,147],labels=['1','50','100','148'],size=24)

fig5.savefig('Intra_map_delta_%d.png' %(Per))
plt.close()
