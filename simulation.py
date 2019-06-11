from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')
smallest_array = []

base_pairs = 1000
root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
root_cell = cell(root_array)
root_sim = sm(root_cell, 8, 0)
root_sim.start()
