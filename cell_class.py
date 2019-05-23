from helix_class import chromosome_matrix as cm
import random

def replicate_top_chromosome(arr):
    A, B = arr[0], arr[1]
    new_top = cm(A, B, A, B)
    new_top.iter_decrease()
    new_top.abrupt_top_shortening()
    return new_top


def replicate_bottom_chromosome(arr):
    # get a[1,0] and a[1,1] from array
    C, D = arr[0], arr[1]
    new_bottom = cm(C, D, C, D)
    new_bottom.iter_decrease()
    new_bottom.abrupt_bottom_shortening()
    return new_bottom


def make_cells_from_array(chromosome_array):
    cell_array = []
    for j in range(int(len(chromosome_array) / 46)):
        cell_sample = random.sample(chromosome_array, 46)
        for i in cell_sample:
            chromosome_array.remove(i)
        cell_array.append(cell(cell_sample))
    return cell_array


class cell:

    # to initialize the class cell, an array of 46 chromosome matrix arrays has to be passed as an argument
    def __init__(self, chromosome_array):
        self.chromosome_array = chromosome_array
        self.is_cell_senescent = False

        if len(chromosome_array) != 46:
            print("cell not properly initialized, {} elements missing".format(len(chromosome_array)-46))

    def get_chromosomes(self):
        return self.chromosome_array

    def print_chromosomes(self):
        for cell in self.chromosome_array:
            print(cell.get_matrix())

    # is_sencescent returns a boolean if any telomere length is less than or equal to zero
    def is_senescent(self):
        condition = False
        for chromosome in self.chromosome_array:
            if chromosome.has_zero() == True:
                condition = True
                break
        return condition

    # was senescent returns a boolean if the cell was previously set as senescent
    def was_senescent(self):
        condition = False
        for chromosome in self.chromosome_array:
            if chromosome.is_senescent:
                condition = True
                break
        return condition

    # loops through all chromosome matrix arrays to return the minimum element of the array of arrays
    def get_min(self):
        result = 5500
        for chromosome in self.chromosome_array:
            minimum = chromosome.get_min()
            if minimum < result:
                result = chromosome.get_min()
        return result

    # the function can_replicate will return a boolean based on a uniformly distributed probability and will also
    # check if the whole cell is senescent
    def can_replicate(self):
        condition = False
        alpha = 0.80
        beta = 4
        base_pairs = 5500
        shortest_chromosome = self.get_min()
        if shortest_chromosome < 0:
            shortest_chromosome = 0

        probability = alpha * (1 - (shortest_chromosome/ base_pairs)) ** beta
        if random.random() > probability:
            condition = True
        return condition

    def replicate(self):
        temp_array = []
        for parent_chromosomes in self.get_chromosomes():
            bottom_chromosome = replicate_bottom_chromosome(parent_chromosomes.get_bottom())
            bottom_chromosome.set_parent(parent_chromosomes)
            top_chromosome = replicate_top_chromosome(parent_chromosomes.get_top())
            top_chromosome.set_parent(parent_chromosomes)
            temp_array.append(bottom_chromosome)
            temp_array.append(top_chromosome)
        return make_cells_from_array(temp_array)
    # makes all of the matrices that constitute it as senescent.
    def make_senescent(self):
        for chromosome in self.chromosome_array:
            chromosome.is_senescent = True

    def get_mean_telomere(self):
        telomere_lengths = 0
        for chromosome in self.chromosome_array:
            telomere_lengths += chromosome.get_mean()
        return telomere_lengths/46






