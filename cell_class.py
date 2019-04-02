from helix_class import chromosome_matrix as cm
import random

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
        alpha = 0.8
        beta = 4
        base_pairs = 5500
        probability = alpha * (1 - (self.get_min() / base_pairs)) ** beta
        if random.random() > probability:
            condition = True
        return condition

    # makes all of the matrices that constitute it as senescent.
    def make_senescent(self):
        for chromosome in self.chromosome_array:
            chromosome.is_senescent = True





