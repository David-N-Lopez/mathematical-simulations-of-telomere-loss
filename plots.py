from sim_with_cells import simulation_with_cells as sm
from cell_class import cell
from helix_class import chromosome_matrix as cm
import matplotlib.pyplot as plt
import math

plt.style.use('seaborn-whitegrid')
base_pairs = 8000
probability = []
dep_var = list(range(base_pairs, 0, -1))
for i in dep_var:
    B = 0.003561
    C = 1776.6
    D = 0.56846
    probability.append(B * math.exp(-((math.log(i / C)) / D) ** 2))


x = dep_var
y = probability
print(x)
print(y)
plt.plot(x, y, '.', color='blue')
plt.ylabel('probability')
plt.xlabel("shortest telomere length")
plt.show()
