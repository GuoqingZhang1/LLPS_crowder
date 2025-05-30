import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8
T_0=120.27
fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',N)

Stru_i=0

for Per in ['0','5','10','15','20','25','30']:
    f_pro=open('../Crowd_'+Per+'/Rg_3R.txt','r')
    line_pro=f_pro.readlines()

    Rg=[]

    for i in range(len(line_pro)):
        ss=line_pro[i].split()
        Rg.append(float(ss[Stru_i]))

    Rg_min=np.min(Rg)
    Rg_max=np.max(Rg)
    delta=0.1
    N_bins=math.ceil((Rg_max-Rg_min)/delta)

    Rg_dis=np.zeros([N_bins])
    for i in range(len(Rg)):
        nl=math.floor((Rg[i]-Rg_min)/delta)
        Rg_dis[nl]=Rg_dis[nl]+1/len(Rg)


    plt.plot(np.arange(Rg_min,Rg_max,delta),Rg_dis,linewidth=4.0,color=cmap((float(Per)+5)/40))

plt.xlabel(u'$\mathregular{R_{g}}$'+' (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,20,40,60,80],['0','2','4','6','8'],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.xlim(0,82)
# plt.ylim(-0.0002,0.0065)
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
plt.savefig('Rg_3R_%d.png' %(Stru_i),dpi=1000,bbox_inches='tight')