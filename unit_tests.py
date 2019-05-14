from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt

# Chromosome level tests
base_pairs = 5500
chromosome = cm(base_pairs, base_pairs, base_pairs, base_pairs)
print("chromosome matrix starting with: {}".format(chromosome.get_matrix()))
chromosome.iter_decrease()
print("chromosome after calling iter_decrease: {}".format(chromosome.get_matrix()))
chromosome.abrupt_bottom_shortening()
chromosome.abrupt_bottom_shortening()

# Cell level tests
new_chromosome = cm(base_pairs, base_pairs, base_pairs, base_pairs)
starting_cell = cell([cm(base_pairs, base_pairs, base_pairs, base_pairs) for x in range(46)])
print("the smallest telomere of the cell: {}".format(starting_cell.get_min))
print(starting_cell.replicate())


# Simulation Level Tests
