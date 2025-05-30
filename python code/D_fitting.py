import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from scipy import optimize as op

f=open('MSD_line.txt','r')
line=f.readlines()

begintime=10000
Timeall=20001-1

def y(x,k,b):
    return k*x+b

MSD=np.zeros([100,Timeall-begintime])

for i in range(Timeall-begintime):
    ss=line[i].split()
    for j in range(100):
        MSD[j][i]=float(ss[j])

al=[]
D=[]
for i in range(100):
    KK,BB=op.curve_fit(y,np.log(0.1*np.arange(Timeall-begintime)[1:100]),np.log(0.01*MSD[i,1:100]))[0]
    al.append(KK)
    D.append(np.exp(BB)/6)

np.savetxt('alpha_fitting.txt', np.c_[al],fmt='%f',delimiter='\t')
np.savetxt('D_fitting.txt', np.c_[D],fmt='%f',delimiter='\t')

r_i=np.random.randint(0,99)

fig,ax=plt.subplots(figsize=(8,6),dpi=1000)

plt.scatter(np.log10(0.1*np.arange(Timeall-begintime)),np.log10(0.01*MSD[r_i]),marker='o',s=150,label='IDR-IDR')

plt.plot(np.log10(0.1*np.arange(Timeall-begintime)[1:100]),np.log10(np.exp(y(np.log(0.1*np.arange(Timeall-begintime)),al[r_i],np.log(6*D[r_i]))[1:100])),color='black',linestyle='--',linewidth=4.0,zorder=1)

plt.xlabel(chr(964),size=40,labelpad=10,fontproperties='calibri')
plt.ylabel('D',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')
fig.set_size_inches(10,6)
plt.savefig('D_fitting_%d.png',bbox_inches='tight',dpi=1000)
plt.close()
