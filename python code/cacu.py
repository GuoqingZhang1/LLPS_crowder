import numpy as np
import math
import matplotlib.pyplot as plt #绘图

a=np.array([[1,2,3],[2,5,3]])

print(np.mean(a))

print(np.mean([1,2,3,2,3,5]))

Per=0.1
BOX=15*15*50
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9

print(BOX*Per*0.01/(4*math.pi*0.8**3/3))

def fun1(x):
    return -0.5*3*3**2*np.log(1-(x/3)**2)

def fun2(x):
    return -5*(1+np.cos(math.pi*x/0.3))

xx=np.arange(0.1,5,0.1)
plt.plot(xx,fun1(xx),label='Bond')
plt.plot(xx,0.5*3*xx**2,label='Ham Bond')
plt.plot(np.arange(0.1,0.3,0.01),fun2(np.arange(0.1,0.3,0.01)),label='Arr')

plt.xlabel('r',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('E(r)',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)

plt.legend()
plt.show()