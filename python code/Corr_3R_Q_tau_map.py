import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt #绘图
from scipy import optimize as op
from matplotlib.colors import LogNorm
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

Per=PERCENT

begintime=10000
Timeall=20001-1

def f(t,tau):
    return np.exp(-t/tau)

def f_tau_Q(x,k,b):
    return k*x+b

Corr_3R=np.load(file='Corr_3R_Nc.npy')

Q_mean=np.load(file='Qij_Nc.npy')

Qt=np.load(file='Qt_Nc.npy')

Inter=np.zeros([3,3])

Intra=np.zeros([3,3])
 
Tau=np.zeros([300,300])

t_x=np.arange(Timeall-begintime)



for i in range(300):
    for j in range(300):
        
        # tau=0
        # if np.max(Qt[:,i,j])>0 and np.min(Qt[:,i,j])==0:
        #     for k in range(Timeall-begintime):
        #         tau+=Corr_3R[k][i][j]*0.1
        
        # Tau[i][j]=tau

        tau=0
        if np.max(Qt[:,i,j])>0:
            tau=op.curve_fit(f,t_x,Corr_3R[:,i,j],maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

        Tau[i][j]=0.1*tau
        # tau=0
        # if np.max(Qt[:,i,j])>0 and np.min(Qt[:,i,j])==0:
        #     for k in range(Timeall-begintime):
        #         if Corr_3R[k][i][j]<0:
        #             tau=0.1*k
        #             break
        
        # Tau[i][j]=tau

Q_12=[]
tau_12=[]

Q_1h=[]
tau_1h=[]

Q_hh=[]
tau_hh=[]

Q_12_intra=[]
tau_12_intra=[]

Q_1h_intra=[]
tau_1h_intra=[]



for i in range(100):
        
    if  Tau[3*i+0][3*i+1]>0:

        Q_1h_intra.append(float(Q_mean[3*i+0][3*i+1]))
        tau_1h_intra.append(float(Tau[3*i+0][3*i+1]))

    if  Tau[3*i+0][3*i+2]>0:

        Q_12_intra.append(float(Q_mean[3*i+0][3*i+2]))
        tau_12_intra.append(float(Tau[3*i+0][3*i+2]))

    if  Tau[3*i+1][3*i+2]>0:

        Q_1h_intra.append(float(Q_mean[3*i+1][3*i+2]))
        tau_1h_intra.append(float(Tau[3*i+1][3*i+2]))



for j in range(99):
    for k in range(j,100):
        
        if  Tau[3*j+0][3*k+0]>0:

            Q_12.append(float(Q_mean[3*j+0][3*k+0]))
            tau_12.append(float(Tau[3*j+0][3*k+0]))

        if  Tau[3*j+0][3*k+2]>0:

            Q_12.append(float(Q_mean[3*j+0][3*k+2]))
            tau_12.append(float(Tau[3*j+0][3*k+2]))

        if  Tau[3*j+2][3*k+0]>0:

            Q_12.append(float(Q_mean[3*j+2][3*k+0]))
            tau_12.append(float(Tau[3*j+2][3*k+0]))

        if  Tau[3*j+2][3*k+2]>0:

            Q_12.append(float(Q_mean[3*j+2][3*k+2]))
            tau_12.append(float(Tau[3*j+2][3*k+2]))

        if  Tau[3*j+0][3*k+1]>0:

            Q_1h.append(float(Q_mean[3*j+0][3*k+1]))
            tau_1h.append(float(Tau[3*j+0][3*k+1]))

        if  Tau[3*j+1][3*k+0]>0:

            Q_1h.append(float(Q_mean[3*j+1][3*k+0]))
            tau_1h.append(float(Tau[3*j+1][3*k+0]))

        if  Tau[3*j+1][3*k+2]>0:

            Q_1h.append(float(Q_mean[3*j+1][3*k+2]))
            tau_1h.append(float(Tau[3*j+1][3*k+2]))

        if  Tau[3*j+2][3*k+1]>0:

            Q_1h.append(float(Q_mean[3*j+2][3*k+1]))
            tau_1h.append(float(Tau[3*j+2][3*k+1]))

        if  Tau[3*j+1][3*k+1]>0:

            Q_hh.append(float(Q_mean[3*j+1][3*k+1]))
            tau_hh.append(float(Tau[3*j+1][3*k+1]))


Q_hhx = np.hstack((Q_hh, Q_hh))  # 合并数据
Q_hhxx=np.hstack((Q_hhx,Q_hhx))

tau_hhx = np.hstack((tau_hh, tau_hh))  # 合并数据
tau_hhxx=np.hstack((tau_hhx,tau_hhx))

k_12,b_12=op.curve_fit(f_tau_Q,np.log10(Q_12),np.log10(tau_12),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

# k_1h,b_1h=op.curve_fit(f_tau_Q,np.log10(Q_1h),np.log10(tau_1h),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

k_hh,b_hh=op.curve_fit(f_tau_Q,np.log10(Q_hhxx),np.log10(tau_hhxx),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]


fig=plt.figure(figsize=(8, 6),dpi=1000)

# brown_colors = ["#ffffff", "#8B4513"]  # 从白色到棕色

# # 创建自定义的colormap
# brown_cmap = LinearSegmentedColormap.from_list("brown_cmap", brown_colors)

ax = sns.kdeplot(x=np.log10(Q_hhxx),y=np.log10(tau_hhxx),kind='kde', cmap="YlOrRd")
# ax = sns.kdeplot(x=np.log10(Q_1h),y=np.log10(tau_1h),kind='kde', cmap="Purples")
ax = sns.kdeplot(x=np.log10(Q_12),y=np.log10(tau_12),kind='kde', cmap="Greens")

xx=np.arange(-5,-2,0.01)

plt.plot(xx,(f_tau_Q(xx,k_hh,b_hh)),color='orange',linestyle='--',linewidth=4.0,zorder=1)
plt.plot(xx,(f_tau_Q(xx,k_12,b_12)),color='green',linestyle='--',linewidth=4.0,zorder=1)

# plt.errorbar(np.log10(np.mean(Q_hhxx)), np.log10(np.mean(tau_hhxx)), fmt='o',mfc='orange',mec='black',mew=2,elinewidth=2, ecolor='black',capthick=12, capsize=8,markersize=16,zorder=2)
# plt.errorbar(np.log10(np.mean(Q_12)), np.log10(np.mean(tau_12)), fmt='o',mfc='green',mec='black',mew=2,elinewidth=2, ecolor='black',capthick=12, capsize=8,markersize=16,zorder=2)

# g = sns.JointGrid(x=np.log10(Q_12), y=np.log10(tau_12))
# g.plot_joint(sns.kdeplot, fill=True, cmap='Blues', alpha=0.5)
# g.plot_marginals(sns.kdeplot, color='blue', alpha=0.5)

# # 绘制第二个数据集的KDE和边缘分布
# sns.kdeplot(x=np.log10(Q_1h), y=np.log10(tau_1h), fill=True, cmap='Greens', alpha=0.5, ax=g.ax_joint)
# sns.kdeplot(x=np.log10(Q_1h), color='green', ax=g.ax_marg_x, alpha=0.5)
# sns.kdeplot(y=np.log10(tau_1h), color='green', ax=g.ax_marg_y, alpha=0.5)

# # 绘制第三个数据集的KDE和边缘分布
# sns.kdeplot(x=np.log10(Q_hh), y=np.log10(tau_hh), fill=True, cmap='Reds', alpha=0.5, ax=g.ax_joint)
# sns.kdeplot(x=np.log10(Q_hh), color='red', ax=g.ax_marg_x, alpha=0.5) 
# sns.kdeplot(y=np.log10(tau_hh), color='red', ax=g.ax_marg_y, alpha=0.5)
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.tick_params(length=7,pad=10,width = 3,direction='in')

plt.xlabel("Q",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+' (ns)',labelpad=10,size=40,fontproperties='calibri')
plt.xticks([-5,-4,-3,-2],['$\mathregular{10^{-5}}$','$\mathregular{10^{-4}}$','$\mathregular{10^{-3}}$','$\mathregular{10^{-2}}$'],fontproperties='Arial',fontsize=36)
plt.yticks([-1,0,1,2],['$\mathregular{10^{-1}}$','$\mathregular{10^{0}}$','$\mathregular{10^{1}}$','$\mathregular{10^{2}}$'],fontproperties='Arial',fontsize=36)
plt.xlim(-5,-2)
plt.ylim(-1,2)
fig.set_size_inches(8,6)
plt.savefig('Map_Q_tau_%d.png' %(Per),bbox_inches='tight',dpi=1000)
