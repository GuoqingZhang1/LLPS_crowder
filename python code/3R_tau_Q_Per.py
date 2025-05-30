import numpy as np
import math
import matplotlib.pyplot as plt #绘图 

def f(x,k,b):
    return k*x+b

xx=np.arange(0.0000001,0.01,0.0000001)

fig,ax=plt.subplots(figsize=(10,6),dpi=1000)
cmap1=plt.get_cmap('Blues',8)


for Per in [0,5,10,15,20,25,30]:
    f_12=open('../Crowd_%d/IDR12.txt' %(Per),"r" )
    line_12=f_12.readlines()
    f_1h=open('../Crowd_%d/IDR1h.txt' %(Per),"r" )
    line_1h=f_1h.readlines()
    f_hh=open('../Crowd_%d/IDRhh.txt' %(Per),"r" )
    line_hh=f_hh.readlines()

    plt.plot(xx,np.exp(f(np.log(xx),float(line_12[0]),float(line_12[1]))),linestyle='-',linewidth=4.0,color=cmap1((Per+5)/40))
    plt.plot(xx,np.exp(f(np.log(xx),float(line_1h[0]),float(line_1h[1]))),linestyle='-.',linewidth=4.0,color=cmap1((Per+5)/40))
    plt.plot(xx,np.exp(f(np.log(xx),float(line_hh[0]),float(line_hh[1]))),linestyle='--',linewidth=4.0,color=cmap1((Per+5)/40))
    

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

fig.set_size_inches(10,6)
plt.savefig('Q_tau_Per.png',bbox_inches='tight',dpi=1000)
plt.close()