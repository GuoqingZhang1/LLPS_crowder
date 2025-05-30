import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
from scipy import optimize as op

def y(x,k,b):
    return k*x+b

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=50001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

# N_inter_llps=np.load(file="N_inter_llps_%d.npy" %(Per))

Inter_llps=np.zeros([148,148])
Intra_llps=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter_llps=np.zeros([148,148])

for i in range(100):  
    for j in range(145):
        for k in range(j+3,148):
            Intra_llps[j][k]=Intra_llps[j][k]+Matric[i*148+j][i*148+k]/(N_tamp*100)
            Intra_llps[k][j]=Intra_llps[k][j]+Matric[i*148+k][i*148+j]/(N_tamp*100)

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter_llps[j][n]+=1
                    Inter_llps[j][n]=Inter_llps[j][n]+Matric[i*148+j][m*148+n]/(N_tamp*100)

#single

Per=PERCENT
BOX=25*25*25
N_PEG=int(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=148+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="../Single/Distance_%d.npy" %(Per))
# Matric=Matric/N_ta
Intra=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(1):  
    for j in range(145):
        for k in range(j+3,148):
            Intra[j][k]=Intra[j][k]+Matric[i*148+j][i*148+k]/(N_tamp)
            Intra[k][j]=Intra[k][j]+Matric[i*148+k][i*148+j]/(N_tamp)


#double

Per=PERCENT
BOX=12.5*12.5*12.5
N_PEG=int(BOX*Per*0.01/(0.8**3))
N_atoms=148*2+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="../Double/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

Inter=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter[j][n]=Inter[j][n]+Matric[i*148+j][m*148+n]/(N_tamp)


fig=plt.figure(figsize=(8,6),dpi=1000)



plt.scatter(Inter_llps.ravel(),Inter.ravel(),s=200)

k,b=op.curve_fit(y,Inter_llps.ravel(),Inter.ravel())[0]

xx=np.arange(0.0,0.24,0.001)
plt.plot(xx,(y(xx,k,b)),color='black',linestyle='--',linewidth=3.0,zorder=1)

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

# plt.xscale('log')
# plt.yscale('log')

font_properties = {
    'fontsize': 36,
    
    'fontname': 'Arial'
}

plt.xlim(0.0,0.16)
plt.ylim(0.0,0.004)
plt.xticks([0.00,0.08,0.16],fontproperties="Arial",size=36)
plt.yticks([0.000,0.002,0.004],fontproperties="Arial",size=36)

plt.xlabel('$\mathregular{N_{ij}}$ (LLPS)',size=40,labelpad=10,fontproperties="Arial")  
plt.ylabel('$\mathregular{N_{ij}}$ (Dimer)',size=40,labelpad=10,fontproperties="Arial")

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
# plt.tick_params(length=5,pad=10,which='minor',width = 2,direction='in')

fig.set_size_inches(8,6)
plt.savefig('Qij_vs_Qij_Inter.png',dpi=1000,bbox_inches='tight')




fig=plt.figure(figsize=(8,6),dpi=1000)

plt.scatter(Intra_llps.ravel(),Intra.ravel(),s=200)

k,b=op.curve_fit(y,Intra_llps.ravel(),Intra.ravel())[0]

xx=np.arange(-0.02,1.02,0.01)
plt.plot(xx,(y(xx,k,b)),color='black',linestyle='--',linewidth=3.0,zorder=1)

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

# plt.xscale('log')
# plt.yscale('log')

font_properties = {
    'fontsize': 36,
    
    'fontname': 'Arial'
}

plt.xlim(-0.02,1.02)
plt.ylim(-0.02,1.02)
plt.xticks([0.0,0.2,0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)
plt.yticks([0.0,    0.2,0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)

plt.xlabel('$\mathregular{N_{ij}}$ (LLPS)',size=40,labelpad=10,fontproperties="Arial")  
plt.ylabel('$\mathregular{N_{ij}}$ (Single)',size=40,labelpad=10,fontproperties="Arial")

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
# plt.tick_params(length=5,pad=10,which='minor',width = 2,direction='in')

fig.set_size_inches(8,6)
plt.savefig('Qij_vs_Qij_Intra.png',dpi=1000,bbox_inches='tight')
