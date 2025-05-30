import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
from scipy import optimize as op
from matplotlib.ticker import ScalarFormatter

begintime=10000
totaltime=50001
totalline=500

def y(x,k,b):
    return k*x+b

typeCro='2'

fig=plt.figure(figsize=(8,6),dpi=1000)

B22=np.zeros([7])
rou=[]
rou_std=[]
MSD=[]
MSD_std=[]
for Per in [0,5,10,15,20,25,30]:

    f_MSD=open('../Crowd_%d/alpha_fitting.txt' %(Per),'r')
    line_MSD=f_MSD.readlines()

    D=[]
    for i in range(10):
        D0=0
        for j in range(10):
            D0+=float(line_MSD[i*10+j])/10
        D.append(D0)

    MSD.append(np.mean(D))
    MSD_std.append(np.std(D))

    f=open('../Crowd_%d/rou_high.txt' %(Per),'r')
    line=f.readlines()

    rou.append(float(line[0]))
    rou_std.append(float(line[1]))

    f.close()


if typeCro=='1':
    cmap1=plt.get_cmap('Reds',8)
elif typeCro=='2':
    cmap1=plt.get_cmap('Blues',8)
for i in range(7):
    plt.errorbar(MSD[i],rou[i], xerr=MSD_std[i], yerr=rou_std[i], fmt='o',mfc=cmap1((5*i+5)/40),mec='black',mew=2,elinewidth=2, ecolor='black',capthick=12, capsize=8,markersize=16,zorder=2)

k,b=op.curve_fit(y,MSD,rou)[0]


xx=np.arange(-0.2,8.2,0.1)
plt.plot(xx,y(xx,k,b),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)

if typeCro=='1':
    plt.ylim(0.92,1.02)
    plt.xlim(0.62,0.68)
    plt.yticks([0.93,0.96,0.99,1.02],fontproperties="Arial",size=36)
    plt.xticks([0.62,0.64,0.66,0.68],fontproperties="Arial",size=36)
elif typeCro=='2':
    plt.xlim(0.6,0.9)
    plt.ylim(0.35,1.0)
    plt.yticks([0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)
    plt.xticks([0.6,0.7,0.8,0.9],fontproperties="Arial",size=36)


plt.ylabel(chr(961)+'$\mathregular{_{h}}$'+" (g/cm"+'$\mathregular{^3}$)',size=40,labelpad=10,fontproperties="Arial")
plt.xlabel(chr(945),size=40,labelpad=10,fontproperties="Arial")  

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
plt.tick_params(length=5,which='minor',width = 2,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black',shadow=True)

fig.set_size_inches(8,6)
plt.savefig('Alpha_vs_rou_high.png',dpi=1000,bbox_inches='tight')