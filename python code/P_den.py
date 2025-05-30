import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵 
import math
import matplotlib.ticker as ticker

begintime=10000
totaltime=50001
totalline=500

P_den=[]
Per_x=[]

N_in_per=[]
N_out_per=[]

for Per in ['5','10','15','20','25','30']:


    f_pro=open('../Crowd_'+Per+'/density_re_pro.txt','r')
    line_pro=f_pro.readlines()

    f_cro=open('../Crowd_'+Per+'/density_re_cro.txt','r')
    line_cro=f_cro.readlines()

    den_pro=np.zeros([500])
    den_cro=np.zeros([500])


    for k in range(begintime,totaltime):

        for i in range(totalline):
            ss=line_pro[k*(totalline+1)+i+4].split()
            ss1=line_cro[k*(totalline+1)+i+4].split()
            den_pro[i]+=float(ss[2])/(totaltime-begintime)
            den_cro[i]+=float(ss1[2])/(totaltime-begintime)

    z_cut=0
    for i in range(250,499):
        if den_pro[i]<0.5*(den_pro[249]-den_pro[499]):
            z_cut=i
            break
    
    N_in=0
    N_out=0
    for i in range(250,499):
        if i<z_cut:
            N_in+=den_cro[i]
        else:
            N_out+=den_cro[i]

    P_den.append(N_in/N_out)
    N_in_per.append(N_in)
    N_out_per.append(N_out)
    Per_x.append(float(Per))


fig = plt.figure(dpi=1000,figsize=(8,6))
plt.scatter(Per_x,P_den,s=150)
plt.plot(Per_x,P_den,linewidth=4.0)
plt.xlabel('Percent',labelpad=10,fontproperties='Arial',size=40)
# plt.xlabel('cos'+chr(966),labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('P',labelpad=10,fontproperties='Arial',size=40)
plt.xticks(fontproperties='Arial',fontsize=36)
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
plt.savefig('P_den.png',dpi=1000,bbox_inches='tight')


fig,axx1=plt.subplots(figsize=(10,6),dpi=1000)

# plt.plot(0.05+np.arange(0,12.5,0.1),rou_pro[0:125],linewidth=4.0)
axx1.scatter(np.arange(0.5,3.5,0.5),N_in_per,color='blue',s=150,label='N_in')
axx1.plot(np.arange(0.5,3.5,0.5),N_in_per,color='blue',linewidth=4.0)

axx1.set_xlabel("z (nm)",size=40,labelpad=10,fontproperties="Arial")
axx1.set_ylabel(u'$\mathregular{P^{N}_{in}}$',labelpad=10,size=40,fontproperties="Arial")
# axx1.set_xticks(fontproperties='Arial',fontsize=36)
# axx1.set_yticks(fontproperties='Arial',fontsize=36)
axx1.tick_params(length=7,pad=10,width = 3,direction='in') 

axx2=axx1.twinx()
axx2.scatter(np.arange(0.5,3.5,0.5),N_out_per,color='red',s=150,label='N_out')
axx2.plot(np.arange(0.5,3.5,0.5),N_out_per,color='red',linewidth=4.0)

axx2.set_xlabel("z (nm)",size=40,labelpad=10,fontproperties="Arial")
axx2.set_ylabel(u'$\mathregular{P^{N}_{out}}$',labelpad=10,size=40,fontproperties="Arial")
# axx2.set_xticks(fontproperties='Arial',fontsize=36)
# axx2.set_yticks(fontproperties='Arial',fontsize=36)
axx2.tick_params(length=7,pad=10,width = 3,direction='in') 

plt.legend(prop = {'size':14},frameon=True,edgecolor ='black',shadow=True)

# plt.ylim(-0.05,1.8)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24

fig.set_size_inches(10,6)
plt.savefig('N_per_in_out.png',bbox_inches='tight',dpi=1000)