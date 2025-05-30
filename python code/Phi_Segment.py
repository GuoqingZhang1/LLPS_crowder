import matplotlib.pyplot as plt #绘图
import matplotlib as mpl 
import numpy as np #矩阵 
import math
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd



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


IDR_left=[]
IDR_right=[]
Helix_left=[]
Helix_right=[]


j=0
for i in range(len(line_n)):
    if 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i<250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                IDR_left.append(k)
    elif 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i>=250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                IDR_right.append(k)

j=1
for i in range(len(line_n)):
    if 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i<250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                Helix_left.append(k)
    elif 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i>=250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                Helix_right.append(k)
j=2
for i in range(len(line_n)):
    if 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i<250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                IDR_left.append(N_bins-1-k)
    elif 0.2*max(N_i[j])<N_i[j][i]<0.8*np.max(N_i[j]) and i>=250:
        for k in range(N_bins):
            for l in range(round(Phi_z[j][k][i])):
                IDR_right.append(N_bins-1-k)


IDR_left_np=np.array(IDR_left)
IDR_right_np=np.array(IDR_right)
Helix_left_np=np.array(Helix_left)
Helix_right_np=np.array(Helix_right)


df = pd.DataFrame({
    "Group": ["IDR"] * (len(IDR_left_np)+len(IDR_right_np)) + ["Helix"] * (len(Helix_left_np)+len(Helix_right_np)),  # 主分组（两对）
    "Subgroup": ["Left"] * len(IDR_left_np) + ["Right"] * len(IDR_right_np) + ["Left"] * len(Helix_left_np)+ ["Right"] * len(Helix_right_np),  # 子分组（左右）
    "Value": np.concatenate([IDR_left_np, IDR_right_np, Helix_left_np, Helix_right_np])
})


df["Group_Sub"] = df["Group"].astype(str) + "_" + df["Subgroup"].astype(str)

# 定义调色盘：同一 Group 的左右颜色相同
palette = {
    "IDR_Left": "skyblue",
    "IDR_Right": "skyblue",  # Group1 统一颜色
    "Helix_Left": "orange",
    "Helix_Right": "orange"    # Group2 统一颜色
}

fig=plt.figure(figsize=(8, 6),dpi=1000)
ax=sns.violinplot(
    x="Group",          # 主分组（两对）
    y="Value",          # 数值列
    hue="Group_Sub",     # 子分组（左右）
    data=df,
    split=True,         # 开启对称分割
    palette=palette,  # 自定义颜色
    inner="quartile",    # 显示四分位线
    scale="count",     # 根据数据量调整宽度
    dodge=True,  # 关键：关闭自动横向偏移
    legend=False,
    linewidth=4,
    linecolor='black',
)

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

plt.ylabel(chr(966),fontsize=40)

plt.xlabel("Segments",fontsize=40)
plt.xticks(size=36)
plt.yticks([0,100*math.pi*1/4,100*math.pi/2,100*math.pi*3/4,100*math.pi],['0°','45°','90°','135°','180°'],size=36)

plt.ylabel(chr(966))
fig.set_size_inches(8,6)
plt.savefig('Phi_segments_%d.pdf' %(Per),bbox_inches='tight',dpi=1000)