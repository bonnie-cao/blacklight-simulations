# plotting change in flux over dump number
# heating model of file grmhd_restart_beta_1e2_cooling_121_a9_electrons

import numpy as np
import matplotlib.pyplot as plt
import glob
import re
import os

# folder with .npz files
folder = "/Users/bonniecao/Documents/blacklight/output/ricky_outputs5"

res = 256
D = 8127.0 * 3.0857e18

files = sorted(glob.glob(folder + "/*.npz"))

times = []
fluxes = []

for file in files:
    dic = np.load(file)

    dx =  dic["width"] / res
    Flux  = np.sum(dic["I_nu"]) * dx**2/(D**2)
    Flux_jy = Flux / 1e-23

    # get number from filename
    nums = re.findall(r"\d+", os.path.basename(file))
    time = int(nums[-1]) if nums else len(times)

    times.append(time)
    fluxes.append(Flux_jy)

plt.plot(times, fluxes, label="heating model")

plt.xlabel("dump number")
plt.ylabel("flux [Jy]")
plt.title("grmhd_restart_beta_1e2_cooling_121_a9_electrons")
plt.show()