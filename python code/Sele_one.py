import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

# f=open('ul11stll.lammpstrj','r')
f=open('NPT_out.lammpstrj','r')
line=f.readlines()
begintime=551
finaltime=552

Per=0

BOX=15*15*40

cut_l=75
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))

N_atoms=14800+N_PEG

labeltime=0
for i in range(finaltime-begintime+1):
    sss=line[(N_atoms+9)*(i+begintime)+5].split()
    if float(sss[1])<cut_l:
        labeltime=i
        break

www=[]
for i in range(labeltime,labeltime+1):
    for j in range(N_atoms+9):
        www.append(line[(N_atoms+9)*(i+begintime)+j])



f.close()

f_w=open('One_llps_%d.lammpstrj' %(Per),'w')
for j in range(len(www)):
    f_w.write(www[j])

f_w.close()

