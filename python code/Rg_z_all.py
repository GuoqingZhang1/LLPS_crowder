import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math

fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',8)

for Per in [0,5,10,15,20,25,30]:
    f=open('../Crowd_%d/Rg_z_llps.txt' %(Per),'r')
    line=f.readlines()

    x_z=[]
    Rg_z=[]

    for i in range(len(line)):
        ss=line[i].split()
        if float(ss[2])>=10000:
            x_z.append(float(ss[0]))
            Rg_z.append(0.1*float(ss[1])/float(ss[2]))

# f_2=open('Rg_llps.txt','r')
# line_2=f_2.readlines()



    plt.plot(x_z,Rg_z,color=cmap((float(Per)+5)/40),linewidth=4.0)

plt.ylim([2.3,4.2])
plt.xlim([-250,250])
plt.xticks([-250,-150,-50,50,150,250],['0','10','20','30','40','50'],fontproperties='Arial',fontsize=36)
plt.yticks([2.5,3.0,3.5,4.0],fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
plt.xlabel('z (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel(u'$\mathregular{R_{g}}$'+' (nm)',labelpad=10,fontproperties='Arial',size=40)
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
fig.set_size_inches(8,6)
plt.savefig('Rg_z_all.png',dpi=1000,bbox_inches='tight')