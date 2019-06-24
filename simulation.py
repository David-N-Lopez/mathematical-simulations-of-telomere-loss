from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')
smallest_array = []

base_pairs = 4000
root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
root_cell = cell(root_array)
root_sim = sm(root_cell, 8, 0)
root_sim.start()
population = root_sim.total_population_array
print(population)
population_doublings = root_sim.total_population_array
print(population_doublings)
plt.plot(population_doublings, population)
plt.xlabel("real population doublings")
plt.ylabel("population")
plt.title("M=10 Kr = 0.1 alpha 0.001/ 4000bp/ p=0.005")
plt.show()
