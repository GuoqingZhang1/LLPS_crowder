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

MSD=[]
B22=[]
for Per in ['0']:
    f_MSD=open('../Crowd_%s/MSD_all_llps.txt' %(Per),'r')
    line_MSD=f_MSD.readlines()

    MSD.append(0.01*float(line_MSD[100]))
 
    f_MSD.close()

for Per in ['1','5','10','15','20','30','40']:
    f_MSD=open('../Crowd_m_%s/MSD_all_llps.txt' %(Per),'r')
    line_MSD=f_MSD.readlines()

    MSD.append(0.01*float(line_MSD[100]))
 
    f_MSD.close()

for Per in ['5','10','15','20','25','30']:
    f_MSD=open('../Crowd_%s/MSD_all_llps.txt' %(Per),'r')
    line_MSD=f_MSD.readlines()

    MSD.append(0.01*float(line_MSD[100]))
 
    f_MSD.close()

for Per in [0,1,5,10,15,20,30,40,50,100,150,200,250,300]:

    if typeCro=='2' :
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Expand/Double/B22_%d.txt' %(Per),'r')
    else:
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Double/B22_%d.txt' %(Per),'r')

    line_single = f_single.readlines()

    B22.append(-float(line_single[0]))



# if nfile=='1':
#     plt.scatter(B22,rou_fitting,marker="o",color='black',s=100)
#     k,b=op.curve_fit(y,np.log10(B22),np.log10(rou_fitting))[0]

if nfile=='2':
    if typeCro=='1':
        cmap1=plt.get_cmap('Reds',8)
    elif typeCro=='2':
        cmap1=plt.get_cmap('Blues',15)
        for i in range(14):
            plt.errorbar(B22[i],MSD[i], fmt='o',mfc=cmap1((i+1)/15),mec='black',mew=2,elinewidth=2, ecolor=cmap1((i+1)/15),capthick=2, capsize=5,markersize=16,zorder=2)
    
    k,b=op.curve_fit(y,B22,MSD)[0]

xx=np.arange(-200000,1200000,0.1)

plt.plot(xx,y(xx,k,b),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)
# plt.plot(xx,np.power(10,y(np.log10(xx),k,b)),color='red',label='Fitting curve',linewidth=4.0)


if typeCro=='1':
    plt.xlim(-200000,1200000)
    # plt.ylim(0.90,1.02) 
    plt.xticks([0,400000,800000,1200000],['0.0','0.4','0.8','1.2'],fontproperties="Arial",size=36)
    plt.yticks([0.90,0.94,0.98,1.02],fontproperties="Arial",size=36)
elif typeCro=='2':
    plt.xlim(0,75000)
    plt.ylim(0,6)
    plt.xticks([0,20000,40000,60000],['0.0','2.0','4.0','6.0'],fontproperties="Arial",size=36)
    plt.yticks([0,2,4,6],fontproperties="Arial",size=36)



# plt.xscale('log')
# plt.yscale('log')

plt.xlabel('$\mathregular{-B_{22}}$ ('+'$\\times$'+'$\mathregular{10^{4}}$)',size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+'$\mathregular{_{high}}$'+" (g/cm"+'$\mathregular{^3}$)',size=40,labelpad=10,fontproperties="Arial") 

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
plt.savefig('B22_vs_MSD_'+nfile,dpi=1000,bbox_inches='tight')