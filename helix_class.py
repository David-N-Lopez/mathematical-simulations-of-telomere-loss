import random

class double_helix():

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.parent = None
        self.iter = 0
        self.top = False
        self.bottom = False
        self.is_senescent = False

    def add_iter(self, num):
        self.iter = num

    def get_top(self):
        return [self.A, self.B]

    def set_top(self):
        self.top = True

    def get_bottom(self):
        return [self.C, self.D]

    def set_bottom(self):
        self.bottom = True

    def set_parent(self, parent):
        self.parent = parent

    def iter_decrease_with_probability(self):
        alpha = 0.8
        beta = 4
        base_pairs = 5500
        probability = alpha*(1-(self.get_min()/base_pairs))**beta
        #print("{} is given by 1 minus {}".format(probability,self.get_min()/base_pairs))
        if random.random() > probability:
            rand_val_a = int(random.uniform(50, 200))
            rand_val_d = int(random.uniform(50, 200))
            self.A -= rand_val_a
            self.D -= rand_val_d

    def iter_decrease(self):
        rand_val_a = int(random.uniform(50, 200))
        rand_val_d = int(random.uniform(50, 200))
        self.A -= rand_val_a
        self.D -= rand_val_d

    def abrupt_decrease(self):
        c1 = 100
        c2 = 300

        prob = rand_val = int(random.uniform(c1, c2))


    def probability_of_abrupt(B):
        k0 = -7.9233**-5
        k1 = 3.3968**-6
        k2 = -1.766**-8
        k3 = 3.478**-11
        k4 = -2.8912**-14
        k5 = 1.26**-17
        k6 = -3.1371**-21
        k7 = 4.4957**-25
        k8 = -3.4492**-29
        k9 = 1.0959**-33
        array = [k0,k1,k2,k3,k4,k5,k6,k7,k8,k9]
        return sum(el*(B**ind) for ind, el in enumerate(array))


    def get_matrix(self):
        return [[self.A, self.B], [self.C, self.D]]

    def get_min(self):
        return min(self.A, self.B, self.C, self.D)

    def is_senescent(self):
        if self.get_min() <= 0:
            return True
        else:
            return False





# x = double_helix(base_pairs,base_pairs,base_pairs,base_pairs)
# print(x.A)
# x.rand_decrease('A')
# print(x.A)

