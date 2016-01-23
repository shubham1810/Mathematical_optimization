__author__ = 'Shubham Dokania'

import random
import time

from helpers.point import Point
from helpers.collection import Collection
from helpers import get_best_point


class SOMA(object):
    def __init__(self, path_length=2.0, step_length=0.2, perturbation=0.4, num_iterations=10, dim=2):
        random.seed()
        self.dim = dim
        self.pathLength = path_length
        self.step = step_length
        self.perturbation = perturbation
        self.numIterations = num_iterations
        self.iteration = 0
        self.population = Collection(dim=dim)

    def generate_perturbation(self):
        p_vector = []
        for nx in range(self.dim):
            rnd = random.random()
            if rnd < self.perturbation:
                p_vector.append(1)
            else:
                p_vector.append(0)

        return p_vector

    def get_leader(self):
        top_point = sorted(self.population.points, key=lambda x: x.z)[0]
        return top_point

    def iterate(self):
        leader = self.get_leader()
        # print(leader.z)

        for ix in range(len(self.population.points)):
            curr_point = self.population.points[ix]
            path_value = 0
            p_vec = self.generate_perturbation()
            new_points = []
            while path_value <= self.pathLength:
                new_point = Point(dim=self.dim)
                for dx in range(new_point.dim):
                    new_point.coords[dx] = curr_point.coords[dx] + (leader.coords[dx] - curr_point.coords[
                        dx]) * path_value * p_vec[dx]
                new_point.evaluate_point()
                new_points.append(new_point)
                path_value += self.step
            self.population.points[ix] = get_best_point(new_points)
        self.iteration += 1

    def simulate(self):
        pnt = get_best_point(self.population.points)
        # print('best value of: ' + str(pnt.z) + ' at ' + str(pnt.coords)
        print('Initial best value of: ' + str(pnt.z))
        while self.iteration < self.numIterations:
            self.iterate()
        pnt = get_best_point(self.population.points)
        # print('best value of: ' + str(pnt.z) + ' at ' + str(pnt.coords)
        print('Final best value of: ' + str(pnt.z))
        print("")
        return pnt.z


if __name__ == '__main__':
    number_of_runs = 1
    val = 0
    print_time = True

    for i in xrange(number_of_runs):
        start = time.clock()
        soma = SOMA(num_iterations=100, dim=2)
        val += soma.simulate()
        if print_time:
            print(time.clock() - start)

    print("Final average of all runs: "), (val / number_of_runs)
