import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8
T_0=120.27

Rg_per=[]
Rg_single_per=[]

P=[]

for Per in [0,5,10,15,20,25,30]:
    f_sin=open('../Single/Rg_llps_%d.txt' %(10*Per),'r')
    line_sin=f_sin.readlines()

    f_pro=open('../Crowd_%d/Rg_llps.txt' %(Per),'r')
    line_pro=f_pro.readlines()

    Rg_sin=[]

    for i in range(len(line_sin)):
        Rg_sin.append(float(line_sin[i]))

    Rg=[]

    for i in range(len(line_pro)):
        Rg.append(float(line_pro[i]))

    Rg_single_per.append(np.mean(Rg_sin))
    Rg_per.append(np.mean(Rg))

    P.append(Per)

fig=plt.figure(figsize=(8,6),dpi=1000)

# cmap = plt.get_cmap('Reds')

cmap = plt.get_cmap('Blues')
# 计算每个点的颜色
colors = cmap(np.linspace(0, 1, 7))
nn=int(1/7)
for i in range(6):
    plt.errorbar(P[i:i+2],Rg_per[i:i+2],color=colors[i+1],fmt='o-',mec='black', mew=2 ,markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)
    plt.errorbar(P[i:i+2],Rg_single_per[i:i+2],color=colors[i+1],fmt='s-' ,markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)


plt.xlabel('C'+'$\mathregular{_{Rep}}$'+' (%)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(u'$\mathregular{R_{g}}$'+' (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks([20,30,40],['2.0','3.0','4.0'],fontproperties='Arial',fontsize=36)
# plt.xlim(0,82)
# plt.ylim(-0.0002,0.0065)
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
plt.savefig('Rg_single_llps_per.png',dpi=1000,bbox_inches='tight')