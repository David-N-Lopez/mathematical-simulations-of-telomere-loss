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

# all the matrices that are part of a senescent cell are put in a separate array and then
# they are made into cells before the re-sampling call
# all other matrices are made into cells and then the senescent ones are put into a separate cell
# array. further of to be used for re-sampling calculations.
# need to add two methods in matrix and in cell.
# in matrix add a variable that stores a boolean if part of senescent cell
# in cell a method that sets all of it's matrices as part of senescent cell

def replicate_top_chromosome(arr):
    A, B = arr[0], arr[1]
    new_top = cm(A, B, A, B)
    new_top.abrupt_top_shortening()
    new_top.iter_decrease()
    return new_top


def replicate_bottom_chromosome(arr):
    # get a[1,0] and a[1,1] from array
    C, D = arr[0], arr[1]
    new_bottom = cm(C, D, C, D)
    new_bottom.abrupt_bottom_kshortening()
    new_bottom.iter_decrease()
    return new_bottom


def resample(array, to):
    resampled_array = random.sample(array, to)
    return resampled_array


# this is erasing the elements inside cell_array
def make_cells_from_array(chromosome_array):
    cell_array = []
    for j in range(int(len(chromosome_array) / 46)):
        cell_sample = random.sample(chromosome_array, 46)
        for i in cell_sample:
            chromosome_array.remove(i)
        cell_array.append(cell(cell_sample))
    return cell_array


def make_matrix_from_cells(cell_array):
    matrix_array = []
    for cells in cell_array:
        matrix_array += cells.get_chromosomes()
    return matrix_array


def get_senescent_cells_and_cells(cell_array):
    sen_cells = [x for x in cell_array if x.is_senescent()]
    cell_array = list(set(cell_array)^set(sen_cells))
    return sen_cells, cell_array


def get_senescent_matrices_and_mat(mat_array):
    senescent_mat_array = [x for x in mat_array if x.is_senescent]

    mat_array = list(set(mat_array)^ set(senescent_mat_array))
    return senescent_mat_array, mat_array



def make_cells_senescent(cell_array):
    for cl in cell_array:
        cl.is_cell_senescent = True


class simulation_with_cells:
    def __init__(self, cell, upper, max_doublings):
        # initial seed cell that starts the simulation
        self.cell = cell
        # upper is a variable that sets the upper limit before re-sampling
        # if during a level of the binary tree the number of cells grows larger than 2^upper
        # then we will re-sample
        self.upper = upper
        self.max_doublings = max_doublings
        # sim array will be a list of list that contain our matrices
        self.sim_array = []
        self.iteration = 0
        self.cond = True
        self.sim_array.append(self.cell.get_chromosomes())
        self.percent_array = []
        self.total_population = 1
        self.multiplier = 1
        self.population_doublings_array = []

    def start(self):

        # While loops through each level of the binary tree
        while self.cond:
            # list of chromosome matrices at given level
            mat_array_at_iteration = self.sim_array[self.iteration]
            # separates the matrices part of senescent cell in the previous iteration
            senescent_matrices, mat_array_at_iteration = get_senescent_matrices_and_mat(mat_array_at_iteration)
            senescent_cells = make_cells_from_array(senescent_matrices)
            # cell_array makes a an array of cell objects from sim_array
            cell_array = make_cells_from_array(mat_array_at_iteration)
            temp_senescent_cells, cell_array = get_senescent_cells_and_cells(cell_array)
            senescent_cells += temp_senescent_cells
            make_cells_senescent(senescent_cells)

            if len(cell_array) == 0:
                return self.population_doublings_array[-1]
            # temp array will be appended to
            temp_array = []
            cell_divider_counter = 0
            # senescence_count will keep track of how many cells have become senescent
            for cells in cell_array:
                if cells.can_replicate():
                    for parent_chromosomes in cells.get_chromosomes():
                        bottom_chromosome = replicate_bottom_chromosome(parent_chromosomes.get_bottom())
                        bottom_chromosome.set_parent(parent_chromosomes)
                        top_chromosome = replicate_top_chromosome(parent_chromosomes.get_top())
                        top_chromosome.set_parent(parent_chromosomes)
                        temp_array.append(bottom_chromosome)
                        temp_array.append(top_chromosome)
                    cell_divider_counter += 1

                else:
                    for matrix in cells.get_chromosomes():
                        temp_array.append(matrix)

            self.iteration += 1
            not_senescent_cells = make_cells_from_array(temp_array)
            total_cells = not_senescent_cells + senescent_cells

            # re-sampling if the sample goes beyond 2^upper bound of the parameters
            if len(total_cells) >= (2**(self.upper)):
                self.multiplier *= (len(total_cells) / 2 ** (self.upper))
                new_temp = resample(total_cells, (2**self.upper))
                total_cells = new_temp

            # append cells to the next level
            self.sim_array.append(make_matrix_from_cells(total_cells))
            self.total_population += cell_divider_counter*self.multiplier

            # if max_doublings is equal to zero then we want the simulation to run until its end
            # then we want to return a random sample of 200 cells
            if self.max_doublings != 0 and self.max_doublings == self.iteration:
                print(math.log((len(temp_array)/46),2))
                new_sample = resample(make_cells_from_array(temp_array),100)
                return new_sample
            senescence_count = 0
            for cl in total_cells:
                if cl.is_cell_senescent:
                    senescence_count += 1
            # print("the total number of senescent cells before resampling {}".format(len(senescent_cells)))
            # print("the total number of not senescent cells before re-sampling {}".format(len(not_senescent_cells)))
            # print("simulation iterating for the {} th time".format(self.iteration))
            # print("current number of cells at iteration level: 2^{}".format(math.log(len(total_cells),2)))
            # print("total number of population doublings {}".format(math.log(self.total_population,2)))
            #     # print("the number of PDs this iteration is {}".format(math.log(self.matrix_count/46, 2)))
            # print("the percentage of senescent cells is : {} %".format(((senescence_count/len(total_cells))*100)))
            #     # print("number of active cells at given iteration {}".format(len(cell_array)))
            #     # # This is just for graphing the percent increase

            self.percent_array.append((senescence_count / len(total_cells)) * 100)
            self.population_doublings_array.append(math.log(self.total_population,2))



            # in the end, if self.sim_array at the current iteration is greater than the upper bound. resample.











# x = sim_array[iteration]
# cells make_cells_from_array[iteration]
# for cell in cells

