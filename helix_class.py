import random
import math

class chromosome_matrix():

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

    def probability(self, L):
        B = 0.003561
        C = 1776.6
        D = 0.56846
        probability = B*math.exp(-((math.log(L/C))/D)**2)
        #1999 paper shortening:

        # probability = math.exp(((L-30)/6.65))+10
        return probability

    def abrupt_top_shortening(self):
        L = self.B
        probability = self.probability(L)
        if probability < 0:
            probability = 0
        random_num = random.random()
        if random_num < probability:
            H = 2400
            self.B -= H
            self.D -= H

    def abrupt_bottom_shortening(self):
        L = self.C
        probability = self.probability(L)
        if probability < 0:
            probability = 0
        random_num = random.random()
        if random_num < probability:
            H = 2400
            self.A -= H
            self.C -= H

    def iter_decrease(self):
        rand_val_a = int(random.uniform(50, 200))
        rand_val_d = int(random.uniform(50, 200))
        self.A -= rand_val_a
        self.D -= rand_val_d

    def get_matrix(self):
        return [[self.A, self.B], [self.C, self.D]]

    def get_min(self):
        minimum = min(self.A, self.B, self.C, self.D)
        if minimum < 0:
            minimum = 0
        return minimum

    def get_mean(self):
        return (self.A+self.B+self.C+self.D)/4

    def has_zero(self):
        if self.get_min() <= 0:
            return True
        else:
            return False





# x = double_helix(base_pairs,base_pairs,base_pairs,base_pairs)
# print(x.A)
# x.rand_decrease('A')
# print(x.A)

