import matplotlib.pyplot as plt #绘图
import numpy as np #矩阵


tau_e=[]
std=[]
Per_x=[]


for Per in [5,10,15,20,25,30]:
    f_llps=open('Rg_per_in_%d.txt' %(Per*10),"r" )
    line_llps = f_llps.readlines() # 以行的形式进行读取文件
    Lmax_llps = len(line_llps)

    tau_llps=[]
    for i in range(Lmax_llps):
        ss=line_llps[i].split()
        tau_llps.append(float(ss[0]))

    tau_e.append(np.mean(tau_llps))
    std.append(np.std(tau_llps))
    Per_x.append(Per)

fig = plt.figure(dpi=1000,figsize=(8,6))
plt.rcParams['font.sans-serif'] ='Arial'
ax1 = fig.gca()
ax1.scatter(Per_x,tau_e,s=100)
ax1.plot(Per_x,tau_e,linewidth=6.0)
# ax1.plot(0.1*np.arange(Lmax_llps),MSD_single,linewidth=6.0,color='darkgreen',label='Free state')
# plt.plot(xx,np.exp(y(np.log(xx),a_llps,b_llps)),linewidth=6.0,label='Condensate')
# plt.plot(xx,np.exp(y(np.log(xx),a_single,b_single)),linewidth=6.0,label='Free state')

plt.xlabel('Percent',size=40,labelpad=10,fontproperties='Arial')
plt.ylabel(chr(964)+' (ns)',size=40,labelpad=10,fontproperties='calibri')
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
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(8,6)
plt.savefig('Rg_in_Per.png',dpi=1000,bbox_inches='tight')