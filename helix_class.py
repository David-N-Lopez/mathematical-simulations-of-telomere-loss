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

    def iter_decrease(self):
        rand_val_a = int(random.uniform(50, 200))
        rand_val_d = int(random.uniform(50, 200))
        self.A -= rand_val_a
        self.D -= rand_val_d
    def elongate(self):
        p = 0.026
        random_number = random.random()
        y = -math.log(1 - random_number) / p
        return y
    def elongate_or_shorten(self):

        Lo = 1000
        beta = 0.045
        if self.A > Lo:
            probability_A = 1/(1+beta*(self.A-Lo))
        else:
            probability_A = 1
        # print(probability_A)
        if random.random()< probability_A:
            # do elongation
            elongate_by = self.elongate()
            self.A += elongate_by

        else:
            # do shortening
            decrease_by = int(random.uniform(50,200))
            self.A -= decrease_by
        if self.D > Lo:
            probability_D = 1/(1+beta*(self.A-Lo))
        else:
            probability_D = 1
        # print(probability_D)
        if random.random() < probability_D:
            # do elongation
            elongate_by = self.elongate()
            self.D += elongate_by

        else:
            # do shortening
            decrease_by = int(random.uniform(50, 200))
            self.D -= decrease_by


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



