import matplotlib.pyplot as plt #绘图
import matplotlib as mpl

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

cmap1=plt.get_cmap('Blues',8)
for Per in [0,5,10,15,20,25,30]:
    f_Q=open('../Crowd_%d/Inter_Qij.txt' %(Per),'r')
    line_Q=f_Q.readlines()

    f_tau=open('../Crowd_%d/Inter_tau.txt' %(Per),'r')
    line_tau=f_tau.readlines()

    Q_12=[]
    tau_12=[]

    Q_1h=[]
    tau_1h=[]

    Q_hh=[]
    tau_hh=[]

    Q_12.append(float(line_Q[0].split()[0]))
    tau_12.append(float(line_tau[0].split()[0]))

    Q_12.append(float(line_Q[0].split()[2]))
    tau_12.append(float(line_tau[0].split()[2]))

    Q_12.append(float(line_Q[2].split()[0]))
    tau_12.append(float(line_tau[2].split()[0]))

    Q_12.append(float(line_Q[2].split()[2]))
    tau_12.append(float(line_tau[2].split()[2]))

    Q_1h.append(float(line_Q[0].split()[1]))
    tau_1h.append(float(line_tau[0].split()[1]))

    Q_1h.append(float(line_Q[1].split()[0]))
    tau_1h.append(float(line_tau[1].split()[0]))

    Q_1h.append(float(line_Q[1].split()[2]))
    tau_1h.append(float(line_tau[1].split()[2]))

    Q_1h.append(float(line_Q[2].split()[1]))
    tau_1h.append(float(line_tau[2].split()[1]))

    Q_hh.append(float(line_Q[1].split()[1]))
    tau_hh.append(float(line_tau[1].split()[1]))

    plt.scatter(Q_12,tau_12,marker='o',s=150,color=cmap1((Per+5)/40))
    plt.scatter(Q_1h,tau_1h,marker='^',s=150,color=cmap1((Per+5)/40))
    plt.scatter(Q_hh,tau_hh,marker='d',s=150,color=cmap1((Per+5)/40))

plt.xlabel("Q",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+' (ns)',labelpad=10,size=40,fontproperties='calibri')
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

plt.xscale('log')
plt.yscale('log')
# plt.xlim(0,50)
# plt.ylim(-0.05,1.8)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

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

fig.set_size_inches(10,6)
plt.savefig('Q_tau.png',bbox_inches='tight',dpi=1000)