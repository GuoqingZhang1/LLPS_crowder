import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵


Per=PERCENT

# def y(x,a):
#     return a*x

f_llps=open('MSD_all_llps.txt',"r" )
line_llps = f_llps.readlines() # 以行的形式进行读取文件
Lmax_llps = len(line_llps)

MSD_llps=[]
for i in range(Lmax_llps):
    MSD_llps.append(0.01*float(line_llps[i]))

f_single=open(f'/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/tdp43/msd.pyw/{-0.01*Per}_300.0','r')
line_single = f_single.readlines()

MSD_single=[]
for i in range(Lmax_llps):
    ss=line_single[i].split()
    MSD_single.append(0.01*float(ss[1]))


fig = plt.figure(dpi=1000,figsize=(8,6))
plt.rcParams['font.sans-serif'] ='Arial'

plt.plot(0.1*np.arange(Lmax_llps),MSD_llps,linewidth=6.0,color='darkgreen',label='Condensate')
# ax1.plot(0.1*np.arange(Lmax_llps),MSD_single,linewidth=6.0,color='darkgreen',label='Free state')
# plt.plot(xx,np.exp(y(np.log(xx),a_llps,b_llps)),linewidth=6.0,label='Condensate')
plt.plot(0.1*np.arange(Lmax_llps),MSD_single,linewidth=6.0,color='orange',label='Free state')
# plt.plot(xx,np.exp(y(np.log(xx),a_single,b_single)),linewidth=6.0,label='Free state')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1,0.1*Lmax_llps+10)
plt.ylim(0.01,1000)
plt.xlabel('Lag time, '+chr(964)+' (ns)',size=40,labelpad=10,fontproperties='calibri')
plt.ylabel('MSD'+' ('+u'$\mathregular{nm^2}$)',size=40,labelpad=10,fontproperties='Arial')
plt.xticks(fontproperties="Arial",size=36)
plt.yticks(fontproperties="Arial",size=36)

plt.text(0.2, 60, 'Condensate', fontsize=28, color='darkgreen', fontproperties='Arial')
plt.text(0.2, 200, 'Free state', fontsize=28, color='orange', fontproperties='Arial')

# plt.text(50,MSD_llps[50]-0.5,chr(945)+'=%.2f' %(a_llps),fontdict={'size':'26','color':'blue','family':'Times New Roman'})
# plt.text(26,MSD_single[50]+5,chr(945)+'=%.2f'  %(a_single),fontdict={'size':'26','color':'orange','family':'Times New Roman'})

plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
plt.tick_params(length=5,which='minor',width = 2,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(8,6)
plt.savefig('MSD_t_%d.png' %(Per),dpi=1000,bbox_inches='tight')