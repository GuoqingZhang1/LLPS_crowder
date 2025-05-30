import numpy as np
import math
import matplotlib.pyplot as plt #绘图

# f=open('ul11stll.lammpstrj','r')
f=open('HPS.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

f_in=open('input_crowd.lammps','r')
line_in=f_in.readlines()

Label_time=line_in[14].split('.')[2]

print(Label_time)

# Per=PERCENT
# BOX=15*15*50

# N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))

# N_atoms=14800+N_PEG

# N_one=N_atoms+9

f_w=open('Final.lammpstrj','w')

i_stop=0
for i in range(Lmax):
    
    if line[i]==Label_time:
        i_stop=1
    
    if line[i]=='0\n' and i>1000000:
        i_stop=2

    if i_stop==0:
        f_w.write(line[i])

    if i_stop==2:
        if line[i-1]=='ITEM: TIMESTEP\n':
            line[i]=('%d\n' %(float(Label_time)+float(line[i])))
        
        f_w.write(line[i])
    


f.close()
f_w.close()
