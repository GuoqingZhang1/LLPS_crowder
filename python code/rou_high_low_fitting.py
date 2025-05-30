import numpy as np 
import matplotlib.pyplot as plt #绘图
import math 
import matplotlib as mpl
from scipy import optimize as op
import matplotlib.ticker as ticker


def f_rou(z,rou_low,rou_high,z_0,d):
    return 0.5*(rou_high+rou_low)-0.5*(rou_high-rou_low)*np.tanh((z-z_0)/d)

begintime=10000
totaltime=50001
totalline=500

fig=plt.figure(figsize=(10,6),dpi=1000)
cmap=plt.get_cmap('Blues',8)

for Per in ['0','5','10','15','20','25','30']:
    f_pro=open('../Crowd_'+Per+'/density_pro.txt','r')
    line_pro=f_pro.readlines()

    rou_pro=[]

    f_index=open('../Crowd_'+Per+'/Middle_list.txt','r')
    line_index=f_index.readlines()

    M_index=[]

    for i in range(len(line_index)):
        M_index.append(float(line_index[i]))

    rou_z=np.zeros([500])

    for k in range(begintime,totaltime):
        t_pro=[]

        for i in range(totalline):
            ss=line_pro[k*(totalline+1)+i+4].split()
            t_pro.append(float(ss[3]))
        

        z0_index=t_pro.index(0)
    
        re_pro=[]

        for i in range(z0_index,totalline):
            re_pro.append(t_pro[i])

        for i in range(0,z0_index):
            re_pro.append(t_pro[i])

        l_pro=[]
  

        for i in range(math.ceil(M_index[k]),totalline):
            l_pro.append(re_pro[i])

        for i in range(0,math.ceil(M_index[k])):
            l_pro.append(re_pro[i])

        for i in range(totalline):
            rou_z[i]=rou_z[i]+l_pro[i]/(totaltime-begintime)

    z = np.arange(0,25,0.1)

    rou_low,rou_high,z_0,d=op.curve_fit(f_rou,z,rou_z[250:500],bounds=([0,0,0,0],[np.inf,np.inf,np.inf,np.inf]))[0]

    y = 0.5*(rou_high+rou_low)-0.5*(rou_high-rou_low)*np.tanh((z-z_0)/d)

    rou_fitting=[]
    rou_fitting.append(rou_low)
    rou_fitting.append(rou_high)



    np.savetxt('../Crowd_'+Per+'/rou_fitting.txt', np.c_[rou_fitting],fmt='%f',delimiter='\t')

    plt.scatter(z,rou_z[250:500],marker="o",color='black',s=100)

    plt.plot(z,y,color='red',label='Fitting curve',linewidth=4.0)
    plt.xlabel('z-'+'$\mathregular{z_{H}}$'+' (nm)',size=40,labelpad=10,fontproperties="Arial")
    plt.ylabel(chr(961)+' (mol/L)',size=40,labelpad=10,fontproperties="Arial")  
    plt.xticks(fontproperties="Arial",size=26)
    plt.yticks(fontproperties="Arial",size=26)
    plt.tick_params(length=7,pad=10,which='major',width = 3,direction='in')
    plt.xlim(0,25)
    bwith = 3 #边框宽度设置为2
    ax = plt.gca()#获取边框
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
    # plt.legend(prop = {'size':26,'family':'Times New Roman'},frameon=False,edgecolor ='black',shadow=True)
    fig.set_size_inches(8,6)
    plt.savefig('../Crowd_'+Per+'/fitting_%s.png' %(Per),dpi=1000,bbox_inches='tight')
    plt.close()