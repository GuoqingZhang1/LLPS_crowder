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

nfile='2'
typeCro='1'

fig=plt.figure(figsize=(8,6),dpi=1000)

B22=np.zeros([7])
rou=[]
MSD=[]
for Per in [0,5,10,15,20,25,30]:

    f_MSD=open('../Crowd_%d/Corr_Rg_tau_fitting.txt' %(Per),'r')
    line_llps = f_MSD.readlines() # 以行的形式进行读取文件
    Lmax_llps = len(line_llps)

    tau_llps=[]
    for i in range(Lmax_llps):
        tau_llps.append(float(line_llps[i]))
    MSD.append(np.mean(tau_llps))

    f_pro=open('../Crowd_%d/density_pro.txt' %(Per),'r')
    line_pro=f_pro.readlines()


    f_index=open('../Crowd_%d/Middle_list.txt' %(Per),'r')
    line_index=f_index.readlines()

    M_index=[]

    for i in range(len(line_index)):
        M_index.append(float(line_index[i]))

    rou_z=np.zeros([500])

    for k in range(begintime,totaltime):
        t_pro=[]

        for i in range(totalline):
            ss=line_pro[k*(totalline+1)+i+4].split()
            t_pro.append(float(ss[3]))
        

        z0_index=t_pro.index(0)
    
        re_pro=[]

        for i in range(z0_index,totalline):
            re_pro.append(t_pro[i])

        for i in range(0,z0_index):
            re_pro.append(t_pro[i])

        l_pro=[]
  

        for i in range(math.ceil(M_index[k]),totalline):
            l_pro.append(re_pro[i])

        for i in range(0,math.ceil(M_index[k])):
            l_pro.append(re_pro[i])

        for i in range(totalline):
            rou_z[i]=rou_z[i]+l_pro[i]/(totaltime-begintime)


    rou.append(rou_z[249])
    f_MSD.close()
    f_pro.close()
    f_index.close()

if typeCro=='1':
    cmap1=plt.get_cmap('Blues',8)
elif typeCro=='2':
    cmap1=plt.get_cmap('Reds',8)
for i in range(7):
    plt.scatter(rou[i],MSD[i],marker="o",edgecolors='black',color=cmap1((5*i+5)/40),s=150,zorder=2)
k,b=op.curve_fit(y,rou,MSD)[0]


xx=np.arange(np.min(rou)-0.1,np.max(rou)+0.1,0.1)
plt.plot(xx,y(xx,k,b),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)

if typeCro=='1':
    plt.xlim(0.89,1.02)
    # plt.ylim(0.90,1.02)
    plt.xticks([0.90,0.94,0.98,1.02],fontproperties="Arial",size=36)
    plt.yticks([0.0,10,20,30,40],fontproperties="Arial",size=36)
elif typeCro=='2':
    # plt.xlim(24,32)
    # plt.ylim(0.38,1.02)
    plt.xticks([0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)
    plt.yticks([0.0,5,10,15,20],fontproperties="Arial",size=36)

plt.xticks(fontproperties="Arial",size=36)
plt.yticks(fontproperties="Arial",size=36)


plt.xlabel(chr(961)+'$\mathregular{_{high}}$'+" (g/cm"+'$\mathregular{^3}$)',size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+'$\mathregular{_{Rg}}$'+' (ns)',size=40,labelpad=10,fontproperties='calibri')  

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
plt.savefig('rou_high_vs_tau',dpi=1000,bbox_inches='tight')