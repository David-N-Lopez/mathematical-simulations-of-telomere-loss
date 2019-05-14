from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')
smallest_array = []

base_pairs = 5500
root_array = [cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)]
root_cell = cell(root_array)
root_sim = sm(root_cell, 9, 23)
root_sim.resample_num = 1
mother_cell = root_sim.start()
mother_sim = sm(mother_cell[0], 9, 16)
mother_sim.resample_num = 150
sample_cells = mother_sim.start()





# print(sample_cells)
a_80 = []


shortest_pd_array = []
shortest_avg_array= []
pd_array = []
avg_array = []
max = 0
for cl in sample_cells:
    sample_base = cl.get_min()
    sample_array = [cm(sample_base,sample_base,sample_base,sample_base) for x in range(46)]
    sample_cell = cell(sample_array)
    full_sim = sm(sample_cell, 6, 0)
    x = full_sim.start()
    print(x)
    a_80.append(x+39)
    # if x == 1:
    #     shortest_pd_array = root_sim.population_doublings_array + full_sim.population_doublings_array
    #     shortest_avg_array = root_sim.shortest_length_array+ full_sim.shortest_length_array
    # if x >= 22:
    #     avg_pd = []
    #     for i in full_sim.population_doublings_array:
    #         avg_pd.append(i+39)
    #     print(avg_pd)
    #     pd_array = root_sim.population_doublings_array + avg_pd
    #     print(len(pd_array))
    #     avg_array = root_sim.shortest_length_array + full_sim.shortest_length_array
    #     print(len(avg_array))

# y_short = np.asarray(shortest_avg_array)
# x_short = np.asarray(shortest_pd_array)
# x_long = np.asarray(pd_array)
# y_long = np.asarray(avg_array)
#
# plt.subplot(2,1,1)
#
#
# plt.ylabel("smallest avg telomere length - shorter")
# plt.plot(shortest_pd_array, shortest_avg_array, '.')
# plt.subplot(2,1,2)
# plt.xlabel("population doublings")
# plt.ylabel("smallest avg telomere length - longer")
# plt.plot(pd_array, avg_array, '.')
# plt.show()






# sorted(smallest_array, key= sort_on_last)
# min_length_y = smallest_array[-1][1]
# min_length_x = smallest_array[-1][0]
# max_length_y = smallest_array[0][1]
# max_length_x = smallest_array[0][0]
#
# plt.plot(list(range(len(min_length_x))), min_length_y, '.', color='blue')
# plt.ylabel('smallest average length - min')
# # plt.plot(np.linspace(0,len(max_length)), max_length, '.', color='red')
# # plt.ylabel('smallest average length - max')
# plt.title("min population doublings'")
#
# plt.xlabel("population doubling")
# plt.show()

#############################################################################

# cell_lengths = [[len(x),x] for x in smallest_array]
# sorted(cell_lengths, key=sort_on_first)
# min_length = cell_lengths[-1][1]
# max_length = cell_lengths[0][1]
# population_doubling_attempts = np.linspace(0,len(min_length))
# plt.plot(list(range(len(min_length))), min_length, '.', color='blue')
# plt.ylabel('smallest average length - min')
# plt.title("min population doublings'")


print(a_80)
plt.title("cell 'death' histogram of 150 runs and B = 1e-2")
plt.hist(a_80, bins=40, alpha=0.80, label='alpha = 0.80')
plt.ylabel('counts')
plt.xlabel("population doublings")
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