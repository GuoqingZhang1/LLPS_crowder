import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math

# f=open('tdp43_300.000.trj','r')
# line=f.readlines()
# Lmax=len(line)


# f_z0=open('Center.txt','r')
# line_z0=f_z0.readlines()

Per=PERCENT
BOX=25*25*25

N_PEG=int(BOX*(Per)/(4*math.pi*0.8**3/3))

N_atoms=148+N_PEG
if Per==0.15:
    N_atoms=1237
N_one=N_atoms+9

begin=10000
Timeall=90000


f_pro=open('Rdf_pro.txt','r')
line_pro=f_pro.readlines()

rou_pro=np.zeros([1250])

f_cro=open('Rdf_cro.txt','r')
line_cro=f_cro.readlines()

rou_cro=np.zeros([1250])

n_pro=np.zeros([1250])
n_cro=np.zeros([1250])


for i in range(begin,Timeall):
    for j in range(1250):
        ss1=line_pro[1251*i+j+4].split()
        ss2=line_cro[1251*i+j+4].split()

        n_pro[j]=n_pro[j]+float(ss1[2])/(Timeall-begin)
        n_cro[j]=n_cro[j]+float(ss2[2])/(Timeall-begin)
    
        rou_pro[j]=rou_pro[j]+float(ss1[2])/(0.01*(0.01*j+0.005)**2*(Timeall-begin))
        rou_cro[j]=rou_cro[j]+float(ss2[2])/(0.01*(0.01*j+0.005)**2*(Timeall-begin))
    
n_size=10
n_bins=round(1250/n_size)
rou_n_pro=[]
rou_n_cro=[]
for i in range(n_bins):
    rou_n_pro.append(np.mean(rou_pro[n_size*i:n_size*(i+1)]))
    rou_n_cro.append(np.mean(rou_cro[n_size*i:n_size*(i+1)]))
# rou_pro=rou_pro/rou_pro[249]
# rou_cro=rou_cro

f_Rg=open('../../../Expand/Single/Rg_llps_%d.txt' %(-Per*1000),'r')
line_Rg=f_Rg.readlines()

Rg=[]

for i in range(len(line_Rg)):
    Rg.append(float(line_Rg[i]))

cut_Rg=round(np.mean(Rg))

sig=(8+3.82/2)*10

N_in=0 
N_out=0

for i in range(cut_Rg+200):
    if i<cut_Rg:
        N_in=N_in+n_cro[i]
    elif cut_Rg<i<cut_Rg+1.5*sig:
        N_out=N_out+n_cro[i]

np.savetxt('N_in_out.txt',[N_in,N_out])

# np.savetxt('N_r_cro.txt',[rou_n_cro])

fig,ax=plt.subplots(figsize=(8,6),dpi=1000)

# plt.plot(0.005+np.arange(0,12.49,0.01),rou_pro,label='IDR',linewidth=4.0)
plt.plot(np.arange(0,12.5,0.01*n_size),rou_n_cro,label='PEG',linewidth=4.0)
plt.axvline(x=0.1*np.mean(Rg),color='red', linestyle='--',linewidth=4.0)
plt.xlabel("r (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+' (nm'+'$\mathregular{^{-3}}$)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks([0,4,8,12],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  
plt.xlim(0,12)
plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
plt.ylim(0,4)
# plt.yscale('log')
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24

fig.set_size_inches(8,6)
plt.savefig('Rdf_single_%f.png' %(Per),bbox_inches='tight',dpi=1000)