import numpy as np #矩阵
import math
import random

# AAsequence='MGLSFSGTRPCCCRNNVLITDDGEVVSLTAHDFDVVDIESEEEGNFYVPPDMRGVTRAPGRQRLRSSDPPSRHTHRRTPGGACPATQFPPPMSDSEWSHPQFEK'     #UL11stll

AAsequence='NRQLERSGRFGGNPGGFGNQGGFGNSRGGGAGLGNNQGSNMGGGMNFGAFSINPAMMAAAQAALQSSWGMMGMLASQQNQSGPSGNNQNQGNMQREPNQAFGSGNNSYSGSNSGAAIGWGSASNAGSGSGFNGGFGSSMDSKSSGWGM'       #CTD

Saa=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

Taa=['ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL']

Atomtype=['C','H','O','N','S']

Atommass=[12.010,1.007,15.999,14.006,32.065]

f=open('CTD_by_alphafold2.pdb' ,"r" )
line = f.readlines() # 以行的形式进行读取文件

Lmax = 1017

N_res=len(AAsequence)

CG_AR=np.zeros([N_res,3])

N_m=100

BOX=15*15*40

Per=30

N_PEG=round(BOX*Per*0.01/(4*math.pi*0.8**3/3))
print(N_PEG)

ren=0
for i in range(1,Lmax):
    ss=line[i].split()
    if ss[2]=='CA':
        CG_AR[ren][0]=float(line[i][30:38])
        CG_AR[ren][1]=float(line[i][38:46])
        CG_AR[ren][2]=float(line[i][46:54])
        ren=ren+1

f_data=open('CTD_100_PEG_%d.data' %(Per),'w')

f_data.write('#LAMMPS data file\n')
f_data.write('\n')
f_data.write('%d atoms\n' %(100*N_res+N_PEG))
f_data.write('%d bonds\n' %(100*(N_res-1)))
f_data.write('\n')
f_data.write('21 atom types\n')
f_data.write('1 bond types\n')
f_data.write('\n')
f_data.write('-500 500 xlo xhi\n')
f_data.write('-500 500 ylo yhi\n')
f_data.write('-500 500 zlo zhi\n')
f_data.write('\n')
f_data.write('Atoms\n')
f_data.write('\n')
Rx=[]
Ry=[]
Rz=[]

for k in range(N_m):
    for i in range(N_res):
        for j in range(20):
            if Saa[j]==AAsequence[i]:
                atom_type=Taa[j]
                ni=j
                break
        if atom_type=='ARG' or atom_type=='LYS':
            q_atom=1
        elif atom_type=='ASP' or atom_type=='GLU':
            q_atom=-1

        else:
            q_atom=0

        za=math.floor(k/25)
        ya=math.floor((k-za*25)/5)
        xa=k-za*25-ya*5
        xx=CG_AR[i][0]+100+xa*200
        yy=CG_AR[i][1]+100+ya*200
        zz=CG_AR[i][2]+100+za*200
        Rx.append(xx)
        Ry.append(yy)
        Rz.append(zz)
        f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(k*N_res+i+1,k+1,ni+1,q_atom,xx,yy,zz))

PEGx=[]
PEGy=[]
PEGz=[]

Dis_c=16
n_lat=round(1000/Dis_c)

Space=np.zeros([n_lat,n_lat,n_lat])

for nn in range(len(Rx)):
    x_l=math.floor((Rx[nn])/Dis_c)
    x_h=math.ceil((Rx[nn])/Dis_c)
    y_l=math.floor((Ry[nn])/Dis_c)
    y_h=math.ceil((Ry[nn])/Dis_c)
    z_l=math.floor((Rz[nn])/Dis_c)
    z_h=math.ceil((Rz[nn])/Dis_c)

    Space[x_l][y_l][z_l]=1
    Space[x_l][y_l][z_h]=1
    Space[x_l][y_h][z_l]=1
    Space[x_h][y_l][z_l]=1
    Space[x_l][y_h][z_h]=1
    Space[x_h][y_h][z_l]=1
    Space[x_h][y_l][z_h]=1
    Space[x_h][y_h][z_h]=1


for i in range(n_lat):
    for j in range(n_lat):
        for k in range(n_lat):
            if Space[i][j][k]==0:
                PEGx.append(Dis_c*i)
                PEGy.append(Dis_c*j)
                PEGz.append(Dis_c*k)

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