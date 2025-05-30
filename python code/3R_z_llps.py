import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵
from matplotlib.ticker import ScalarFormatter
import math

f=open('3R_z_llps.txt','r')
line=f.readlines()

Per=PERCENT

x_z=[]
R1_z=[]
R2_z=[]
R3_z=[]

for i in range(len(line)):
    ss=line[i].split()
    R1_z.append(float(ss[0])/4000100)
    R2_z.append(float(ss[1])/4000100)
    R3_z.append(float(ss[2])/4000100)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


fig=plt.figure(figsize=(8,6),dpi=1000)
plt.plot(np.arange(500),R1_z,linewidth=4.0,label='IDR1',color=rgb_to_hex((0,113,188)))
plt.plot(np.arange(500),R2_z,linewidth=4.0,label='Helix',color=rgb_to_hex((255,78,42)))
plt.plot(np.arange(500),R3_z,linewidth=4.0,label='IDR2',color=rgb_to_hex((0,146,69)))

plt.ylim([0,0.015])
plt.xlim([0,500])
plt.xticks([0,100,200,300,400,500],['0','10','20','30','40','50'],fontproperties='Arial',fontsize=36)
plt.yticks([0,0.005,0.01,0.015],['0.0%','0.5%','1.0%','1.5%'],fontproperties='Arial',fontsize=36)
plt.tick_params(length=7,pad=10,width = 3,direction='in')

plt.xlabel('z (nm)',labelpad=10,fontproperties='Arial',size=40)
plt.ylabel('Probability',labelpad=10,fontproperties='Arial',size=40)
# plt.legend(prop = {'size':26,'family':'Arial'},frameon=False,edgecolor ='black')

bwith = 3 #边框宽度设置为2
ax = plt.gca()#获取边框
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0,1))

# formatter = ScalarFormatter(useMathText=True)
# formatter.set_powerlimits((0, 1))
# ax.yaxis.set_major_formatter(formatter)

# # 获取并修改偏移文本
# offset_text = ax.yaxis.get_offset_text()
# offset_text.set_fontsize(20)

# # 修改偏移文本为 10^-2 的形式
# def update_offset_text(event):
#     if ax.yaxis.get_offset_text().get_text():
#         exponent_str = ax.yaxis.get_offset_text().get_text().replace('e', '10^{') + '}'
#         ax.yaxis.offsetText.set_text(r'$\times$' + exponent_str)
#     fig.canvas.draw_idle()

# fig.canvas.mpl_connect('draw_event', update_offset_text)


fig.set_size_inches(8,6)
plt.savefig('3R_z_%d.png' %(Per),dpi=1000,bbox_inches='tight')