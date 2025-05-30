import numpy as np 
import matplotlib.pyplot as plt #绘图
import math 
import matplotlib as mpl
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset


begintime=10000
totaltime=50001
totalline=500

N_mean=10

rou_all_pro=[]
rou_all_cro=[]

for Per in ['0','5','10','15','20','25','30']:
    f_index=open('../Crowd_'+Per+'/Middle_list.txt','r')
    line_index=f_index.readlines()

    M_index=[]

    for i in range(len(line_index)):
        M_index.append(float(line_index[i]))

    f_pro=open('../Crowd_'+Per+'/density_pro.txt','r')
    line_pro=f_pro.readlines()

    f_cro=open('../Crowd_'+Per+'/density_cro.txt','r')
    line_cro=f_cro.readlines()

    rou_pro=np.zeros([500])
    rou_cro=np.zeros([500])

    rou_high=[]
    rou0=np.zeros([N_mean])
    cut_t=round((totaltime-begintime)/N_mean)

    for k in range(begintime,totaltime):
        t_pro=[]
        t_cro=[]

        for i in range(totalline):
            ss=line_pro[k*(totalline+1)+i+4].split()
            ss1=line_cro[k*(totalline+1)+i+4].split()
            t_pro.append(float(ss[3]))
            t_cro.append(float(ss1[3]))

        z0_index=t_pro.index(0)
    
        re_cro=[]
        re_pro=[]

        for i in range(z0_index,totalline):
            re_cro.append(t_cro[i])
            re_pro.append(t_pro[i])

        for i in range(0,z0_index):
            re_cro.append(t_cro[i])
            re_pro.append(t_pro[i])

        l_cro=[]
        l_pro=[]

        for i in range(math.ceil(M_index[k]),totalline):
            l_cro.append(re_cro[i])
            l_pro.append(re_pro[i])

        for i in range(0,math.ceil(M_index[k])):
            l_cro.append(re_cro[i])
            l_pro.append(re_pro[i])

        for j in range(N_mean):
            if begintime+j*cut_t<=k<begintime+(j+1)*cut_t:
                rou0[j]+=l_pro[249]/cut_t

        for i in range(totalline):
            rou_pro[i]=rou_pro[i]+l_pro[i]/(totaltime-begintime)
            rou_cro[i]=rou_cro[i]+l_cro[i]/(totaltime-begintime)

    
    rou_high.append(np.mean(rou0))
    rou_high.append(np.std(rou0))
    np.savetxt('../Crowd_'+Per+'/rou_high.txt', np.c_[rou_high],fmt='%f',delimiter='\t')

    rou_all_pro.append(rou_pro)
    rou_all_cro.append(rou_cro)

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

cmap1=plt.get_cmap('Reds',8)


for i in range(7):
    plt.plot(np.arange(0,50,0.1),rou_all_pro[i]+0.6,linewidth=4.0,color=cmap1((i*5+5)/40))
    plt.plot(np.arange(0,50,0.1),rou_all_cro[i],linestyle='--',dashes=(10,1),linewidth=4.0,color=cmap1((5*i+5)/40))
    
plt.xlabel("z (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+" (g/cm"+'$\mathregular{^3}$)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks([0.0,0.3,0.6,1.2,1.8],['0.0','0.3','0.0','0.6','1.2'],fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  
plt.hlines(y=0.57,xmin=0,xmax=50,linewidth=3,color='black')
plt.xlim(0,50)
plt.ylim(-0.05,1.8)
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
    ticks=[1.5/8,3.5/8,5.5/8,7.5/8]

)
cb.set_ticklabels(['0%','10%','20%','30%'])
cb.ax.set_ylim(1/8,1)
cb.ax.set_title('C'+'$\mathregular{_{Rep}}$',pad=20,fontdict={'size':30,'family':'Arial'})

# axins = zoomed_inset_axes(ax, zoom=2.5, loc='upper right')  # 放大倍数为2.5，位置在右上角
# axins.plot(np.arange(0,50,0.1),rou_all_pro[i], 'b-')  # 绘制内容和主图一致

# # 设置放大区域的范围
# x1, x2 = 20, 30
# y1, y2 = 0.9, 1.1
# axins.set_xlim(x1, x2)
# axins.set_ylim(y1, y2)

# # 调整子图的样式
# axins.set_xticks([20,25,30])
# axins.set_yticks([0.8,0.9,1.0])

# # 画框并连线
# mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5", lw=1)

ax_inset = fig.add_axes([0.54, 0.67, 0.19, 0.2])  # [左, 下, 宽, 高]
for i in range(7):
    ax_inset.plot(np.arange(0,50,0.1),rou_all_pro[i],linewidth=4.0,color=cmap1((i*5+5)/40))

ax_inset.set_xlim(20,30)
ax_inset.set_ylim(0.88,1.11)

ax_inset.set_xticks([20,25,30])  # 设置x轴刻度
ax_inset.set_yticks([0.9,1.0,1.1])  # 设置y轴刻度

for tick in ax_inset.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)  # 设置x轴刻度标签字体大小
    tick.label1.set_fontfamily('Arial')  # 设置x轴刻度标签字体类型

for tick in ax_inset.yaxis.get_major_ticks():
    tick.label1.set_fontsize(16)  # 设置y轴刻度标签字体大小
    tick.label1.set_fontfamily('Arial')  # 设置y轴刻度标签字体类型
# 设置子图的边框样式
bwith = 2
ax_inset.spines['top'].set_linewidth(bwith)
ax_inset.spines['bottom'].set_linewidth(bwith)
ax_inset.spines['left'].set_linewidth(bwith)
ax_inset.spines['right'].set_linewidth(bwith)

ax_inset.tick_params(length=4,pad=2,width = 2,direction='in')

fig.set_size_inches(10,6)
plt.savefig('rou_z_tot.png',bbox_inches='tight',dpi=1000)