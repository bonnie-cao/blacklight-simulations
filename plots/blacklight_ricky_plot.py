import numpy as np
import matplotlib.pyplot as plt

dic = np.load("/Users/bonniecao/Documents/blacklight/output/ricky_output3/dump_00001.npz")

res = 256 ## change to whatever you set in the input file
dx =  dic["width"] / res
D = 8127.0 * 3.0857e18   ## distance to Sgr A* in cm
Flux  = np.sum(dic["I_nu"]) * dx**2/(D**2)

Flux_Jy = Flux / 1e-23
print(Flux_Jy)

dic = np.load("/Users/bonniecao/Documents/blacklight/output/ricky_output3/dump_00016.npz")
plt.pcolormesh(dic['I_nu'])
plt.show()