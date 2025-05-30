import numpy as np #矩阵
import math

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

ren=0
for i in range(1,Lmax):
    ss=line[i].split()
    if ss[2]=='CA':
        CG_AR[ren][0]=float(line[i][30:38])
        CG_AR[ren][1]=float(line[i][38:46])
        CG_AR[ren][2]=float(line[i][46:54])
        ren=ren+1

f_data=open('CTD_100.data','w')

f_data.write('#LAMMPS data file\n')
f_data.write('\n')
f_data.write('%d atoms\n' %(100*N_res))
f_data.write('%d bonds\n' %(100*(N_res-1)))
f_data.write('\n')
f_data.write('20 atom types\n')
f_data.write('1 bond types\n')
f_data.write('\n')
f_data.write('-500 500 xlo xhi\n')
f_data.write('-500 500 ylo yhi\n')
f_data.write('-500 500 zlo zhi\n')
f_data.write('\n')
f_data.write('Atoms\n')
f_data.write('\n')
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
        f_data.write('%3d %2d %2d %2.1f %f %f %f\n' %(k*N_res+i+1,k+1,ni+1,q_atom,CG_AR[i][0]-400+xa*200,CG_AR[i][1]-400+ya*200,CG_AR[i][2]-400+za*200))

f_data.write('\n')
f_data.write('Bonds\n')
f_data.write('\n')
for k in range(N_m):
    for i in range(N_res-1):
        f_data.write('%d %d %d %d\n' %(k*(N_res-1)+i+1,1,k*N_res+i+1,k*N_res+i+2))
f_data.close()
