import dionysus._dionysus as d
import dionysus.plot as plot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SPY = pd.read_csv("SPY.csv")
SPY = SPY.iloc[:,1:].sample(250)
SPY = SPY.values

print("Generating Rips filtration...")
rips_filtration = d.fill_rips(SPY, 2, 300000)
print(rips_filtration)

# Compute the persistent homology of the filtration
print("Computing persistent homology of Rips filtration...")
persistence = d.homology_persistence(rips_filtration)
diag = d.init_diagrams(persistence, rips_filtration)

# Show the cluster and bar diagrams
plot.plot_bars(diag[0], show = True)