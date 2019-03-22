from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import random
plt.style.use('seaborn-whitegrid')
base_pairs = 5500
# root array is an array of 46 chromosome matrices
array = []
for i in range(100):
    root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
    # root cell will be used to initialize the simulation class
    root_cell = cell(root_array)
    full_sim = sm(root_cell, 8, 0)
    x = full_sim.start()
    array.append(x)
    print(i+1, x)
# x = range(len(full_sim.percent_array))
# y = full_sim.percent_array
# plt.plot(x, y, 'o', color='black');


# array = inst.start()
# mother_cell = random.choice(array)
# mother_sim = sm(mother_cell, 8, 16)
# cell_culture = mother_sim.start()
# iteration_array = []
# for seed_cell in cell_culture:
#     seed_sim = sm(seed_cell, 7, 0)
#     # because of the upper bound, the start method will return a 200 cell array
#     iteration_array.append(seed_sim.start())
print(array)
plt.hist(array, bins=20)
plt.ylabel('counts')
plt.xlabel("PD")
plt.show()

# things that are missing: If a cell becomes senescent, then copy the cell, and keep it grouped.
                            #senescence is being counted if the cell cant replicate
                            #changed the sample size to 100 instead of 200

# generate histogram for PD counts with different alpha values : 0.8,0.85,0.9
# 100 runs per value
# run the 200 cell culture by taking the chromosome that has the shortest telomere and  copying to make a new cell...
