import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from scipy import optimize as op
from matplotlib.colors import LogNorm

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
        # if np.max(Qt[:,i,j])>0 and np.min(Qt[:,i,j])==0:
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
        
            Q_12.append(float(Q_mean[3*j+0][3*k+0]))
            tau_12.append(float(Tau[3*j+0][3*k+0]))

            Q_12.append(float(Q_mean[3*j+0][3*k+2]))
            tau_12.append(float(Tau[3*j+0][3*k+2]))

            Q_12.append(float(Q_mean[3*j+2][3*k+0]))
            tau_12.append(float(Tau[3*j+2][3*k+0]))

            Q_12.append(float(Q_mean[3*j+2][3*k+2]))
            tau_12.append(float(Tau[3*j+2][3*k+2]))

            Q_1h.append(float(Q_mean[3*j+0][3*k+1]))
            tau_1h.append(float(Tau[3*j+0][3*k+1]))

            Q_1h.append(float(Q_mean[3*j+1][3*k+0]))
            tau_1h.append(float(Tau[3*j+1][3*k+0]))

            Q_1h.append(float(Q_mean[3*j+1][3*k+2]))
            tau_1h.append(float(Tau[3*j+1][3*k+2]))

            Q_1h.append(float(Q_mean[3*j+2][3*k+1]))
            tau_1h.append(float(Tau[3*j+2][3*k+1]))

            Q_hh.append(float(Q_mean[3*j+1][3*k+1]))
            tau_hh.append(float(Tau[3*j+1][3*k+1]))

# for j in range(99):
#     for k in range(j,100):
        
#         if  Tau[3*j+0][3*k+0]>0:

#             Q_12.append(float(Q_mean[3*j+0][3*k+0]))
#             tau_12.append(float(Tau[3*j+0][3*k+0]))

#         if  Tau[3*j+0][3*k+2]>0:

#             Q_12.append(float(Q_mean[3*j+0][3*k+2]))
#             tau_12.append(float(Tau[3*j+0][3*k+2]))

#         if  Tau[3*j+2][3*k+0]>0:

#             Q_12.append(float(Q_mean[3*j+2][3*k+0]))
#             tau_12.append(float(Tau[3*j+2][3*k+0]))

#         if  Tau[3*j+2][3*k+2]>0:

#             Q_12.append(float(Q_mean[3*j+2][3*k+2]))
#             tau_12.append(float(Tau[3*j+2][3*k+2]))

#         if  Tau[3*j+0][3*k+1]>0:

#             Q_1h.append(float(Q_mean[3*j+0][3*k+1]))
#             tau_1h.append(float(Tau[3*j+0][3*k+1]))

#         if  Tau[3*j+1][3*k+0]>0:

#             Q_1h.append(float(Q_mean[3*j+1][3*k+0]))
#             tau_1h.append(float(Tau[3*j+1][3*k+0]))

#         if  Tau[3*j+1][3*k+2]>0:

#             Q_1h.append(float(Q_mean[3*j+1][3*k+2]))
#             tau_1h.append(float(Tau[3*j+1][3*k+2]))

#         if  Tau[3*j+2][3*k+1]>0:

#             Q_1h.append(float(Q_mean[3*j+2][3*k+1]))
#             tau_1h.append(float(Tau[3*j+2][3*k+1]))

#         if  Tau[3*j+1][3*k+1]>0:

#             Q_hh.append(float(Q_mean[3*j+1][3*k+1]))
#             tau_hh.append(float(Tau[3*j+1][3*k+1]))

np.save(file="Q_hh.npy", arr=Q_hh)
np.save(file="Q_1h.npy", arr=Q_1h)
np.save(file="Q_12.npy", arr=Q_12)

np.save(file="tau_hh.npy", arr=tau_hh)
np.save(file="tau_1h.npy", arr=tau_1h)
np.save(file="tau_12.npy", arr=tau_12)


k_12,b_12=op.curve_fit(f_tau_Q,np.log10(Q_12),np.log10(tau_12),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

k_1h,b_1h=op.curve_fit(f_tau_Q,np.log10(Q_1h),np.log10(tau_1h),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

k_hh,b_hh=op.curve_fit(f_tau_Q,np.log10(Q_hh),np.log10(tau_hh),maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

np.savetxt('IDR12.txt', np.c_[[k_12,b_12]],fmt='%f',delimiter='\t')
np.savetxt('IDR1h.txt', np.c_[[k_1h,b_1h]],fmt='%f',delimiter='\t')
np.savetxt('IDRhh.txt', np.c_[[k_hh,b_hh]],fmt='%f',delimiter='\t')

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

plt.scatter(Q_12,tau_12,marker='o',s=150,label='IDR-IDR')

xx=np.arange(np.min(Q_12),np.max(Q_12),0.0000000001)

plt.plot(xx,np.power(10,(f_tau_Q(np.log10(xx),k_12,b_12))),color='black',linestyle='--',linewidth=4.0,zorder=1)

plt.xlabel("Q",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+' (ns)',labelpad=10,size=40,fontproperties='calibri')
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

plt.xscale('log')
plt.yscale('log')
plt.ylim(0.1,100)
plt.xlim(0.0000001,0.01)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('Q_tau_12_%d.png' %(Per),bbox_inches='tight',dpi=1000)
plt.close()

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

plt.scatter(Q_1h,tau_1h,marker='^',s=150,label='IDR-Helix')

xx=np.arange(np.min(Q_1h),np.max(Q_1h),0.0000000001)
plt.plot(xx,np.power(10,(f_tau_Q(np.log10(xx),k_1h,b_1h))),color='black',linestyle='--',linewidth=4.0,zorder=1)

plt.xlabel("Q",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+' (ns)',labelpad=10,size=40,fontproperties='calibri')
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

plt.xscale('log')
plt.yscale('log')
plt.ylim(0.1,100)
plt.xlim(0.0000001,0.01)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('Q_tau_1h_%d.png' %(Per),bbox_inches='tight',dpi=1000)
plt.close()

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

plt.scatter(Q_hh,tau_hh,marker='d',s=150,label='Helix-Helix')

xx=np.arange(np.min(Q_hh),np.max(Q_hh),0.0000000001)
plt.plot(xx,np.power(10,(f_tau_Q(np.log10(xx),k_hh,b_hh))),color='black',linestyle='--',linewidth=4.0,zorder=1)

plt.xlabel("Q",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(964)+' (ns)',labelpad=10,size=40,fontproperties='calibri')
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

plt.xscale('log')
plt.yscale('log')
plt.ylim(0.1,100)
plt.xlim(0.0000001,0.01)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('Q_tau_hh_%d.png' %(Per),bbox_inches='tight',dpi=1000)
plt.close()


fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

plt.scatter(Q_12_intra,tau_12_intra,marker='o',s=150,label='IDR-IDR')


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
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('Q_tau_12_intra_%d.png' %(Per),bbox_inches='tight',dpi=1000)
plt.close()

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)

plt.scatter(Q_1h_intra,tau_1h_intra,marker='^',s=150,label='IDR-Helix')


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
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('Q_tau_1h_intra_%d.png' %(Per),bbox_inches='tight',dpi=1000)
plt.close()

