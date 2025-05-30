import numpy as np
import math
import matplotlib.pyplot as plt #绘图
from scipy import optimize as op
from matplotlib.colors import LogNorm

Per=PERCENT

begintime=40000
Timeall=50001

def f(t,tau):
    return np.exp(-t/tau)

Corr_3R=np.load(file='Corr_3R_Nc.npy')

Q_mean=np.load(file='Qij_Nc.npy')

Qt=np.load(file='Qt_Nc.npy')

Inter=np.zeros([3,3])

Intra=np.zeros([3,3])

Tau=np.zeros([300,300])

t_x=np.arange(Timeall-begintime-1)

for i in range(300):
    for j in range(300):
        
        tau=0
        # if np.max(Qt[:,i,j])>0 and np.min(Qt[:,i,j])==0:
        tau=op.curve_fit(f,t_x,Corr_3R[:,i,j],maxfev = 100000000,xtol=0.0001,ftol=0.0001,gtol=0.0001)[0]

        Tau[i][j]=tau

Intra_Qij=np.zeros([3,3])
Inter_Qij=np.zeros([3,3])

intra_n=np.zeros([3,3])
inter_n=np.zeros([3,3])


for j in range(300-1):
    for k in range(j,300):

        j_l=math.floor(j/3)
        j_n=round(j-3*j_l)
        k_l=math.floor(k/3)
        k_n=round(k-3*k_l)

        if Tau[j][k]>0 :
            if j_l==k_l:
                
                if j_n!=k_n:
                    intra_n[j_n][k_n]+=1
                    Intra_Qij[j_n][k_n]+=Q_mean[j][k]
                    Intra[j_n][k_n]+=Tau[j][k]
        
                    intra_n[k_n][j_n]+=1
                    Intra_Qij[k_n][j_n]+=Q_mean[j][k]
                    Intra[k_n][j_n]+=Tau[j][k]

            else:

                inter_n[j_n][k_n]+=1
                Inter[j_n][k_n]+=Tau[j][k]
                # Inter[k_n][j_n]+=Tau[j][k]/(99*50)
                Inter_Qij[j_n][k_n]+=Q_mean[j][k]

Inter_Qij=Inter_Qij/inter_n
Inter=Inter/inter_n

intra_n = np.where(intra_n == 0, 1, intra_n)

Intra_Qij=Intra_Qij/intra_n
Intra=Intra/intra_n


np.savetxt('Intra_Qij.txt', np.c_[Intra_Qij],fmt='%f',delimiter='\t')
np.savetxt('Inter_Qij.txt', np.c_[Inter_Qij],fmt='%f',delimiter='\t')
np.savetxt('Intra_tau.txt', np.c_[Intra],fmt='%f',delimiter='\t')
np.savetxt('Inter_tau.txt', np.c_[Inter],fmt='%f',delimiter='\t')

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Inter,cmap='Greens',origin='lower',norm=LogNorm(vmin=1,vmax=100))

cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)

plt.tick_params(length=7,pad=10,width = 3,direction='in')
# tick_locator = ticker.MaxNLocator(nbins=5)
cb5.set_ticks([1,100])
# cb5.locator = tick_locator
# im5.set_clim(0,20)
cb5.update_ticks()
cb5.ax.set_title(chr(964)+' (ns)',pad=20,fontdict={'size':15,'family':'Cabril'})
# plt.title(r'$U_{LJ}$',fontsize=32)
# plt.xlabel('Residues index',fontsize=30)
# plt.ylabel('Residues index',fontsize=30)
plt.xticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.yticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Inter_tau_%d.png' %(Per))
plt.close()

fig5 = plt.figure(figsize=(8,6),dpi=1000)
ax5 = fig5.gca()
im5 = ax5.imshow(Intra,cmap='Greens',origin='lower',norm=LogNorm(vmin=1,vmax=100))

cb5 = plt.colorbar(im5,pad=0.05)
cb5.ax.tick_params(labelsize=20)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
# tick_locator = ticker.MaxNLocator(nbins=5)
cb5.set_ticks([1,100])
# cb5.locator = tick_locator
# im5.set_clim(0,20)
cb5.update_ticks()
cb5.ax.set_title(chr(964)+' (ns)',pad=20,fontdict={'size':15,'family':'Cabril'})
# plt.title(r'$U_{LJ}$',fontsize=32)
# plt.xlabel('Struct',fontsize=30)
# plt.ylabel('Structure',fontsize=30)
plt.xticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.yticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig5.savefig('Intra_tau_%d.png' %(Per))
plt.close()

fig1 = plt.figure(figsize=(8,6),dpi=1000)
ax1 = fig1.gca()
im1 = ax1.imshow(Inter_Qij,cmap='Reds',origin='lower',norm=LogNorm(vmin=0.0001,vmax=0.001))

cb1 = plt.colorbar(im1,pad=0.05)
cb1.ax.tick_params(labelsize=20)

plt.tick_params(length=7,pad=10,width = 3,direction='in')
# tick_locator = ticker.MaxNLocator(nbins=5)
cb1.set_ticks([0.0001,0.001])
# cb5.locator = tick_locator
# im5.set_clim(0,20)
cb1.update_ticks()
# cb1.ax.set_title(,pad=20,fontdict={'size':15,'family':'Cabril'})
# plt.title(r'$U_{LJ}$',fontsize=32)
# plt.xlabel('Residues index',fontsize=30)
# plt.ylabel('Residues index',fontsize=30)
plt.xticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.yticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig1.savefig('Inter_Qij_%d.png' %(Per))
plt.close()

fig2 = plt.figure(figsize=(8,6),dpi=1000)
ax2 = fig2.gca()
im2 = ax2.imshow(Intra_Qij,cmap='Reds',origin='lower',norm=LogNorm(vmin=0.001,vmax=0.01))

cb2 = plt.colorbar(im2,pad=0.05)
cb2.ax.tick_params(labelsize=20)
plt.tick_params(length=7,pad=10,width = 3,direction='in')
# tick_locator = ticker.MaxNLocator(nbins=5)
cb2.set_ticks([0.001,0.01])
# cb5.locator = tick_locator
# im5.set_clim(0,20)
cb2.update_ticks()
# cb2.ax.set_title(chr(964)+' (ns)',pad=20,fontdict={'size':15,'family':'Cabril'})
# plt.title(r'$U_{LJ}$',fontsize=32)
# plt.xlabel('Struct',fontsize=30)
# plt.ylabel('Structure',fontsize=30)
plt.xticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.yticks([0,1,2],labels=['IDR1','Helix','IDR2'],size=24)
plt.subplots_adjust(bottom=0.2,left=0.2)
fig2.savefig('Intra_Qij_%d.png' %(Per))
plt.close()