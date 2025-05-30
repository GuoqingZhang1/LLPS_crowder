import numpy as np
import math
import matplotlib.pyplot as plt #绘图

# f=open('ul11stll.lammpstrj','r')
f=open('tdp43_300.000.trj','r')
line=f.readlines()
Lmax=len(line)


f_z0=open('Center.txt','r')
line_z0=f_z0.readlines()

Per=PERCENT
BOX=25*25*25

N_PEG=int(BOX*(Per)/(4*math.pi*0.8**3/3))

N_atoms=148+N_PEG
if Per==0.15:
    N_atoms=1237
N_one=N_atoms+9

Timeall=100001

f_w=open('Restru.lammpstrj','w')

for t in range(Timeall):
    for k in range(9):
        f_w.write(line[t*N_one+k])

    for i in range(N_atoms):
        ss=line[t*N_one+i+9].split()
        
        x_f=float(ss[2])-float(line_z0[t+2].split()[1])
        y_f=float(ss[3])-float(line_z0[t+2].split()[2])
        z_f=float(ss[4])-float(line_z0[t+2].split()[3])

        if x_f>125: 
            x_f=x_f-250
        elif x_f<-125:
            x_f=x_f+250

        if y_f>125:
            y_f=y_f-250
        elif y_f<-125:
            y_f=y_f+250

        if z_f>125:
            z_f=z_f-250
        elif z_f<-125:
            z_f=z_f+250
        
        f_w.write(ss[0]+' '+ss[1]+' %7f %7f %7f\n' %(x_f,y_f,z_f))


f.close()
f_w.close()
