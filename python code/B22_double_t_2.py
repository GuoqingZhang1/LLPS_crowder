import numpy as np
import math
import matplotlib.pyplot as plt #绘图
import matplotlib as mpl

d_bin=0.5
N_bins=math.ceil(15/d_bin)

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

cmap1=plt.get_cmap('Oranges',8)

i=0
for Per in ['0','50','100','150','200','250','300']:

 
    p_r=np.load(file="p_r_%s.npy" %(Per))



    plt.plot(np.arange(0,15,d_bin),p_r,linewidth=4.0,color=cmap1((i+1)/15))
    i=i+1



plt.xlabel("r (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel('P(r)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

# plt.xlim(0,50)
# plt.ylim(-0.05,1.6)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)
cb= fig.colorbar(
    plt.cm.ScalarMappable(norm=norm, cmap=cmap1),
    ax=ax,
    orientation='vertical',
    ticks=[1.5/8,2.5/8,3.5/8,4.5/8,5.5/8,6.5/8,7.5/8]

)
cb.set_ticklabels(['0.0%','5.0%','10%','15%','20%','25%','30%'])
cb.ax.set_ylim(1/15,1)
cb.ax.set_title('C'+'$\mathregular{_{Rep}}$',pad=20,fontdict={'size':30,'family':'Arial'})

fig.set_size_inches(10,6)
plt.savefig('p_r.png',bbox_inches='tight',dpi=1000)

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

cmap1=plt.get_cmap('Oranges',15)

i=0
for Per in ['0','50','100','150','200','250','300']:

    rou_r=np.load(file="rou_r_%s.npy" %(Per))



    plt.plot(np.arange(0,15,d_bin),rou_r,linewidth=4.0,color=cmap1((i+1)/15))
    i=i+1



plt.xlabel("r (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+'(r)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  
plt.yscale('log')
# plt.xlim(0,50)
# plt.ylim(-0.05,1.6)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)
cb= fig.colorbar(
    plt.cm.ScalarMappable(norm=norm, cmap=cmap1),
    ax=ax,
    orientation='vertical',
    ticks=[1.5/8,2.5/8,3.5/8,4.5/8,5.5/8,6.5/8,7.5/8]

)
cb.set_ticklabels(['0.0%','5.0%','10%','15%','20%','25%','30%'])
cb.ax.set_ylim(1/15,1)
cb.ax.set_title('C'+'$\mathregular{_{Rep}}$',pad=20,fontdict={'size':30,'family':'Arial'})

fig.set_size_inches(10,6)
plt.savefig('rou_r.png',bbox_inches='tight',dpi=1000)


fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

cmap1=plt.get_cmap('Oranges',15)

i=0
for Per in ['0','50','100','150','200','250','300']:


    g_r=np.load(file="g_r_%s.npy" %(Per))


    plt.plot(np.arange(0,15,d_bin),g_r,linewidth=4.0,color=cmap1((i+1)/15))
    i=i+1



plt.xlabel("r (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel('g(r)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  
plt.yscale('log')
# plt.xlim(0,50)
# plt.ylim(-0.05,1.6)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)
cb= fig.colorbar(
    plt.cm.ScalarMappable(norm=norm, cmap=cmap1),
    ax=ax,
    orientation='vertical',
    ticks=[1.5/8,2.5/8,3.5/8,4.5/8,5.5/8,6.5/8,7.5/8]

)
cb.set_ticklabels(['0.0%','5.0%','10%','15%','20%','25%','30%'])
cb.ax.set_ylim(1/15,1)
cb.ax.set_title('C'+'$\mathregular{_{Rep}}$',pad=20,fontdict={'size':30,'family':'Arial'})

fig.set_size_inches(10,6)
plt.savefig('g_r.png',bbox_inches='tight',dpi=1000)