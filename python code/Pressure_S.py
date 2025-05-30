import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵

f=open('Stress.txt','r')
line=f.readlines()

Px=np.zeros([500])
Py=np.zeros([500])
Pz=np.zeros([500])

begin=100
end=501

for j in range(end-begin):
    for i in range(500):
        ss=line[i+4+501*j].split()
        Px[i]+=float(ss[3])/(end-begin)
        Py[i]+=float(ss[4])/(end-begin)
        Pz[i]+=float(ss[5])/(end-begin)

fig=plt.figure(figsize=(8,6),dpi=1000)
plt.plot(np.arange(500),Px,linewidth=4.0,label='x')
plt.plot(np.arange(500),Py,linewidth=4.0,label='y')
plt.plot(np.arange(500),Pz,linewidth=4.0,label='z')

# plt.ylim([0,0.015])
# plt.xlim([0,500])
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')

plt.xlabel(' (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

fig.set_size_inches(8,6)
plt.savefig('Pressure_S.png',dpi=1000,bbox_inches='tight')
