import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',N)

for Per in ['50','100','150','200','250','300']:
    f_pro=open('trj/tdp43_-%.2f_nopb/N_r_cro.txt' %(0.001*float(Per)),'r')
    line_pro=f_pro.readlines()

    Rg=[]

    ss=line_pro[0].split()
    for i in range(125):
        
        Rg.append(float(ss[i]))

    Rdf=np.array(Rg)
    Rdf=Rdf-Rdf[120]

    plt.plot(np.arange(0,12.5,0.1),Rdf,linewidth=4.0,color=cmap((float(Per)+50)/400))

plt.xlabel('r'+' (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('g(r)',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,4,8,12],fontproperties='Arial',fontsize=36)
plt.yticks([0,1,2,3,4],fontproperties='Arial',fontsize=36)
plt.xlim(0,12)
plt.ylim(0,4)
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
plt.savefig('g_r_single.png',dpi=1000,bbox_inches='tight')