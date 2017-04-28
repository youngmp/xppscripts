import numpy as np
import matplotlib.pyplot as plt

from collect_disjoint_branches import collect_disjoint_branches as collect

# load all info bifurcation data from XPPAUTO
bif = np.loadtxt('twod_wave_trunc_exist_all.dat')

# collect the disjoint branches. Branches are saved to a dictionary.
# val are the branch values as a function of the parameter
# ty is the stability type
val,ty = collect(bif,remove_isolated=True,remove_redundant=True,redundant_threshold=.05,isolated_number=50)


# display the branch numbers
print val.keys()

fig = plt.figure()
ax = fig.add_subplot(111)

for key in val.keys():
    ax.plot(val[key][:,1],val[key][:,2],label=key)
    
    ax.legend()
plt.show()

