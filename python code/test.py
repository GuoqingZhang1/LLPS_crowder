import numpy as np

Distance_t=np.zeros([101,300,300])

Mean=np.ones([300,300])

Sum=np.ones([300,300])*1000

print(((Distance_t[1]-Mean)*(Distance_t[50]-Mean)/Sum).shape)