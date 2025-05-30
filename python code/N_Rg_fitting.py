import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
from sklearn.metrics import mean_squared_error 
from sklearn.linear_model import LinearRegression
import scipy.optimize as op

begin=10000
Timeall=90000

def y(x,k,b):
    return k*x+b

N_per=np.zeros((6,2))

N_in=np.zeros((6))

Rg=np.zeros((6))

i_p=0

for Per in [0.05,0.10,0.15,0.20,0.25,0.30]:

    f_pro=open('../trj/tdp43_%.2f_nopb/N_in_out.txt' %(Per),'r')
    line_pro=f_pro.readlines()


    N_per[i_p][0]=(float(line_pro[0])/(float(line_pro[0])+float(line_pro[1])))
    N_per[i_p][1]=(float(line_pro[1])/(float(line_pro[0])+float(line_pro[1])))

    N_in[i_p]=((float(line_pro[0])/(float(line_pro[0])+float(line_pro[1]))))

    f_Rg=open('../../Single/Rg_llps_%d.txt' %(Per*1000),'r')
    line_Rg=f_Rg.readlines()

    Rg_per=[]
    for i in range(len(line_Rg)):
        Rg_per.append(float(line_Rg[i]))

    Rg[i_p]=(0.1*np.mean(Rg_per))
    i_p+=1


# Rg=Rg/np.mean(Rg)
# N_per[:,0]=N_per[:,0]/np.mean(N_per[:,0])
# N_per[:,1]=N_per[:,1]/np.mean(N_per[:,1])

k,b=op.curve_fit(y,N_in,Rg,maxfev = 100000000)[0]


fig=plt.figure(figsize=(8,6),dpi=1000)

plt.scatter(100*N_in,Rg,color='black',label='Data',s=150)
plt.plot(100*N_in,y(N_in,k,b),'-',linewidth=4.0,color='red',label='Fit')

plt.xlabel("$\mathregular{P^{N}_{in}}$"+' (%)',size=40,labelpad=10,fontproperties="Arial")
plt.ylabel('$\mathregular{R_{g}}$'+' (nm)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  

# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
# plt.xlim(0,1)
# plt.ylim(0,0.01)

bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24

fig.set_size_inches(8,6)
plt.savefig('N_Rg_fitting.png',bbox_inches='tight',dpi=1000)