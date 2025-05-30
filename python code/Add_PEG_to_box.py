import numpy as np
import math
import random

Taa=['ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL']

f=open('LLPS_peg.lammpstrj','r')
line=f.readlines()
Lmax=len(line)

N_m=100
N_res=148
N_atoms=int(N_m*N_res)


ratom=np.full([N_atoms+1,4],np.nan)             #0为空，从1起
for i in range(N_m):
    
    for j in range(N_res):
        sx=line[i*N_res+9+j].split()
        ratom[int(sx[0])][0]=float(sx[1])
        ratom[int(sx[0])][1]=float(sx[2])
        ratom[int(sx[0])][2]=float(sx[3])
        ratom[int(sx[0])][3]=float(sx[4])

BOX=15*15*50

Per=40

N_PEG=round(BOX*Per*0.001/(4*math.pi*0.8**3/3))
print(N_PEG)

f_data=open('CTD_LLPS_PEG_m_%d.data' %(Per),'w')

f_data.write('#LAMMPS data file\n')  
f_data.write('\n')
f_data.write('%d atoms\n' %(100*N_res+N_PEG))
f_data.write('%d bonds\n' %(100*(N_res-1)))
f_data.write('\n')
f_data.write('21 atom types\n')
f_data.write('1 bond types\n')
f_data.write('\n')  
f_data.write('0 150 xlo xhi\n')
f_data.write('0 150 ylo yhi\n')
f_data.write('-250 250 zlo zhi\n')
f_data.write('\n')
f_data.write('Atoms\n')
f_data.write('\n')


for i in range(1,N_atoms+1):
    atom_type=Taa[int(ratom[i][0])-1]    
    if atom_type=='ARG' or atom_type=='LYS':
        q_atom=1
    elif atom_type=='ASP' or atom_type=='GLU':
        q_atom=-1
    else:
        q_atom=0
    f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(i,math.floor((i-1)/148)+1,ratom[i][0],q_atom,ratom[i][1],ratom[i][2],ratom[i][3]))


PEGx=[]
PEGy=[]
PEGz=[]

Dis_c=16
n_lat_x=math.floor(150/Dis_c)+2
n_lat_y=math.floor(150/Dis_c)+2
n_lat_z=math.floor(500/Dis_c)+2

Space=np.zeros([n_lat_x,n_lat_y,n_lat_z])

for nn in range(1,N_atoms+1):
    x_l=math.floor((ratom[nn][1])/Dis_c)
    x_h=math.ceil((ratom[nn][1])/Dis_c)
    y_l=math.floor((ratom[nn][2])/Dis_c)
    y_h=math.ceil((ratom[nn][2])/Dis_c)
    z_l=math.floor((ratom[nn][3]+250)/Dis_c)
    z_h=math.ceil((ratom[nn][3]+250)/Dis_c)

    Space[x_l][y_l][z_l]=1
    Space[x_l][y_l][z_h]=1
    Space[x_l][y_h][z_l]=1
    Space[x_h][y_l][z_l]=1
    Space[x_l][y_h][z_h]=1
    Space[x_h][y_h][z_l]=1
    Space[x_h][y_l][z_h]=1
    Space[x_h][y_h][z_h]=1


for i in range(n_lat_x-2):
    for j in range(n_lat_y-2):
        for k in range(n_lat_z-2):
            if Space[i][j][k]==0:
                PEGx.append(Dis_c*i)
                PEGy.append(Dis_c*j)
                PEGz.append(Dis_c*k-250)

print(len(PEGx))

# for i in range(-500,500,4):
#     for j in range(-500,500,4):
#         for k in range(-500,500,4):
#             Nlabel=0
#             for nn in range(len(Rx)):
#                 dd=(i-Rx[nn])**2+(j-Ry[nn])**2+(k-Rz[nn])**2
#                 if dd<16:
#                     Nlabel=1

#             if Nlabel==0:
#                 PEGx.append(i)
#                 PEGy.append(j)
#                 PEGz.append(k)


peg_list=random.sample(range(len(PEGx)),N_PEG)
for i in range(len(peg_list)):
    n_i=peg_list[i]
    f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(100*N_res+i+1,100+i+1,21,0,PEGx[n_i],PEGy[n_i],PEGz[n_i]))


f_data.write('\n')
f_data.write('Bonds\n')
f_data.write('\n')
for k in range(N_m):
    for i in range(N_res-1):
        f_data.write('%d %d %d %d\n' %(k*(N_res-1)+i+1,1,k*N_res+i+1,k*N_res+i+2))
f_data.close()