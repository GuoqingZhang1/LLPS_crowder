import numpy as np
import math
import matplotlib.pyplot as plt #绘图

begintime=10000
Timeall=20001-1

Crosstime=0.15

line_n=10

f=open('Corr_Rg.txt','r')
line=f.readlines()
Lmax=len(line)

Rg_t=np.zeros([100,Timeall-begintime])

for i in range(Timeall-begintime):
    for j in range(100):
        ss=line[i].split()
        Rg_t[j][i]=float(ss[j])

tau=np.zeros([100])

for i in range(100):
    tau0=0
    for j in range(Timeall-begintime):
        if Rg_t[i][j]<Crosstime:
            tau0=j
            break
    
    tau[i]=tau0

fig = plt.figure(dpi=1000,figsize=(8,6))
plt.plot(0.1*np.arange(Timeall-begintime),Rg_t[line_n])
plt.xlabel('Lag time, '+chr(964)+' (ns)',size=40,labelpad=10,fontproperties='calibri')
plt.ylabel('Autocorrelation'+' ('+u'$\mathregular{nm^2}$)',size=40,labelpad=10,fontproperties='Arial')
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks([-0.2,0.2,0.6,1.0],fontproperties='Arial',fontsize=36)
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
plt.savefig('Corr_Rg_t_%d.png' %(line_n),dpi=1000,bbox_inches='tight')

np.savetxt('Corr_Rg_tau.txt', np.c_[tau],fmt='%f',delimiter='\t')