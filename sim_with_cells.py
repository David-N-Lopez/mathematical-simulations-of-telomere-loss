from helix_class import chromosome_matrix as cm
from cell_class import cell
import random
import math
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


# re-sample an array with an upper limit set as "to"

def resample(array, to):
    resampled_array = random.sample(array, to)
    return resampled_array


# helper function for eliminating senescent cells from the current array

def get_non_senescent_cells(cell_array):
    cell_array = [x for x in cell_array if x.is_not_senescent()]
    return cell_array


# helper function to eliminate cells after apoptosis with probability described by
# JCB 2019 paper


def alive_cells_after_apoptosis(cell_array):
    new_cell_array = []
    for cell in cell_array:
        cell_min = cell.get_min()

        # alpha value in the JCB paper was set to 0.001
        alpha = 0.001
        probability = math.exp(-alpha * cell_min)
        if random.random() > probability:
            new_cell_array.append(cell)
    return new_cell_array

class simulation_with_cells:
    def __init__(self, cell, upper, max_doublings):
        # initial seed cell that starts the simulation

        self.cell = cell
        self.upper = upper
        self.max_doublings = max_doublings

        # sim array will be a list of list that contain our matrices

        self.sim_array = []
        self.iteration = 0
        self.cond = True
        self.percent_array = []
        self.total_population = 1
        self.total_population_array = []
        self.multiplier = 1
        self.population_doublings_array = []
        self.shortest_length_array = []
        self.length_average_array = []
        self.resample_num = 200

        # the initial conditions for the JCB paper start with 5000 cells as part of the
        # initial culture

        initial_culture = [self.cell for x in range(5000)]
        self.sim_array.append(initial_culture)

    def start(self):

        # While loops through each level of the binary tree
        while self.cond:
            cell_array_at_iteration = self.sim_array[self.iteration]
            print(len(cell_array_at_iteration))

            cell_array_before_apoptosis = get_non_senescent_cells(cell_array_at_iteration)
            print(len(cell_array_before_apoptosis))
            cell_array = alive_cells_after_apoptosis(cell_array_before_apoptosis)
            print(len(cell_array))
            print("*********************")

            if len(cell_array) == 0:
                return math.log(self.total_population, 2)
            # temp array will be appended to
            temp_array = []
            cell_divider_counter = 0
            # senescence_count will keep track of how many cells have become senescent
            for cells in cell_array:
                if cells.can_replicate():
                    temp_array.append(cells.replicate())
                    cell_divider_counter += 1
                else:
                    temp_array.append([cells])

            self.iteration += 1
            not_senescent_cells = []
            for cell_pair in temp_array:
                for cell in cell_pair:
                    not_senescent_cells.append(cell)
            # total cells will now only depend on the not senescent cells
            # this is based on the JCB 2019 paper.
            total_cells = not_senescent_cells

            # re-sampling if the sample goes beyond 2^upper bound of the parameters
            if len(total_cells) >= 5000:
                self.multiplier *= (len(total_cells) / 5000)
                new_temp = resample(total_cells, 5000)
                total_cells = new_temp

            # append cells to the next level
            self.sim_array.append(total_cells)
            self.total_population += (cell_divider_counter+1) * self.multiplier
            self.total_population_array.append(math.log10((cell_divider_counter+1)* self.multiplier))

            # if max_doublings is equal to zero then we want the simulation to run until its end
            # then we want to return a random sample of 200 cells
            if self.max_doublings != 0 and self.max_doublings <= math.log(self.total_population, 2):
                new_sample = resample(total_cells, self.resample_num)
                return new_sample
            senescence_count = 0
            smallest_cell_average = 0
            length_average = 0
            for cl in total_cells:
                if cl.is_cell_senescent:
                    senescence_count += 1
                smallest_cell_average += cl.get_min()
                length_average += cl.get_mean_telomere()
            smallest_cell_average /= len(total_cells)
            length_average /= len(total_cells)
            self.percent_array.append((senescence_count / len(total_cells)) * 100)
            self.length_average_array.append(length_average)
            self.population_doublings_array.append(math.log(self.total_population, 2))
            self.shortest_length_array.append(smallest_cell_average)

            # in the end, if self.sim_array at the current iteration is greater than the upper bound. resample.
