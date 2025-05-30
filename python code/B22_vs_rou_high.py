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
typeCro='1'

fig=plt.figure(figsize=(8,6),dpi=1000)

B22=[]
rou=[]
rou_std=[]
rou_fitting=[]
for Per in [0,5,10,15,20,25,30]:

    if typeCro=='2' and Per!=0:
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Expand/Double/B22_%d.txt' %(10*Per),'r')
    else:
        f_single=open('/hpc2hdd/home/gzhang733/project/CTD_LLPS/Double/B22_%d.txt' %(10*Per),'r')

    line_single = f_single.readlines()

    B22.append(-float(line_single[0]))

    f=open('../Crowd_%d/rou_fitting.txt' %(Per),'r')
    line=f.readlines()

    rou_fitting.append(float(line[1]))

    f_pro=open('../Crowd_%d/density_pro.txt' %(Per),'r')
    line_pro=f_pro.readlines()


    f_index=open('../Crowd_%d/Middle_list.txt' %(Per),'r')
    line_index=f_index.readlines()

    M_index=[]

    for i in range(len(line_index)):
        M_index.append(float(line_index[i]))

    rou_z=np.zeros([500])

    rou_i=[]

    for k in range(begintime,totaltime):
        t_pro=[]

        for i in range(totalline):
            ss=line_pro[k*(totalline+1)+i+4].split()
            t_pro.append(float(ss[3]))
        

        z0_index=t_pro.index(0)
    
        re_pro=[]

        for i in range(z0_index,totalline):
            re_pro.append(t_pro[i])

        for i in range(0,z0_index):
            re_pro.append(t_pro[i])

        l_pro=[]
  

        for i in range(math.ceil(M_index[k]),totalline):
            l_pro.append(re_pro[i])

        for i in range(0,math.ceil(M_index[k])):
            l_pro.append(re_pro[i])

        for i in range(totalline):
            rou_z[i]=rou_z[i]+l_pro[i]/(totaltime-begintime)

        rou_i.append(l_pro[249])

    rou.append(np.mean(rou_i))
    rou_std.append(np.std(rou_i)/(totaltime-begintime)**0.5)

    f_single.close()
    f.close()
    f_pro.close()
    f_index.close()

# if nfile=='1':
#     plt.scatter(B22,rou_fitting,marker="o",color='black',s=100)
#     k,b=op.curve_fit(y,np.log10(B22),np.log10(rou_fitting))[0]

if nfile=='2':
    if typeCro=='1':
        cmap1=plt.get_cmap('Reds',8)
    elif typeCro=='2':
        cmap1=plt.get_cmap('Blues',8)
    for i in range(7):
        plt.errorbar(B22[i],rou[i], yerr=rou_std[i], fmt='o',mfc=cmap1((5*i+5)/40),mec='black',mew=2,elinewidth=2, ecolor=cmap1((5*i+5)/40),capthick=2, capsize=5,markersize=16,zorder=2)
    
    k,b=op.curve_fit(y,B22,rou)[0]

xx=np.arange(-200000,1200000,0.1)

plt.plot(xx,y(xx,k,b),color='lightgray',linestyle='--',linewidth=4.0,zorder=1)
# plt.plot(xx,np.power(10,y(np.log10(xx),k,b)),color='red',label='Fitting curve',linewidth=4.0)


if typeCro=='1':
    plt.xlim(-200000,1200000)
    # plt.ylim(0.90,1.02) 
    plt.xticks([0,400000,800000,1200000],['0.0','0.4','0.8','1.2'],fontproperties="Arial",size=36)
    plt.yticks([0.90,0.94,0.98,1.02],fontproperties="Arial",size=36)
elif typeCro=='2':
    # plt.xlim(24,32)
    # plt.ylim(0.38,1.02)
    plt.xticks(fontproperties="Arial",size=36)
    plt.yticks([0.4,0.6,0.8,1.0],fontproperties="Arial",size=36)


# plt.xscale('log')
# plt.yscale('log')

plt.xlabel('$\mathregular{-B_{22}}$ ('+'$\\times$'+'$\mathregular{10^{6}}$)',size=40,labelpad=10,fontproperties="Arial")
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
plt.savefig('B22_vs_rou_high_'+nfile,dpi=1000,bbox_inches='tight')