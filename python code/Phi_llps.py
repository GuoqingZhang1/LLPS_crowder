import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
import math
N=8
T_0=120.27
fig=plt.figure(figsize=(8,6),dpi=1000)
cmap=plt.get_cmap('Blues',N)

for Per in ['0','5','10','15','20','25','30']:
    f_pro=open('../Crowd_'+Per+'/Phi_llps.txt','r')
    line_pro=f_pro.readlines()

    Phi=[]

    for i in range(len(line_pro)):
        Phi.append(np.arccos(float(line_pro[i].split()[1])))
        # Phi.append(np.arcsin(float(line_pro[i].split()[1])))



    Phi_min=np.min(Phi)
    Phi_max=np.max(Phi)
    delta=0.01
    N_bins=math.ceil((Phi_max-Phi_min)/delta)


    Phi_dis=np.zeros([N_bins])
    for i in range(len(Phi)):

        if Phi_min<=Phi[i]<Phi_max:
            nl=math.floor((Phi[i]-Phi_min)/delta)
            Phi_dis[nl]=Phi_dis[nl]+1/len(Phi)



    plt.plot(np.arange(Phi_min,Phi_max,delta),Phi_dis,linewidth=4.0,color=cmap((float(Per)+5)/40))

plt.xlabel(chr(966),labelpad=10,fontproperties='Arial',size=40)
# plt.xlabel('cos'+chr(966),labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
plt.xticks([0,math.pi*1/4,math.pi/2,math.pi*3/4,math.pi],['0',chr(960)+'/4',chr(960)+'/2','3'+chr(960)+'/4',chr(960)],fontproperties='Arial',fontsize=36)
# plt.xticks([-1.0,-0.5,0.0,0.5,1.0],fontproperties='Arial',fontsize=36)
plt.yticks(fontproperties='Arial',fontsize=36)
# plt.xlim(0,math.pi)
# plt.ylim(-0.0002,0.0082)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)
fig.set_size_inches(8,6)
plt.savefig('Phi_llps.png',dpi=1000,bbox_inches='tight')