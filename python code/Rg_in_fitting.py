import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
import scipy.optimize as op
from scipy.special import airy, pbdv

dxx=0.00001
# def dU (x,a1,k1):
#     y_out=[]
#     for x_one in x:
#         N=math.ceil(x_one/dxx)
#         y1=0
#         for i in range(N):
#             xi=i*dxx
#             y1+=dxx*np.exp(k1*xi**2/2)
#         y_out.append(a1*y1*np.exp(-k1*x_one**2/2))
#     return y_out

# def y(x,a,b):
#     z = (a * b)**(1/3) * x
#     Ai, Aip, Bi, Bip = airy(z)
#     y1 = (a / (a*b)**(1/3)) * Ai / Aip
#     return y1

# def dU (x,a,b):
#     z = (b) * x
#     Ai, Aip, Bi, Bip = airy(z)
#     y1 = a * Ai / Aip
#     return y1

def dU (x,a,c):

    return (np.sqrt(c**2*x**2+4*(a+c)*x+1)-(c*x+1))/(2*x)

Rg_y=[]
Per_x=[]

Rg_0=0
# for Per in ['0','1','5','10','15','20','30','40','50','100','150','200','250','300']:
for Per in ['50','100','150','200','250','300']:
    f_pro=open('Rg_per_in_'+Per+'.txt','r')
    line_pro=f_pro.readlines()

    Rg=[]

    for i in range(len(line_pro)):
        Rg.append(float(line_pro[i]))

    if Per=='0':
        Rg_0=np.mean(Rg)
    
    Rg_y.append(np.mean(Rg))
    Per_x.append(float(Per)*0.001)

A1,K1=op.curve_fit(dU,Per_x,Rg_y,p0=[0,1],bounds=([0,-1],[1,np.inf]),maxfev = 100000000)[0]

x_fit = np.linspace(min(Per_x), max(Per_x), 100)
y_fit = dU(x_fit, A1,K1)
# y0_fit=dU(x_fit)

fig=plt.figure(figsize=(8,6),dpi=1000)
# 绘制原始数据和拟合曲线
plt.plot(Per_x, Rg_y, 'o', linewidth=4.0, color='black', label='Data')  # 原始数据点
plt.plot(x_fit, y_fit, '-', linewidth=4.0, color='red', label='Fit')    # 拟合曲线

# plt.plot(x_fit,y0_fit,linewidth=4.0,color='blue')

plt.savefig('Rg_in_fitting.png',dpi=1000,bbox_inches='tight')

np.savetxt('Rg_in_fitting.txt', np.c_[[A1,K1]],fmt='%f',delimiter='\t')

