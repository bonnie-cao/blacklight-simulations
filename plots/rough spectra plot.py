
import numpy as np
import matplotlib.pyplot as plt

dic = np.load("/Users/bonniecao/Documents/blacklight/output/freq_1e10.npz")
plt.pcolormesh(dic['I_nu'])
plt.show()

freqs = np.array([1e10, 1e11, 1e12, 1e13, 1e14, 1e15])
fluxes = []

for f in freqs:
    dic = np.load(f"../output/freq_{f:.0e}.npz".replace("+", ""))
    fluxes.append(np.sum(dic["I_nu"]))

plt.loglog(freqs, fluxes, marker="o")
plt.xlabel("frequency (Hz)")
plt.ylabel("rough flux")
plt.title("spectral graph")
plt.show()