import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',N)

for Per in ['0','50','100','150','200','250','300']:
    f_pro=open('Rg_llps_'+Per+'.txt','r')
    line_pro=f_pro.readlines()

    Rg=[]

    for i in range(len(line_pro)):
        Rg.append(float(line_pro[i]))

    Rg_min=np.min(Rg)
    Rg_max=np.max(Rg)
    delta=1.5
    N_bins=math.ceil((Rg_max-Rg_min)/delta)

    Rg_dis=np.zeros([N_bins])
    for i in range(len(Rg)):
        nl=math.floor((Rg[i]-Rg_min)/delta)
        Rg_dis[nl]=Rg_dis[nl]+1/len(Rg)


    plt.plot(np.arange(Rg_min,Rg_max,delta),Rg_dis,linewidth=4.0,color=cmap((float(Per)+50)/400))

plt.xlabel(u'$\mathregular{R_{g}}$'+' (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([10,30,50],['1','3','5'],fontproperties='Arial',fontsize=36)
plt.yticks([0,0.1,0.2,0.3],fontproperties='Arial',fontsize=36)
plt.xlim(10,55)
plt.ylim(0.0,0.3)
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
plt.savefig('Rg_single.png',dpi=1000,bbox_inches='tight')