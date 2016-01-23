__author__ = 'Shubham Dokania'

import copy
import random
import time

from helpers.collection import Collection
from helpers import get_best_point


class DifferentialEvolution(object):
    def __init__(self, num_iterations=10, CR=0.4, F=0.48, dim=2):
        random.seed()
        self.num_iterations = num_iterations
        self.iteration = 0
        self.CR = CR
        self.F = F
        self.population = Collection(dim=dim)

    def iterate(self):
        for ix in xrange(self.population.num_points):
            x = self.population.points[ix]
            [a, b, c] = random.sample(self.population.points, 3)
            while x == a or x == b or x == c:
                [a, b, c] = random.sample(self.population.points, 3)

            R = random.random() * x.dim
            y = copy.deepcopy(x)

            for iy in xrange(x.dim):
                ri = random.random()

                if ri < self.CR or iy == R:
                    y.coords[iy] = a.coords[iy] + self.F * (b.coords[iy] - c.coords[iy])

            y.evaluate_point()
            if y.z < x.z:
                self.population.points[ix] = y
        self.iteration += 1

    def simulate(self):
        pnt = get_best_point(self.population.points)
        print("Initial best value: " + str(pnt.z))
        while self.iteration < self.num_iterations:
            self.iterate()

        pnt = get_best_point(self.population.points)
        print("Final best value: " + str(pnt.z))
        return pnt.z


if __name__ == '__main__':
    number_of_runs = 5
    val = 0
    print_time = True

    for i in xrange(number_of_runs):
        start = time.clock()
        de = DifferentialEvolution(num_iterations=100, dim=2, CR=0.4, F=0.48)
        val += de.simulate()
        if print_time:
            print("")
            print(time.clock() - start)

    print("Final average of all runs: "), (val / number_of_runs)
