import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',N)

for Per in [5,10,15,20,25,30]:
    f_llps=open('Rg_per_in_%d.txt' %(Per*10),"r" )
    line_llps = f_llps.readlines() # 以行的形式进行读取文件
    Lmax_llps = len(line_llps)

    Rg=[]
    for i in range(Lmax_llps):
        ss=line_llps[i].split()
        Rg.append(float(ss[0]))

    Rg_min=np.min(Rg)
    Rg_max=np.max(Rg)
    delta=0.01
    N_bins=math.ceil((Rg_max-Rg_min)/delta)

    Rg_dis=np.zeros([N_bins])
    for i in range(len(Rg)):
        if Rg_min<Rg[i]<Rg_max:
            nl=math.floor((Rg[i]-Rg_min)/delta)
            Rg_dis[nl]=Rg_dis[nl]+1/len(Rg)


    plt.plot(np.arange(Rg_min,Rg_max,delta),Rg_dis,linewidth=4.0,color=cmap((float(Per)+5)/40))

plt.xlabel(u'$\mathregular{N_{in}}$'+' (%)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.xlim(15,50)
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
plt.savefig('Rg_in_per_dis.png',dpi=1000,bbox_inches='tight')