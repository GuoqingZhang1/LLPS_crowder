import numpy as np 
import matplotlib.pyplot as plt #绘图
import math 
import matplotlib as mpl
import matplotlib.ticker as ticker

begintime=10000
totaltime=50001
totalline=500

fig=plt.figure(figsize=(10,6),dpi=1000)
cmap=plt.get_cmap('Blues',8)

Per=PERCENT

f_pro=open('density_pro.txt','r')
line_pro=f_pro.readlines()

rou_pro=[]

f_index=open('Middle_list.txt','r')
line_index=f_index.readlines()

M_index=[]

for i in range(len(line_index)):
    M_index.append(float(line_index[i]))

rou_z=np.zeros([500])

for k in range(begintime,totaltime):
    t_pro=[]

    for i in range(totalline):
        ss=line_pro[k*(totalline+1)+i+4].split()
        t_pro.append(float(ss[3]))
        

    z0_index=t_pro.index(0)
    
    re_pro=[]

    for i in range(z0_index,totalline):
        re_pro.append(t_pro[i])

    for i in range(0,z0_index):
        re_pro.append(t_pro[i])

    l_pro=[]
  

    for i in range(math.ceil(M_index[k]),totalline):
        l_pro.append(re_pro[i])

    for i in range(0,math.ceil(M_index[k])):
        l_pro.append(re_pro[i])

    for i in range(totalline):
        rou_z[i]=rou_z[i]+l_pro[i]/(totaltime-begintime)

lattice_delta=1
N_lattice=321

Phi=np.ones([N_lattice])
for k in range(N_lattice):
    if k<285:
        Phi[k]=rou_z[250-35+k]/98.3*1500
    else:
        Phi[k]=0


A=-12*0.8*6**13

rou_c=np.ones([N_lattice])

for k in range(N_lattice):
    if k < 35:    
        rou_c[k]=0 
    elif k >= 285:
        rou_c[k]=1


rou_c_2=np.ones([N_lattice])

io=0
while io !=1:
    io=1
    for k in range(N_lattice):
        if k <35 :
            # rou_c_2[k]=(-rou_c[k+69]*A/26**13+rou_c[k+34]*A/(-9)**13+rou_c[k+33]*A/(-10)**13-Phi[k+69]*A/(36-3.91**13)+Phi[k+33]*A/(-3.91)**13+Phi[k+34]*A/(-2.91)**13-Phi[k]*A/(35-3.91)**13)*25**13/A
            rou_c_2[k]=0
        elif k >= 285:
            # rou_c_2[k]=(-rou_c[k-69]*A/25**13+rou_c[k-35]*A/(-9)**13+rou_c[k-36]*A/(-10)**13-Phi[k]*A/(36-3.91)**13+Phi[k-36]*A/(-3.91)**13+Phi[k-35]*A/(-2.91)**13-Phi[k-69]*A/(35-3.91)**13)*26**13/A
            rou_c_2[k]=1
        else:
            rou_c_2[k]=(rou_c[k-24]*A/25**13+rou_c[k+36]*A/25**13-rou_c[k+22]*A/(1)**13+Phi[k+36]*A/(35-4)**13-Phi[k+6]*A/(1)**13-Phi[k+16]*A/(1)**13+Phi[k-24]*A/(35-4)**13)*(1)**13/(A)

    for k in range(N_lattice):
        if rou_c[k]-rou_c_2[k]>0.0001:
            io=0
            break
    
    if io==0:
        for k in range(N_lattice):
            rou_c[k]=rou_c_2[k]
    
    print(rou_c)

np.savetxt('rou_cro_analysis_llps.txt', np.c_[rou_c],fmt='%f',delimiter='\t')

    