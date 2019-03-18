
from helix_class import double_helix as dh
import networkx as nx
import random
import matplotlib.pyplot as plt


base_pairs = 5500
root_helix = dh(base_pairs,base_pairs,base_pairs,base_pairs)
root_helix.set_parent(None)
iteration = 0
helix_array = []
G = nx.DiGraph()
pd = 80
upper_limit = 2**9
dictionary = {}



def replicate_top_helix_with_prob(arr):
    A,B = arr[0], arr[1]
    new_top = dh(A,B,A,B)
    new_top.iter_decrease_with_probability()
    return new_top, new_top.A == A and new_top.D == B


#returns true if the array did not decrease
def replicate_bottom_helix_with_prob(arr):
    # get a[1,0] and a[1,1] from array

    C, D = arr[0],arr[1]
    new_bottom = dh(C,D,C,D)
    new_bottom.iter_decrease_with_probability()
    return new_bottom, new_bottom.A == C and new_bottom.D == D


def replicate_top_helix(arr):
    A,B = arr[0], arr[1]
    new_top = dh(A,B,A,B)
    new_top.iter_decrease()
    return new_top


def replicate_bottom_helix(arr):
    # get a[1,0] and a[1,1] from array

    C, D = arr[0],arr[1]
    new_bottom = dh(C,D,C,D)
    new_bottom.iter_decrease()
    return new_bottom



while iteration < pd:
    # start_pos starts with 0

    if iteration > 1:

        start_pos = iteration - 2
        repeat = len(helix_array[start_pos])
        if repeat >= 2**10:
            print(repeat)
            random_sample = random.sample(helix_array[start_pos],upper_limit)
            helix_array[start_pos] = random_sample
            repeat = len(helix_array[start_pos])

        array_at_height = []

        for i in range(repeat):

            # assign parent to duplicate children from

            parent_helix = helix_array[start_pos][i]

            top_helix, didnt_replicate = replicate_top_helix_with_prob(parent_helix.get_top())
            if didnt_replicate:
                array_at_height.append(parent_helix)
            else:
                top_helix.set_parent(parent_helix)
                top_helix.add_iter(iteration)
                top_helix.set_top()
                array_at_height.append(top_helix)

            bottom_helix, didnt_replicate = replicate_bottom_helix_with_prob(parent_helix.get_bottom())


            if didnt_replicate:
                array_at_height.append(parent_helix)
            else:
                bottom_helix.set_parent(parent_helix)
                bottom_helix.add_iter(iteration)
                bottom_helix.set_bottom()

                # for every time a cell is senescent, then number to a count to retrieve how many cells died
                array_at_height.append(bottom_helix)

        helix_array.append(array_at_height)

    elif iteration == 1:

        parent_helix = helix_array[0][0]

        top_helix = replicate_top_helix(parent_helix.get_top())

        top_helix.set_parent(parent_helix)
        top_helix.add_iter(iteration)
        top_helix.set_top()

        bottom_helix = replicate_bottom_helix(parent_helix.get_bottom())

        bottom_helix.set_parent(parent_helix)
        bottom_helix.add_iter(iteration)
        bottom_helix.set_bottom()

        iteration_array = [top_helix,bottom_helix]

        # loop through nested array of helix_array and create children for each element
        # if element does not duplicate, then copy it to the next array. Have a boolean that indicates if the matrix decreased
        # if cell becomes senescent, then dont copy it to the next array maybe append death iteration number and population doubling number

    else:
        helix_array.append([root_helix])

    iteration += 1


def print_results(array):
    # G.add_node(array[0])
    count = 2
    for level, arr in enumerate(array):
        for object in arr:
            if level > 0:
                print(object.get_matrix(), level)
                count += 1
    return count






print(print_results(helix_array))
print([len(x) for x in helix_array])

dictionary = {3: 27, 34: 1, 3: 72, 4: 62, 5: 33, 6: 36}
plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
plt.show()


    #     G.add_edge(*(obj.parent, obj))
    #     G.node[obj]['matrix'] = obj.get_matrix()
    # nx.write_adjlist(G, sys.stdout.buffer)  # write adjacency list to screen
    # # write edgelist to grid.edgelist
    # nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
    # # read edgelist from grid.edgelist
    # H = nx.read_edgelist(path="grid.edgelist", delimiter=":")
    # # print("Edges of graph: ")
    # # print(G.edges())
    # nx.draw(H)
    # plt.show()
