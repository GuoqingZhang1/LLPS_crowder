import numpy as np
import matplotlib.pyplot as plt #绘图

Qmean_12=[]
Qmean_1h=[]
Qmean_hh=[]

Qstd_12=[]
Qstd_1h=[]
Qstd_hh=[]

taumean_12=[]
taumean_1h=[]
taumean_hh=[]

taustd_12=[]
taustd_1h=[]
taustd_hh=[]


for Per in [0,5,10,15,20,25,30]:
    Q_12=np.load(file='../Crowd_%d/Q_12.npy' %(Per))
    Q_1h=np.load(file='../Crowd_%d/Q_1h.npy' %(Per))
    Q_hh=np.load(file='../Crowd_%d/Q_hh.npy' %(Per))

    tau_12=np.load(file='../Crowd_%d/tau_12.npy' %(Per))
    tau_1h=np.load(file='../Crowd_%d/tau_1h.npy' %(Per))
    tau_hh=np.load(file='../Crowd_%d/tau_hh.npy' %(Per))

    Qmean_12.append(np.mean(Q_12))
    Qmean_1h.append(np.mean(Q_1h))
    Qmean_hh.append(np.mean(Q_hh))

    Qstd_12.append(np.std(Q_12)/len(Q_12)**0.5)
    Qstd_1h.append(np.std(Q_1h)/len(Q_1h)**0.5)
    Qstd_hh.append(np.std(Q_hh)/len(Q_hh)**0.5)  

    taumean_12.append(np.mean(tau_12))
    taumean_1h.append(np.mean(tau_1h))
    taumean_hh.append(np.mean(tau_hh))

    taustd_12.append(np.std(tau_12)/len(tau_12)**0.5)
    taustd_1h.append(np.std(tau_1h)/len(tau_1h)**0.5)
    taustd_hh.append(np.std(tau_hh)/len(tau_hh)**0.5)  

Per_x=[0,5,10,15,20,25,30]

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap = plt.get_cmap('Blues')
# 计算每个点的颜色
colors = cmap(np.linspace(0, 1, 8))

for i in range(len(Qmean_12)):
    Qmean_hh[i]=Qmean_hh[i]-0.0053

plt.hlines(y=0.0014,xmin=-1,xmax=31,linewidth=3,color='black')
plt.hlines(y=0.0016,xmin=-1,xmax=31,linewidth=3,color='black')
plt.errorbar(Per_x,Qmean_12,fmt='o-',mfc=rgb_to_hex((143,195,31)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)
# plt.errorbar(Per_x,Qmean_1h,yerr=Qstd_1h,fmt='o-',mfc=rgb_to_hex((146,7,131)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)
plt.errorbar(Per_x,Qmean_hh,fmt='o-',mfc=rgb_to_hex((232,56,40)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)
# for i in range(7):
#     plt.plot(Per_x[i:i+2],Qmean_12[i:i+2],color=colors[i+1],linewidth=4.0,zorder=1)
#     plt.plot(Per_x[i:i+2],Qmean_1h[i:i+2],color=colors[i+1],linewidth=4.0,zorder=1)
#     plt.plot(Per_x[i:i+2],Qmean_hh[i:i+2],color=colors[i+1],linewidth=4.0,zorder=1)
plt.xticks([0,10,20,30],fontproperties='Arial',fontsize=36)
plt.yticks([0.0010,0.0012,0.0014,0.0016,0.0018,0.0020],['1','1.2','1.4','6.9','7.1','7.3'],fontproperties='Arial',fontsize=36)
plt.xlim(-1,31)
# plt.ylim(0.000,0.008)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
plt.xlabel('C'+'$\mathregular{_{Att}}$'+' (%)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Q ('+'$\\times$'+'$\mathregular{10^{-3}}$)',fontproperties='Arial',labelpad=10,size=40)

# plt.errorbar(-10,1,yerr=1,fmt='s-',color='black',label='IDR-IDR',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)
# plt.errorbar(-10,1,yerr=1,fmt='^-',color='black',label='IDR-Helix',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)
# plt.errorbar(-10,1,yerr=1,fmt='d-',color='black',label='Helix-Helix',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)

# plt.legend(prop = {'size':24,'family':'Arial'},frameon=False,edgecolor ='black')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)


fig.set_size_inches(8,6)
plt.savefig('Q_per.png',bbox_inches='tight',dpi=1000)

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap = plt.get_cmap('Blues')
# 计算每个点的颜色
colors = cmap(np.linspace(0, 1, 8))

plt.errorbar(Per_x,taumean_12,fmt='o-',mfc=rgb_to_hex((143,195,31)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)
# plt.errorbar(Per_x,taumean_1h,yerr=taustd_1h,fmt='o-',mfc=rgb_to_hex((146,7,131)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)
plt.errorbar(Per_x,taumean_hh,fmt='o-',mfc=rgb_to_hex((232,56,40)),mec='black',mew=3,elinewidth=3, ecolor='black',color='black',linewidth=3.0,capthick=12, capsize=8,markersize=16,zorder=2)

# for i in range(7):
#     plt.errorbar(Per_x[i:i+2],taumean_12[i:i+2],yerr=taustd_12[i:i+2],color=colors[i+1],fmt='s-',mec='black', mew=2 ,markersize=16,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=10)
#     plt.errorbar(Per_x[i:i+2],taumean_1h[i:i+2],yerr=taustd_1h[i:i+2],color=colors[i+1],fmt='^-',mec='black', mew=2 ,markersize=16,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=10)
#     plt.errorbar(Per_x[i:i+2],taumean_hh[i:i+2],yerr=taustd_hh[i:i+2],color=colors[i+1],fmt='d-',mec='black', mew=2 ,markersize=16,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=10)
plt.xticks([0,10,20,30],fontproperties='Arial',fontsize=36)
plt.yticks([1,3,5],fontproperties='Arial',fontsize=36)
plt.xlim(-1,31)
# plt.ylim(2.9,7.1)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
plt.xlabel('C'+'$\mathregular{_{Att}}$'+' (%)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(chr(964)+' (ns)',fontproperties='calibri',labelpad=10,size=40)

# plt.errorbar(-10,1,yerr=1,fmt='s-',color='black',label='IDR-IDR',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)
# plt.errorbar(-10,1,yerr=1,fmt='^-',color='black',label='IDR-Helix',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)
# plt.errorbar(-10,1,yerr=1,fmt='d-',color='black',label='Helix-Helix',markersize=12,linewidth=4.0,elinewidth=3.0,capthick=3.0,capsize=8)

# plt.legend(prop = {'size':28,'family':'Arial'},frameon=False,edgecolor ='black',loc='upper left')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)


fig.set_size_inches(8,6)
plt.savefig('tau_per.png',bbox_inches='tight',dpi=1000)
