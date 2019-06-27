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
        self.M = 10
        self.Kr = 0.1
        self.status = {'normal': True,'single mutation': False, 'double mutation': False}

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

    def set_M(self, value):
        self.M = value

    def set_Kr(self, value):
        self.Kr = value

    def iter_decrease(self):
        rand_val_a = int(random.uniform(50, 200))
        rand_val_d = int(random.uniform(50, 200))
        self.A -= rand_val_a
        self.D -= rand_val_d
    def elongate_by(self):
        p = 0.005
        random_number = random.random()
        y = -math.log(1 - random_number) / p
        return y
    def elongate(self):

        probability = (2*self.M)/((1+self.M)*(1+math.sqrt(1+4*self.Kr*self.get_min()/1+self.M)))
        if random.random() <= probability:
            self.A += self.elongate_by()
            self.D += self.elongate_by()

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



