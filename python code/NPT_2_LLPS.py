import numpy as np
import math
import matplotlib.pyplot as plt #绘图

Per=30
BOX=15*15*40
N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
N_atoms=14800+N_PEG
N_one=N_atoms+9
N_res=148

begintime=0
Timeall=1

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]

Taa=['ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL']

# f=open('ul11stll.lammpstrj','r')
f=open('../NPT/One_llps_%d.lammpstrj' %(Per),'r')
line=f.readlines()
Lmax=len(line)
f.close()
R_pro=np.zeros([Timeall-begintime,100,148,4])     #0: type 1: x 2: y 3: z
R_cro=np.zeros([Timeall-begintime,N_PEG,4])

for i in range(Timeall-begintime):
    for j in range(N_atoms):
        sss=line[(begintime+i)*N_one+9+j].split()
        type=float(sss[1])
        index=float(sss[0])
        if type==21:
            R_cro[i][round(index-14800-1)][0]=round(type)
            R_cro[i][round(index-14800-1)][1]=float(sss[2])
            R_cro[i][round(index-14800-1)][2]=float(sss[3])
            R_cro[i][round(index-14800-1)][3]=float(sss[4])

        else:
            n_l=math.floor((index-1)/148)
            n_b=round(index-1-148*n_l)
            R_pro[i][n_l][n_b][0]=round(type)
            R_pro[i][n_l][n_b][1]=float(sss[2])
            R_pro[i][n_l][n_b][2]=float(sss[3])
            R_pro[i][n_l][n_b][3]=float(sss[4])

for i in range(Timeall-begintime):
    for j in range(100):
        for k in range(1,148):
        
            if R_pro[i][j][k][1]-R_pro[i][j][k-1][1]>140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]-150
            elif R_pro[i][j][k][1]-R_pro[i][j][k-1][1]<-140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]+150

            if R_pro[i][j][k][2]-R_pro[i][j][k-1][2]>140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]-150
            elif R_pro[i][j][k][2]-R_pro[i][j][k-1][2]<-140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]+150

            if R_pro[i][j][k][3]-R_pro[i][j][k-1][3]>140:
                R_pro[i][j][k][3]=R_pro[i][j][k][3]-150
            elif R_pro[i][j][k][3]-R_pro[i][j][k-1][3]<-140:
                R_pro[i][j][k][3]=R_pro[i][j][k][3]+150


for i in range(Timeall-begintime):
    for j in range(100):
        for k in range(148):
            if R_pro[i][j][k][1]>140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]-150
            elif R_pro[i][j][k][1]<-140:
                R_pro[i][j][k][1]=R_pro[i][j][k][1]+150

            if R_pro[i][j][k][2]>140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]-150
            elif R_pro[i][j][k][2]<-140:
                R_pro[i][j][k][2]=R_pro[i][j][k][2]+150

f_data=open('../NPT/CTD_LLPS_PEG_%d.data' %(Per),'w')

f_data.write('#LAMMPS data file\n')
f_data.write('\n')
f_data.write('%d atoms\n' %(100*N_res+N_PEG))
f_data.write('%d bonds\n' %(100*(N_res-1)))
f_data.write('\n')
f_data.write('21 atom types\n')
f_data.write('1 bond types\n')
f_data.write('\n')
f_data.write('-75 75 xlo xhi\n')
f_data.write('-75 75 ylo yhi\n')
f_data.write('-200 200 zlo zhi\n')
f_data.write('\n')
f_data.write('Atoms\n')
f_data.write('\n')


for j in range(100):
    for k in range(148):
        atom_type=Taa[int(R_pro[0][j][k][0])-1]    
        if atom_type=='ARG' or atom_type=='LYS':
            q_atom=1
        elif atom_type=='ASP' or atom_type=='GLU':
            q_atom=-1
        else:
            q_atom=0

        f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(j*148+k+1,j+1,R_pro[0][j][k][0],q_atom,R_pro[0][j][k][1],R_pro[0][j][k][2],R_pro[0][j][k][3]))

for n in range(N_PEG):
    f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(14800+n+1,100+n+1,21,0,R_cro[0][n][1],R_cro[0][n][2],R_cro[0][n][3]))

f_data.write('\n')
f_data.write('Bonds\n')
f_data.write('\n')
for k in range(100):
    for i in range(N_res-1):
        f_data.write('%d %d %d %d\n' %(k*(N_res-1)+i+1,1,k*N_res+i+1,k*N_res+i+2))
f_data.close()