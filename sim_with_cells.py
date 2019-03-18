from helix_class import chromosome_matrix as cm
from cell_class import cell
import random
import math


# Start with 46 matrices
# Randomly group matrices in 46
# Every iteration we test probability (with smallest num of all matrices and we test for senescence)
# if true duplicate them all
# if not copy the whole cell
# once reached 39pds sample randomly 200 cells
# start the simulation for each one individually

def replicate_top_chromosome(arr):
    A, B = arr[0], arr[1]
    new_top = cm(A, B, A, B)
    new_top.iter_decrease()
    return new_top


def replicate_bottom_chromosome(arr):
    # get a[1,0] and a[1,1] from array

    C, D = arr[0], arr[1]
    new_bottom = cm(C, D, C, D)
    new_bottom.iter_decrease()
    return new_bottom


def resample(array, to):
    resampled_array = random.sample(array, to)
    return resampled_array

#this is erasing the elements inside cell_array
def make_cells_from_array(chromosome_array):
    cell_array = []
    for j in range(int(len(chromosome_array) / 46)):
        cell_sample = random.sample(chromosome_array, 46)
        for i in cell_sample:
            chromosome_array.remove(i)
        cell_array.append(cell(cell_sample))
    return cell_array


class simulation_with_cells:
    def __init__(self, cell, upper, max_doublings):
        self.cell = cell
        self.upper = upper
        self.max_doublings = max_doublings
        self.sim_array = []
        self.iteration = 0
        self.cond = True
        self.sim_array.append(self.cell.get_chromosomes())
        self.matrix_count = 1
        self.percent_array = []

    def start(self):
        while self.cond:
            # sim array will be a list of list that contain our matrices
            # cell_array makes a an array of cell objects from sim_array
            cell_array = make_cells_from_array(self.sim_array[self.iteration])
            # temp array will be appended to
            temp_array = []
            #  senescence_count will keep track of how many cells have become senescent
            senescence_count = 0
            for cells in cell_array:
                if cells.can_replicate():
                    for chromo_matrix in cells.get_chromosomes():
                        parent_chromosomes = chromo_matrix.get_matrix()
                        bottom_chromosome = replicate_bottom_chromosome(parent_chromosomes[1])
                        bottom_chromosome.iter_decrease()
                        bottom_chromosome.set_parent(parent_chromosomes)
                        top_chromosome = replicate_top_chromosome(parent_chromosomes[0])
                        top_chromosome.iter_decrease()
                        top_chromosome.set_parent(parent_chromosomes)
                        temp_array.append(bottom_chromosome)
                        temp_array.append(top_chromosome)
                        self.matrix_count += 2
                else:
                    senescence_count += 1
                    if senescence_count == len(cell_array):
                        return self.iteration

                    for matrix in cells.get_chromosomes():
                        temp_array.append(matrix)

            self.iteration += 1

            # re-sampling if the sample goes beyond 2^upper bound of the parameters
            if len(temp_array) >= (2**(self.upper+1))*46:
                new_temp = resample(temp_array, (2**self.upper)*46)
                temp_array = new_temp
            self.sim_array.append(temp_array)

            # if max_doublings is equal to zero then we want the simulation to run until its end
            # then we want to return a random sample of 200 cells
            if self.max_doublings != 0 and self.max_doublings == self.iteration:
                print(len(temp_array))
                new_sample = resample(make_cells_from_array(temp_array),100)
                return new_sample
            print("simulation iterating for the {} th time".format(self.iteration))
            print("current number of cells at iteration level: 2^{}".format(math.log(len(temp_array)/46,2)))
            print("the number of PDs this iteration is: {}".format(math.log(self.matrix_count/46, 2)))
            print("the percentage of senescent cells is : {} %".format((senescence_count/len(cell_array)*100)))
            # This is just for graphing the percent increase
            self.percent_array.append(senescence_count / len(cell_array) * 100)



            # in the end, if self.sim_array at the current iteration is greater than the upper bound. resample.











# x = sim_array[iteration]
# cells make_cells_from_array[iteration]
# for cell in cells

