import numpy as np 
import matplotlib.pyplot as plt #绘图
import math 
import matplotlib as mpl
import matplotlib.ticker as ticker

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

    print(rou_z)
    
    plt.plot(np.arange(0,50,0.1),rou_z,linewidth=4.0,color=cmap((float(Per)+5)/40))

plt.xlabel("z (nm)",size=40,labelpad=10,fontproperties="Arial")
plt.ylabel(chr(961)+" (g/cm"+'$\mathregular{^3}$)',labelpad=10,size=40,fontproperties="Arial")
plt.xticks(fontproperties='Arial',fontsize=36)
plt.yticks([0.0,0.3,0.6,0.9,1.2],fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')  
plt.xlim(0,50)
plt.ylim(-0.02,1.22)
bwith = 3 #边框宽度设置为2
ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)
sm = plt.cm.ScalarMappable(cmap=cmap) 
cb=plt.colorbar(sm,format='%.2f')
cb.set_ticks([1.5/8,3.5/8,5.5/8,7.5/8])
cb.set_ticklabels(['0%','10%','20%','30%'])
cb.ax.set_ylim(1/8,1)
cb.ax.set_title('Crowders Percent',pad=20,fontdict={'size':30,'family':'Arial'})

# legend=plt.legend(prop = {'size':20,'family':'Times New Roman'},frameon=False,edgecolor='black')
fig.set_size_inches(10,6)
plt.savefig('rou_z_pro.png',bbox_inches='tight',dpi=1000)
