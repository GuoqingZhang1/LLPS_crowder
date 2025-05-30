import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.ticker as ticker
from matplotlib.colors import LogNorm
from scipy import optimize as op

def f(x,k,b):
    return k*x+b


Per=0
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=50001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Crowd_0/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

# N_inter_llps=np.load(file="N_inter_llps_%d.npy" %(Per))

Inter0_llps=np.zeros([148,148])
Intra0_llps=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter_llps=np.zeros([148,148])

for i in range(100):  
    for j in range(145):
        for k in range(j+3,148):
            Intra0_llps[j][k]=Intra0_llps[j][k]+Matric[i*148+j][i*148+k]/(N_tamp*100)
            Intra0_llps[k][j]=Intra0_llps[k][j]+Matric[i*148+k][i*148+j]/(N_tamp*100)

for i in range(100):
    for j in range(148):
        for m in range(100):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter_llps[j][n]+=1
                    Inter0_llps[j][n]=Inter0_llps[j][n]+Matric[i*148+j][m*148+n]/(N_tamp*100)

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

Per=0
BOX=25*25*25
N_PEG=int(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=148+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Single/Distance_%d.npy" %(Per))
# Matric=Matric/N_ta
Intra0=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(1):  
    for j in range(145):
        for k in range(j+3,148):
            Intra0[j][k]=Intra0[j][k]+Matric[i*148+j][i*148+k]/(N_tamp)
            Intra0[k][j]=Intra0[k][j]+Matric[i*148+k][i*148+j]/(N_tamp)


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

Per=0
BOX=12.5*12.5*12.5
N_PEG=int(BOX*Per*0.01/(0.8**3))
N_atoms=148*2+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=100001
delta_tamp=10
N_tamp=round((Timeall-begintime)/delta_tamp)

Matric=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Double/Distance_%d.npy" %(Per))
# Matric=Matric/N_tamp

Inter0=np.zeros([148,148])

Cow=np.zeros([148])

# N_inter=np.zeros([148,148])

for i in range(2):
    for j in range(148):
        for m in range(2):
            for n in range(148):
                if i!=m:
                    # if Matric[i*148+j][m*148+n]>0:
                    #     N_inter[j][n]+=1
                    Inter0[j][n]=Inter0[j][n]+Matric[i*148+j][m*148+n]/(N_tamp)

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

Inter_index_llps=np.zeros([len(Inter_llps)])
Inter0_index_llps=np.zeros([len(Inter_llps)])
Inter_index=np.zeros([len(Inter_llps)])
Inter0_index=np.zeros([len(Inter_llps)])

for i in range(len(Inter_llps)):
    Inter_index_llps[i]=np.sum(Inter_llps[i])
    Inter0_index_llps[i]=np.sum(Inter0_llps[i])
    Inter_index[i]=np.sum(Inter[i])
    Inter0_index[i]=np.sum(Inter0[i])

x=Inter_index_llps-Inter0_index_llps
y=Inter_index-Inter0_index

x=x.reshape(-1,1)

fig=plt.figure(figsize=(8,6),dpi=1000)

plt.scatter(x,y,s=200)

model1=LinearRegression()
model1.fit(x,y)

MSE1=mean_squared_error(y, model1.predict(x))

np.savetxt('MSE_inter_%d.txt' %(Per), np.c_[MSE1],fmt='%f',delimiter='\t')

k1=model1.coef_[0]
b1=model1.intercept_

xx=np.arange(0.9*np.min(x),1.1*np.max(x),0.01)
plt.plot(xx,f(xx,k1,b1),color='black',linestyle='--',linewidth=3.0,zorder=1)

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

# plt.xlim(-0.062,0.002)
# plt.ylim(-0.0052,0.0012)
plt.xticks(fontproperties="Arial",size=36)
plt.yticks(fontproperties="Arial",size=36)

plt.xlabel(chr(916)+'$\mathregular{N_{ij}}$ (LLPS)',size=40,labelpad=10,fontproperties="Arial")  
plt.ylabel(chr(916)+'$\mathregular{N_{ij}}$ (Dimer)',size=40,labelpad=10,fontproperties="Arial")

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
# plt.tick_params(length=5,pad=10,which='minor',width = 2,direction='in')

fig.set_size_inches(8,6)
plt.savefig('Qij_vs_Qij_delta_Inter.png',dpi=1000,bbox_inches='tight')

Intra_index_llps=np.zeros([len(Intra_llps)])
Intra0_index_llps=np.zeros([len(Intra_llps)])
Intra_index=np.zeros([len(Intra_llps)])
Intra0_index=np.zeros([len(Intra_llps)])

for i in range(len(Intra_llps)):
    Intra_index_llps[i]=np.sum(Intra_llps[i])
    Intra0_index_llps[i]=np.sum(Intra0_llps[i])
    Intra_index[i]=np.sum(Intra[i])
    Intra0_index[i]=np.sum(Intra0[i])

x=Intra_index_llps-Intra0_index_llps
y=Intra_index-Intra0_index

x=x.reshape(-1,1)

fig=plt.figure(figsize=(8,6),dpi=1000)

plt.scatter(x,y,s=200)

model2=LinearRegression()
model2.fit(x,y)

MSE2=mean_squared_error(y, model2.predict(x))

np.savetxt('MSE_intra_%d.txt' %(Per), np.c_[MSE2],fmt='%f',delimiter='\t')

k2=model2.coef_[0]
b2=model2.intercept_

xx=np.arange(0.9*np.min(x),1.1*np.max(x),0.01)
plt.plot(xx,f(xx,k2,b2),color='black',linestyle='--',linewidth=3.0,zorder=1)

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

# plt.xlim(-0.4,0.4)
# plt.ylim(-0.03,0.03)

plt.xticks(fontproperties="Arial",size=36)
plt.yticks(fontproperties="Arial",size=36)

plt.xlabel(chr(916)+'$\mathregular{N_{ij}}$ (LLPS)',size=40,labelpad=10,fontproperties="Arial")  
plt.ylabel(chr(916)+'$\mathregular{N_{ij}}$ (Single)',size=40,labelpad=10,fontproperties="Arial")

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
# plt.tick_params(length=5,pad=10,which='minor',width = 2,direction='in')

fig.set_size_inches(8,6)
plt.savefig('Qij_vs_Qij_delta_Intra.png',dpi=1000,bbox_inches='tight')
