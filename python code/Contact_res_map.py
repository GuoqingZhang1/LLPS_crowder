import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Saa=['A','D','E','F','G','I','K','L','M','N','P','Q','R','S','W','Y']

Na=len(Saa)

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))

f_inter=open('Inter_map.txt' ,"r" )
line_inter = f_inter.readlines() # 以行的形式进行读取文件
Lmax = len(line_inter)

f_intra=open('Intra_map.txt' ,"r" )
line_intra = f_intra.readlines() # 以行的形式进行读取文件
Lmax = len(line_intra)

f_cow=open('Crowd_map.txt','r')
line_cow = f_cow.readlines() # 以行的形式进行读取文件
Lmax = len(line_cow)

begintime=10000
Timeall=50001
delta_tamp=1000
N_tamp=round((Timeall-begintime)/delta_tamp)

Inter=np.zeros([Na,Na])
Intra=np.zeros([Na,Na])
Inter_res=np.zeros([Na])
Intra_res=np.zeros([Na])
Cow=np.zeros([Na])
for i in range(Lmax):
    sx1=line_inter[i].split()
    
    sx3=line_cow[i].split()
    for j in range(Lmax):
        for n in range(Na):
 
            if Saa[n]==AAsequence[i]:
                xi=n
            if Saa[n]==AAsequence[j]:
                yj=n
        Inter[xi][yj]=Inter[xi][yj]+float(sx1[j])/(100*N_tamp)
        Inter_res[xi]=Inter_res[xi]+float(sx1[j])/(100*N_tamp)
    if Per!=0:
        Cow[xi]=float(sx3[0])/(N_PEG*100*N_tamp)

for i in range(Lmax-3):
    sx2=line_intra[i].split()
    for k in range(i+3,Lmax):
        for n in range(Na):

            if Saa[n]==AAsequence[i]:
                xi=n
            if Saa[n]==AAsequence[k]:
                yj=n
        Intra[xi][yj]=Intra[xi][yj]+float(sx2[k])/(100*N_tamp)
        Intra[yj][xi]=Intra[yj][xi]+float(sx2[k])/(100*N_tamp)

        Intra_res[xi]=Intra_res[xi]+float(sx2[k])/(100*N_tamp)
        Intra_res[yj]=Intra_res[yj]+float(sx2[k])/(100*N_tamp)

fig=plt.figure(figsize=(8,6),dpi=1000)
plt.bar(np.arange(Na),Inter_res)
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
plt.savefig('Inter_res_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig=plt.figure(figsize=(8,6),dpi=1000)
plt.bar(np.arange(Na),Intra_res)
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
plt.savefig('Intra_res_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Inter,cmap='hot_r',origin='lower')

cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([0.00001,0.0001,0.001,0.01,0.1])
# cb5.locator = tick_locator
# im5.set_clim(0,20)
cb5.update_ticks()
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues',fontsize=30)
plt.ylabel('Residues',fontsize=30)
plt.xticks(np.arange(Na),labels=Saa,size=24)
plt.yticks(np.arange(Na),labels=Saa,size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Inter_res_map_%d.png' %(Per))
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Intra,cmap='hot_r',origin='lower')
cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

# tick_locator = ticker.MaxNLocator(nbins=5)
# cb5.set_ticks([0.00001,0.0001,0.001,0.01,0.1])
# cb5.locator = tick_locator
cb5.update_ticks()
# plt.title(r'$U_{LJ}$',fontsize=32)
plt.xlabel('Residues',fontsize=30)
plt.ylabel('Residues',fontsize=30)
plt.xticks(np.arange(Na),labels=Saa,size=24)
plt.yticks(np.arange(Na),labels=Saa,
           size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Intra_res_map_%d.png' %(Per))
plt.close()

fig=plt.figure(figsize=(8,6),dpi=1000)
plt.bar(np.arange(Na),Cow)
plt.xlabel('Residues',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(u'$\mathregular{N_{residues}}$',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(np.arange(Na),Saa,fontproperties='Arial',fontsize=26)
plt.yticks([0,0.00005,0.0001,0.00015,0.0002],fontproperties='Arial',fontsize=36)
plt.ylim(0,0.0002)
plt.xlim(-1,Na)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,6)
plt.savefig('Cow_res_%d.png' %(Per),dpi=1000,bbox_inches='tight')
plt.close()