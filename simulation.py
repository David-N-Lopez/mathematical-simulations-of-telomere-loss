from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import statistics
import random
plt.style.use('seaborn-whitegrid')
base_pairs = 5500
# # root array is an array of 46 chromosome matrices
# array = []
# for i in range(100):
#     root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
#     # root cell will be used to initialize the simulation class
#     root_cell = cell(root_array)
#     full_sim = sm(root_cell, 8, 0)
#     x = full_sim.start()
#     array.append(x)
#     print(i+1, x)
a_80 = []
for i in range(100):
    root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
    root_cell = cell(root_array)
    full_sim = sm(root_cell,8,0)
    a_80.append(full_sim.start())
    print(i)
print(a_80)
# x = full_sim.population_doublings_array
# y = full_sim.percent_array
# print(y)
# plt.plot(x, y, 'o', color='black')
#
#
# # array = inst.start()
# # mother_cell = random.choice(array)
# # mother_sim = sm(mother_cell, 8, 16)
# # cell_culture = mother_sim.start()
# # iteration_array = []
# # for seed_cell in cell_culture:
# #     seed_sim = sm(seed_cell, 7, 0)
# #     # because of the upper bound, the start method will return a 200 cell array
# #     iteration_array.append(seed_sim.start())
# print (array)


plt.hist(a_80, bins=40, alpha=0.5, label='alpha = 0.8')
# plt.hist(a_85, bins= 100,range= [0,120], alpha=0.5, label='alpha = 0.85')
# plt.hist(a_90, bins=100, range= [0,120], alpha=0.5, label='alpha = 0.9')
# plt.hist(a_95, bins=100,range= [0,120], alpha=0.5, label='alpha = 0.95')
# x = [0.8,0.85,0.9,0.95]
# y = [statistics.mean(a_80),statistics.mean(a_85),statistics.mean(a_90),statistics.mean(a_95)]
#
# plt.plot(x, y, 'o', color='blue');
#
plt.ylabel('count')
plt.xlabel("PDs")
plt.legend(loc='upper right')
plt.show()




#####################  Things to do #######################

# run the 200 cell culture by taking the chromosome that has the shortest telomere and  copying to make a new cell...


##New changes, copy the cell to the next level, but if it is senescent then don't unwind it -> this will help in the calculations
## Use PDs with the new jaggi formula that multiplies by

#things to do: implement bimodal distribution and compare it with the resampling procedure and thejust letting a cell run.
# When implementing the abrupt shortening if the cell divides (I believe considering prob of replication and senescence) then replicate all matrices without shortening
# and decide for abrupt shortening with nick's formula. In the future we want to vary the parameters and test for the varying peaks -> In the decision making process
# if l = 300 then the probability is 0. If the matrix undergoes abrupt shortening then
# Let the program run for alpha values incrementing from 0.8 to 0.94