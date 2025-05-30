import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=PERCENT
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

begintime=10000
Timeall=20001-1

Corr_3R=np.load(file='Corr_3R_Nc.npy')

Corr_12=[]
Corr_13=[]
Corr_23=[]
for i in range(Timeall-begintime):
    Corr_12.append(Corr_3R[i][0][298])
    Corr_13.append(Corr_3R[i][0][299])
    Corr_23.append(Corr_3R[i][1][298])

print(Corr_12)
print(Corr_13)
print(Corr_23)

fig = plt.figure(dpi=1000,figsize=(8,6))
plt.plot(0.1*np.arange(Timeall-begintime),Corr_12,linewidth=6.0,label='Corr_12')
plt.plot(0.1*np.arange(Timeall-begintime),Corr_23,linewidth=6.0,label='Corr_23')
plt.plot(0.1*np.arange(Timeall-begintime),Corr_13,linewidth=6.0,label='Corr_13')   

plt.xscale('log')
plt.ylim(-0.22,1.02)

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
plt.savefig('Corr_3R_t_%d.png' %(Per),dpi=1000,bbox_inches='tight')