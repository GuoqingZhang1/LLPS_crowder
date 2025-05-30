import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
import scipy.optimize as op

def dU (x,a1,a2,a3,k1,k2):
    return a1*(k1**(x**2/2)-1)*k1**(x**2)+a2*(k2**(x**2/2)-1)*k2**(x**2)+a3*np.log(x+1)

N=8

Rg_y=[]
Per_x=[]

Rg_0=0
for Per in ['0','1','5','10','15','20','30','40','50','100','150','200','250','300']:
    f_pro=open('Rg_llps_'+Per+'.txt','r')
    line_pro=f_pro.readlines()

    Rg=[]

    for i in range(len(line_pro)):
        Rg.append(float(line_pro[i]))

    if Per=='0':
        Rg_0=np.mean(Rg)
    
    Rg_y.append((np.mean(Rg)-Rg_0)/Rg_0)
    Per_x.append(float(Per)*0.001)

A1,A2,A3,K1,K2=op.curve_fit(dU,Per_x,Rg_y,p0=[-0.8,-0.5,-0.6,5.566e-12,8.907e-11],bounds=([-np.inf,-np.inf,-np.inf,0,0],[np.inf,np.inf,0,2,2]),maxfev = 100000000)[0]

x_fit = np.linspace(min(Per_x), max(Per_x), 100)
y_fit = dU(x_fit, A1,A2,A3,K1,K2)
y0_fit=dU(x_fit,539.25,-59.175,-1.46,0.0166,0.2)

fig=plt.figure(figsize=(8,6),dpi=1000)
# 绘制原始数据和拟合曲线
plt.plot(Per_x, Rg_y, 'o', linewidth=4.0, color='black', label='Data')  # 原始数据点
plt.plot(x_fit, y_fit, '-', linewidth=4.0, color='red', label='Fit')    # 拟合曲线

# plt.plot(x_fit,y0_fit,linewidth=4.0,color='blue')

plt.savefig('Rg_single_fitting.png',dpi=1000,bbox_inches='tight')

np.savetxt('Rg_single_fitting.txt', np.c_[[A1,A2,A3,K1,K2]],fmt='%f',delimiter='\t')

