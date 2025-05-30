import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵
import math
from scipy import optimize as op
from matplotlib.ticker import NullLocator

begintime=10000
totaltime=50001
totalline=500

def y(x,k,b):
    return k*x+b

nfile='2'
typeCro='2'

N_mean=10

Rg=[]
Rg_std=[]
rou=[]
rou_std=[]
rou_fitting=[]
for Per in [0,5,10,15,20,25,30]:

    if typeCro=='2' and Per!=0:
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Expand/Single/Rg_llps_%d.txt' %(10*Per),'r')
    else:
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Single/Rg_llps_%d.txt' %(10*Per),'r')

    line_single = f_single.readlines()

    Rg0=np.zeros([N_mean])
    cut_t=round(len(line_single)/N_mean)

    for i in range(len(line_single)):
        for k in range(N_mean):
            if k*cut_t<=i<(k+1)*cut_t:
                Rg0[k]+=float(line_single[i])/cut_t

    Rg.append(np.mean(Rg0))
    Rg_std.append(np.std(Rg0))


    f=open('../Crowd_%d/rou_high.txt' %(Per),'r')
    line=f.readlines()

    rou.append(float(line[0]))
    rou_std.append(float(line[1]))

    f.close()

fig=plt.figure(figsize=(8,6),dpi=1000)
if nfile=='1':
    plt.scatter(Rg,rou_fitting,marker="o",color='black',s=100)
    k,b=op.curve_fit(y,np.log(Rg),np.log(rou_fitting))[0]

elif nfile=='2':
    if typeCro=='1':
        cmap1=plt.get_cmap('Reds',8)
    elif typeCro=='2':
        cmap1=plt.get_cmap('Blues',8)
    for i in range(7):
        plt.errorbar(Rg[i],rou[i], xerr=Rg_std[i], yerr=rou_std[i], fmt='o',mfc=cmap1((5*i+5)/40),mec='black',mew=2,elinewidth=2, ecolor='black',capthick=12, capsize=8,markersize=16,zorder=2)
    
    k,b=op.curve_fit(y,Rg,rou)[0]


xx=np.arange(18,34,0.1)
plt.plot(xx,(y(xx,k,b)),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)

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

if typeCro=='1':
    plt.xlim(20,32)
    plt.ylim(0.92,1.02) 
    plt.xticks([20,24,28,32],['2.0','2.4','2.8','3.2'],fontproperties="Arial",size=36)
    plt.yticks([0.93,0.96,0.99,1.02],fontproperties="Arial",size=36)
elif typeCro=='2':
    plt.xlim(24,32)
    plt.ylim(0.35,1.0)
    plt.xticks([24,28,32],['2.4','2.8','3.2'],fontproperties="Arial",size=36)
    plt.yticks([0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)


plt.xlabel('$\mathregular{R_{g}}$'+' (nm)',size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+'$\mathregular{_{h}}$'+" (g/cm"+'$\mathregular{^3}$)',size=40,labelpad=10,fontproperties="Arial")  
plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
# plt.tick_params(length=5,pad=10,which='minor',width = 2,direction='in')

fig.set_size_inches(8,6)
plt.savefig('Rg_vs_rou_high_'+nfile+'.png',dpi=1000,bbox_inches='tight')