import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math

begin=10000
Timeall=90000

N_in_per=[]
N_out_per=[]

for Per in [0.05,0.10,0.15,0.20,0.25,0.30]:

    f_N=open('../trj/tdp43_%.2f_nopb/N_in_out.txt' %(Per),'r')
    line_N=f_N.readlines()



    N_in=float(line_N[0]) 
    N_out=float(line_N[1])

    N_in_per.append(N_in)
    N_out_per.append(N_out)

fig,axx1=plt.subplots(figsize=(8,6),dpi=1000)

# plt.plot(0.05+np.arange(0,12.5,0.1),rou_pro[0:125],linewidth=4.0)
axx1.scatter(np.arange(0.5,3.5,0.5),N_in_per,color='darkorange',s=150,label='N_in')
axx1.plot(np.arange(0.5,3.5,0.5),N_in_per,color='darkorange',linewidth=4.0)

axx1.set_xlabel('C'+'$\mathregular{_{Rep}}$'+" (%)",size=40,labelpad=10,fontproperties="Arial")
axx1.set_ylabel(u'$\mathregular{N_{in}}$',labelpad=10,size=40,fontproperties="Arial",color='darkorange')
axx1.set_xticks([0.5,1.0,1.5,2.0,2.5,3.0])
axx1.set_xticklabels(["5","10","15","20","25","30"],fontproperties='Arial',fontsize=36)
axx1.set_yticks([0.0002,0.0004,0.0006])
axx1.set_yticklabels(["0.0002","0.0004","0.0006"],fontproperties='Arial',fontsize=36,color='darkorange')

axx1.tick_params(length=7,pad=10,width = 3,direction='in') 

axx2=axx1.twinx()
axx2.scatter(np.arange(0.5,3.5,0.5),N_out_per,color='darkgreen',s=150,label='N_out')
axx2.plot(np.arange(0.5,3.5,0.5),N_out_per,color='darkgreen',linewidth=4.0)

axx2.set_xlabel("z (nm)",size=40,labelpad=10,fontproperties="Arial")
axx2.set_ylabel(u'$\mathregular{N_{out}}$',labelpad=10,size=40,fontproperties="Arial", color='darkgreen')
axx2.set_xticks([0.5,1.0,1.5,2.0,2.5,3.0])
axx2.set_xticklabels(["5","10","15","20","25","30"],fontproperties='Arial',fontsize=36)
axx2.set_yticks([0.15,0.25,0.35,0.45])
axx2.set_yticklabels(["0.15","0.25","0.35","0.45"],fontproperties='Arial',fontsize=36, color='darkgreen')

axx2.tick_params(length=7,pad=10,width = 3,direction='in') 

# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)

# plt.ylim(-0.05,1.8)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24

fig.set_size_inches(8,6)
plt.savefig('N_in_out.png',bbox_inches='tight',dpi=1000)