import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵 
import math
import matplotlib.ticker as ticker

n_file='1'
f=open('Phi_'+n_file+'_z_llps.txt','r')
line=f.readlines()

f_n=open('3R_z_llps.txt','r')
line_n=f_n.readlines()


Per=PERCENT

Phi_min=0
Phi_max=math.pi
delta=0.01
N_bins=math.ceil((Phi_max-Phi_min)/delta)

N_i=np.zeros([3,len(line_n)])
for i in range(len(line_n)):
    str_n=line_n[i].split()
    for j in range(3):
        N_i[j][i]=float(str_n[j])


Phi_z=np.zeros([3,N_bins,500])

for n in range(3):
    f=open('Phi_%d_z_llps.txt' %(n),'r')
    line=f.readlines()
    for i in range(len(line)):
        ss=line[i].split()
        # if N_i[int(n_file)][i]>0.2*np.max(N_i[int(n_file),:]):
        for j in range(N_bins):    
            Phi_z[n][j][i]=float(ss[j])

# yPhi=[]
# xz=[]


# for i in range(len(line)):
  
#     if N_i[int(n_file)][i]>0.2*np.max(N_i[int(n_file),:]):
#         xz.append(i)
#         cutu=0
#         for j in range(N_bins):
#             if Phi_z[j][i]==np.max(Phi_z[:,i]):
#                 cutu=j
#         yPhi.append(cutu)
# f_2=open('Phi_llps.txt','r')
# line_2=f_2.readlines()


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

fig=plt.figure(figsize=(10,6),dpi=1000)
ax1 = fig.gca()
if n_file=='0':
    im1 = ax1.imshow(0.5*Phi_z[0]+0.5*Phi_z[2,::-1],cmap='CMRmap_r',origin='lower',aspect='auto')
if n_file=='1':
    im1 = ax1.imshow(Phi_z[1],cmap='CMRmap_r',origin='lower',aspect='auto')
# ax1.plot([25,25],[Phi_min,Phi_max],linestyle='--')

if n_file=='0':
    lcolor=rgb_to_hex((0,113,188))
if n_file=='1':
    lcolor=rgb_to_hex((255,78,42))
if n_file=='2':
    lcolor=rgb_to_hex((0,146,69))

# ax1.plot(xz,yPhi,color='white',linewidth=5,linestyle='-')
# ax1.plot(xz,yPhi,color=lcolor,linewidth=4,linestyle='-')

plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24
norm = mpl.colors.Normalize(vmin=0, vmax=1.00)

cb=plt.colorbar(im1,pad=0.05)
# cb.ax.set_title('Probability',pad=20,fontdict={'size':20,'family':'Arial'})

# im1.set_clim(0,400)
# cb.set_ticks([0,100,200,300,400])
im1.set_clim(0,100)
cb.set_ticks([0,20,40,60,80,100])

# cb.set_ticklabels(['0.0%','0.2%','0.4%','0.6%','0.8%','1.0%'])
# cb.formatter = ticker.ScalarFormatter(useMathText=True)
# cb.formatter.set_powerlimits((0,10))  # 设置科学计数法的范围

plt.tick_params(length=7,pad=10,width = 3,direction='in') 

bwith = 3 #边框宽度设置为2

ecolor='black'

ax1 = plt.gca()#获取边框
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
ax1.spines['bottom'].set_color(ecolor)
ax1.spines['left'].set_color(ecolor)
ax1.spines['top'].set_color(ecolor)
ax1.spines['right'].set_color(ecolor)
plt.rcParams['font.family']='Arial'
plt.rcParams['font.size']=24


# im1.set_clim(0,300)
tick_locator = ticker.MaxNLocator(nbins=11)

if n_file=='0':
    plt.ylabel(chr(966)+'$\mathregular{_{IDR}}$',fontsize=40)
if n_file=='1':
    plt.ylabel(chr(966)+'$\mathregular{_{Helix}}$',fontsize=40)
if n_file=='2':
    plt.ylabel(chr(966)+'$\mathregular{_{IDR 2}}$',fontsize=40)

plt.xlabel('z'+' (nm)',fontsize=40)
plt.xticks([0,100,200,300,400,500],['0','10','20','30','40','50'],size=36)
plt.yticks([0,100*math.pi*1/4,100*math.pi/2,100*math.pi*3/4,100*math.pi],['0°','45°','90°','135°','180°'],size=36)
fig.set_size_inches(10,6)
plt.savefig('Phi_'+n_file+'_z_%d.png' %(Per),bbox_inches='tight',dpi=1000)