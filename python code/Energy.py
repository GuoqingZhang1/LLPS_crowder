import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵

f_pro=open('Energy_pro.txt','r')
line_pro=f_pro.readlines()

E_pro=np.zeros([500])

f_cro=open('Energy_cro.txt','r')
line_cro=f_cro.readlines()

E_cro=np.zeros([500])

begin=100
end=501

for j in range(end-begin):
    for i in range(500):
        ss_pro=line_pro[i+4+501*j].split()
        ss_cro=line_cro[i+4+501*j].split()
        if float(ss_pro[3])!=0:
            E_pro[i]+=float(ss_pro[3])/(float(ss_pro[2])*(end-begin))
        if float(ss_cro[3])!=0:
            E_cro[i]+=float(ss_cro[3])/(float(ss_cro[2])*(end-begin))

fig=plt.figure(figsize=(8,6),dpi=1000)  
plt.plot(np.arange(500),E_pro,linewidth=4.0,label='pro')


# plt.ylim([0,0.015])
# plt.xlim([0,500])
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')

plt.xlabel('z',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Energy',labelpad=10,fontproperties='Arial',size=40)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

fig.set_size_inches(8,6)
plt.savefig('Energy_pro.png',dpi=1000,bbox_inches='tight')


fig=plt.figure(figsize=(8,6),dpi=1000)  
plt.plot(np.arange(500),E_cro,linewidth=4.0,label='cro')

# plt.ylim([0,0.015])
# plt.xlim([0,500])
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')

plt.xlabel('z',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Energy',labelpad=10,fontproperties='Arial',size=40)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

fig.set_size_inches(8,6)
plt.savefig('Energy_cro.png',dpi=1000,bbox_inches='tight')
