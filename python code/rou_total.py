import numpy as np 
import matplotlib.pyplot as plt #绘图
import math 
import matplotlib as mpl
import matplotlib.ticker as ticker

f_pro=open('density_pro.txt','r')
line_pro=f_pro.readlines()

f_cro=open('density_cro.txt','r')
line_cro=f_cro.readlines()

totaltime=50001
totalline=500
rou_pro=[]
rou_cro=[]

mid_list=[]
z0_list=[]

for k in range(totaltime):
    t_pro=[]
    t_cro=[]


    for i in range(totalline):
        ss=line_pro[k*(totalline+1)+i+4].split()
        ss1=line_cro[k*(totalline+1)+i+4].split()
        t_pro.append(float(ss[3]))
        t_cro.append(float(ss1[3]))
        

    z0_index=t_pro.index(0)
    
    re_pro=[]
    re_cro=[]

    for i in range(z0_index,totalline):
        re_pro.append(t_pro[i])
        re_cro.append(t_cro[i])

    for i in range(0,z0_index):
        re_pro.append(t_pro[i])
        re_cro.append(t_cro[i])

    M_total=0

    for i in range(totalline):
        M_total=M_total+re_pro[i]*i/np.sum(re_pro)

    mid_pro=M_total-250

    if mid_pro<0:
        mid_pro=mid_pro+500
    elif mid_pro>500:
        mid_pro=mid_pro-500

    mid_list.append(mid_pro)
    z0_list.append(z0_index)

    l_pro=[]
    l_cro=[]

    for i in range(math.ceil(mid_pro),totalline):
        l_pro.append(re_pro[i])
        l_cro.append(re_cro[i])

    for i in range(0,math.ceil(mid_pro)):
        l_pro.append(re_pro[i])
        l_cro.append(re_cro[i])    

    # print(l_pro)
    # print(l_cro)
    rou_pro.append(l_pro)
    rou_cro.append(l_cro)

np.savetxt('z0_list.txt', np.c_[z0_list],fmt='%f',delimiter='\t')
np.savetxt('Middle_list.txt', np.c_[mid_list],fmt='%f',delimiter='\t')

fig=plt.figure(figsize=(3,10),dpi=1000)
ax1 = fig.gca()
im1 = ax1.imshow(rou_pro,cmap='Blues',origin='lower',aspect='auto')
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)

cb=plt.colorbar(im1,pad=0.05)
cb.ax.set_title(chr(961)+" (g/cm"+'$\mathregular{^3}$)',pad=20,fontdict={'size':15,'family':'Arial'})
    
im1.set_clim(0,1.0)
tick_locator = ticker.MaxNLocator(nbins=11)
plt.ylabel('t ('+chr(956)+'s)',size=32)
plt.xlabel('z'+' ('+u'$\mathregular{\AA}$)',fontsize=32)
plt.xticks([0,250,500],size=26)
plt.yticks([0,10000,20000,30000,40000,50000],['0','1','2','3','4','5'],size=26)
fig.set_size_inches(6,10)
plt.savefig('rou_pro.png',bbox_inches='tight',dpi=1000)
plt.close()

fig=plt.figure(figsize=(3,10),dpi=1000)
ax1 = fig.gca()
im1 = ax1.imshow(rou_cro,cmap='Greens',origin='lower',aspect='auto')
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)

cb=plt.colorbar(im1,pad=0.05)
cb.ax.set_title(chr(961)+" (g/cm"+'$\mathregular{^3}$)',pad=20,fontdict={'size':15,'family':'Arial'})
    
im1.set_clim(0,0.5)
tick_locator = ticker.MaxNLocator(nbins=11)
plt.ylabel('t ('+chr(956)+'s)',size=32)
plt.xlabel('z'+' ('+u'$\mathregular{\AA}$)',fontsize=32)
plt.xticks([0,250,500],size=26)
plt.yticks([0,10000,20000,30000,40000,50000],['0','1','2','3','4','5'],size=26)
fig.set_size_inches(6,10)
plt.savefig('rou_cro.png',bbox_inches='tight',dpi=1000)
plt.close()
