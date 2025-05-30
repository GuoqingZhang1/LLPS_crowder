
Saa=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

Taa=['ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL']

Mass=[71.08,156.20,114.10,115.10,103.10,128.10,129.10,57.05,137.10,113.20,113.20,128.20,131.20,147.20,97.12,87.08,101.10,186.20,163.20,99.07]

Sigma=[5.04,6.56,5.68,5.58,5.48,6.02,5.92,4.50,6.08,6.18,6.18,6.36,6.18,6.36,5.56,5.18,5.62,6.78,6.46,5.86]

Lambda=[0.602942,0.558824,0.588236,0.294119,0.64706,0.558824,0.0,0.57353,0.764707,0.705883,0.720589,0.382354,0.676471,0.82353,0.758824,0.588236,0.588236,1.0,0.897059,0.664707]

miu=1
delta=0.08

f_in=open("pair_ljlambda_exclude.in",'w')
f_in.write('#Mass\n')
for i in range(20):
    f_in.write('mass %d %f\n' %(i+1,Mass[i]))
f_in.write('mass %d %f\n' %(21,1500))
f_in.write('\n')
f_in.write('#Pair Coeff\n')


#typei typej epsilon sigma lambda lj_cut coul_cut
for i in range(20):

    for j in range(i,20):   
        coul_cut=0
        if (Taa[i]=='ARG' or Taa[i]=='LYS' or Taa[i]=='ASP' or Taa[i]=='GLU' ) and (Taa[j]=='ARG' or Taa[j]=='LYS' or Taa[j]=='ASP' or Taa[j]=='GLU' ):
            coul_cut=35
        
        f_in.write('pair_coeff %d %d ljlambda %f %f %f %f %F\n' %(i+1,j+1,0.2,0.5*(Sigma[i]+Sigma[j]),miu*0.5*(Lambda[i]+Lambda[j])-delta,4*0.5*(Sigma[i]+Sigma[j]),coul_cut))

for i in range(20):
    f_in.write('pair_coeff %d %d lj/exclude %f %f %f %F\n' %(i+1,21,0.2,6,3.82/2+8-6,35))
f_in.write('pair_coeff %d %d lj/exclude %f %f %f %F\n' %(21,21,0.2,6,8+8-6,35))