# plotting change in flux over time, to be used on CITA server!
# heating model of file grmhd_restart_beta_1e2_cooling_121_a9_electrons

import numpy as np
import matplotlib.pyplot as plt
import glob
import re
import os
import h5py 

# folder with .npz files
athdf_folder = "/fs/lustre/project/EXTRARAID-CITA/sressler/Stampede2/grmhd_restart_beta_1e2_cooling_121_a9_electrons"
npz_folder = "/fs/lustre/scratch/RAID-CITA/bonniecao/blacklight_ricky2/output"

res = 256
D = 8127.0 * 3.0857e18

npz_files = sorted(glob.glob(os.path.join(npz_folder, "*.npz")))

times = []
fluxes = []

for npz_file in npz_files:
    
    dic = np.load(npz_file)

    dx =  dic["width"] / res
    Flux  = np.sum(dic["I_nu"]) * dx**2/(D**2)
    Flux_jy = Flux / 1e-23

    # get number from file name
    nums = re.findall(r"\d+", os.path.basename(npz_file))
    dump_number = int(nums[-1]) if nums else len(times)

    athdf_file = os.path.join(
        athdf_folder,
        f"star_wind.out2.{dump_number:05d}.athdf"
    )

    # read time from athdf
    with h5py.File(athdf_file, "r") as f:
        time = float(f.attrs["Time"]) / 1000.0

    times.append(time)
    fluxes.append(Flux_jy)

plt.plot(times, fluxes, label="heating model")

plt.xlabel("time [1000M]")
plt.ylabel("flux [Jy]")
plt.title("grmhd_restart_beta_1e2_cooling_121_a9_electrons heating model")
plt.show()