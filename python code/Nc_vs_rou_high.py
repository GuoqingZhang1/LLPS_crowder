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

# def y0(x,k):
#     return k*x

nfile='2'
typeCro='2'

fig=plt.figure(figsize=(8,6),dpi=1000)

Nc=[]
Nc_std=[]
rou=[]
rou_std=[]
rou_fitting=[]
for Per in [0,5,10,15,20,25,30]:

    if typeCro=='2' and Per!=0:
        N_inter=np.load(file="/hpc2hdd/home/gzhang733/project/CTD_LLPS/Expand/Double/N_inter_%d.npy" %(Per))
    else:
        N_inter=np.load('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Double/N_inter_%d.npy' %(Per),'r')



    Nc.append(N_inter[0])

    Nc_std.append(N_inter[1])

    f=open('../Crowd_%d/rou_high.txt' %(Per),'r')
    line=f.readlines()

    rou.append(float(line[0]))
    rou_std.append(float(line[1]))

    f.close()

# if nfile=='1':
#     plt.scatter(B22,rou_fitting,marker="o",color='black',s=100)
#     k,b=op.curve_fit(y,np.log10(B22),np.log10(rou_fitting))[0]

if nfile=='2':
    if typeCro=='1':
        cmap1=plt.get_cmap('Reds',8)
    elif typeCro=='2':
        cmap1=plt.get_cmap('Blues',8)
    for i in range(7):
        plt.errorbar(Nc[i],rou[i],xerr=Nc_std[i],yerr=rou_std[i], fmt='o',mfc=cmap1((5*i+5)/40),mec='black',mew=2,elinewidth=2, ecolor='black',capthick=12, capsize=8,markersize=16,zorder=2)
    
    k,b=op.curve_fit(y,Nc,rou)[0]

xx=np.arange(-10,140,0.1)

plt.plot(xx,y(xx,k,b),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)
# # plt.plot(xx,np.power(10,y(np.log10(xx),k,b)),color='red',label='Fitting curve',linewidth=4.0)


if typeCro=='1':
    plt.xlim(0,120)
    plt.ylim(0.92,1.02) 
    plt.xticks([0,40,80,120],fontproperties="Arial",size=36)
    plt.yticks([0.93,0.96,0.99,1.02],fontproperties="Arial",size=36)
elif typeCro=='2':
    plt.xlim(0,15)
    plt.ylim(0.35,1.0)
    plt.xticks([0,5,10,15],fontproperties="Arial",size=36)
    plt.yticks([0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)


# plt.xscale('log')
# plt.yscale('log')

plt.xlabel('$\mathregular{N_{c}}$ (Dimer)',size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+'$\mathregular{_{h}}$'+" (g/cm"+'$\mathregular{^3}$)',size=40,labelpad=10,fontproperties="Arial")  

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
plt.tick_params(length=5,which='minor',width = 2,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

# formatter = ScalarFormatter(useMathText=True)
# formatter.set_powerlimits((0, 1))
# ax.xaxis.set_major_formatter(formatter)

# # 获取并修改偏移文本
# offset_text = ax.xaxis.get_offset_text()
# offset_text.set_fontsize(20)

# # 修改偏移文本为 10^-2 的形式
# def update_offset_text(event):
#     if ax.xaxis.get_offset_text().get_text():
#         exponent_str = ax.xaxis.get_offset_text().get_text().replace('e', '10^{') + '}'
#         ax.xaxis.offsetText.set_text(r'$\times$' + exponent_str)
#     fig.canvas.draw_idle()

# fig.canvas.mpl_connect('draw_event', update_offset_text)

# plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black',shadow=True)
fig.set_size_inches(8,6)
plt.savefig('Nc_vs_rou_high_'+nfile,dpi=1000,bbox_inches='tight')