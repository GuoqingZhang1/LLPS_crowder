import numpy as np
import math
import matplotlib.pyplot as plt #绘图

# f=open('ul11stll.lammpstrj','r')
f=open('HPS.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

f_in=open('Middle_list.txt','r')
line_in=f_in.readlines()

f_z0=open('z0_list.txt','r')
line_z0=f_z0.readlines()

Per=PERCENT
BOX=15*15*50

N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))

N_atoms=14800+N_PEG

N_one=N_atoms+9

Timeall=50001

f_w=open('Restru.lammpstrj','w')

for t in range(Timeall):
    for k in range(9):
        f_w.write(line[t*N_one+k])

    for i in range(N_atoms):
        ss=line[t*N_one+i+9].split()
        
        z_f=float(ss[4])-float(line_in[t])-float(line_z0[t])

        if z_f>250:
            z_f=z_f-500
        elif z_f<-250:
            z_f=z_f+500
        
        f_w.write(ss[0]+' '+ss[1]+' '+ss[2]+' '+ss[3]+' %7f\n' %(z_f))


f.close()
f_w.close()
