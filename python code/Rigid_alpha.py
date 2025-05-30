

f_rigid=open('CTD_100.rigid','w')

N_m=100
N_res=148

f_rigid.write('group alpha id ')
for i in range(N_m):
    f_rigid.write(' %d:%d ' %(i*N_res+52,i*N_res+74))
    
f_rigid.close()