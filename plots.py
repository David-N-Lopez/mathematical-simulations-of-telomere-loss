from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
base_pairs = 5500
probability = []
dep_var = list(range(base_pairs, 0, -1))
for i in dep_var:
    alpha = 0.8
    beta = 4
    probability.append(1-(alpha*(1-(i/base_pairs))**beta))


x = dep_var
y = probability
print(x)
print(y)
plt.plot(x, y, '.', color='blue')
plt.ylabel('probability')
plt.xlabel("shortest telomere length")
plt.show()
