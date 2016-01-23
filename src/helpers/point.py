__author__ = 'Shubham Dokania'

import copy

import numpy as np

from test_functions import evaluate


class Point:
    def __init__(self, dim=2, upper_limit=10, lower_limit=-10):
        self.dim = dim
        self.coords = [0] * dim
        self.z = 0
        self.range_upper_limit = upper_limit
        self.range_lower_limit = lower_limit

    def generate_random_point(self):
        co_od = []
        for _ in xrange(self.dim):
            co_od.append(np.random.uniform(self.range_lower_limit, self.range_upper_limit))

        self.coords = copy.deepcopy(co_od)
        self.z = evaluate(self.coords)

    def generate_neighbour(self):
        for ix in xrange(self.dim):
            offset = (2 * np.random.random() - 1.0) * 0.5
            self.coords[ix] += offset
            if self.coords[ix] < self.range_lower_limit:
                self.coords[ix] = self.range_lower_limit
            elif self.coords[ix] > self.range_upper_limit:
                self.coords[ix] = self.range_upper_limit

        self.z = evaluate(self.coords)

    def evaluate_point(self):
        self.z = evaluate(self.coords)


if __name__ == '__main__':
    print("Point class defined in this script")
