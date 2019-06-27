from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')
smallest_array = []
M = 10
Kr = 0.01
alpha = 0.001
base_pairs = 4000
p = 0.005
root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
root_cell = cell(root_array)
root_sim = sm(root_cell, 8, 0)
root_sim.start()
population = root_sim.total_population_array
# normal_prop = root_sim.normal_cells
# single_mutated = root_sim.single_mutated
# double_mutated = root_sim.double_mutated

plt.title("Attempts:  Kr = {} alpha {}  p = {}".format(Kr, alpha, p))
# plt.ylabel("proportion")
# plt.scatter(list(range(len(normal_prop))),normal_prop, color = 'g',marker = '.', label = 'normal')
# plt.scatter(list(range(len(single_mutated))),single_mutated, color = 'b',marker = '.', label = 'm1')
# plt.scatter(list(range(len(double_mutated))),double_mutated, color = 'k',marker = '.', label = 'm2')
print("the population array with M: {} , Kr: {}, alpha:{}, and p:{}".format(M, Kr, alpha, p))
print(population)
attempted_population_doublings = list(range(len(population)))
plt.plot(attempted_population_doublings, population, color = "b")
plt.show()