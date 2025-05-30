import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵

MSD_llps=[]
MSD_0=[]
MSD_1=[]
MSD_2=[]
MSD_single=[]

Per_x=[]



for Per in [0,5,10,15,20,25,30]:
    f_llps=open('../Crowd_%d/MSD_all_llps.txt' %(Per),"r" )
    line_llps = f_llps.readlines() # 以行的形式进行读取文件
    Lmax_llps = len(line_llps)

    llps_x=[]
    for i in range(10,1000):    #1-100 ns
        llps_x.append(0.01*float(line_llps[i])/(2*0.1*i))    
    MSD_llps.append(np.mean(llps_x))

    f_llps.close()
    Per_x.append(Per)

    f_all=open('../Crowd_%d/MSD_4R_llps.txt' %(Per),"r" )
    line_all = f_all.readlines() # 以行的形式进行读取文件
    Lmax_all = len(line_all)

    R0_x=[]
    R1_x=[]
    R2_x=[]
    for i in range(10,1000):
        ss=line_all[i].split()
        R0_x.append(0.01*float(ss[0])/(2*0.1*i))
        R1_x.append(0.01*float(ss[1])/(2*0.1*i))
        R2_x.append(0.01*float(ss[2])/(2*0.1*i))
    
    MSD_0.append(np.mean(R0_x))
    MSD_1.append(np.mean(R1_x))
    MSD_2.append(np.mean(R2_x))

    f_single=open(f'/hpc2hdd/JH_DATA/share/cfeng593/PrivateShareGroup/share/tdp43/msd.pyw/{0.01*Per}_300.0','r')
    line_single = f_single.readlines()

    single_x=[]
    for i in range(10,1000):
        sss=line_single[i].split()
        single_x.append(0.01*float(sss[1])/(2*0.1*i))
    MSD_single.append(np.mean(single_x))

fig = plt.figure(dpi=1000,figsize=(8,6))
plt.rcParams['font.sans-serif'] ='Arial'
ax1 = fig.gca()
ax1.scatter(Per_x,MSD_0,linewidth=6.0,label='IDR1')
ax1.scatter(Per_x,MSD_1,linewidth=6.0,label='Helix')
ax1.scatter(Per_x,MSD_2,linewidth=6.0,label='IDR2')
ax1.scatter(Per_x,MSD_llps,linewidth=6.0,label='Condensate')
ax1.scatter(Per_x,MSD_single,linewidth=6.0,label='Free state')
ax1.plot(Per_x,MSD_0,linewidth=6.0,label='IDR1')
ax1.plot(Per_x,MSD_1,linewidth=6.0,label='Helix')
ax1.plot(Per_x,MSD_2,linewidth=6.0,label='IDR2')
ax1.plot(Per_x,MSD_llps,linewidth=6.0,label='Condensate')
ax1.plot(Per_x,MSD_single,linewidth=6.0,label='Free state')

plt.yscale('log')

plt.xlabel('Percent',size=40,labelpad=10,fontproperties='calibri')
plt.ylabel('D'+' ('+u'$\mathregular{nm^2}$'+'/ns)',size=40,labelpad=10,fontproperties='Arial')
plt.xticks(fontproperties="Arial",size=36)
plt.yticks(fontproperties="Arial",size=36)

# plt.text(0.2, 60, 'Condensate', fontsize=28, color='darkgreen', fontproperties='Arial')
# plt.text(0.2, 300, 'Free state', fontsize=28, color='orange', fontproperties='Arial')

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
plt.savefig('MSD_4R_Per_D.png',dpi=1000,bbox_inches='tight')