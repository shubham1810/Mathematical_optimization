__author__ = 'Shubham Dokania'

import copy
# import numpy as np

from point import Point


class Collection:
    def __init__(self, dim=2, num_points=10, upper_limit=10, lower_limit=-10):
        self.points = []
        self.num_points = num_points
        for ix in xrange(num_points):
            new_point = Point(dim=dim, upper_limit=upper_limit,
                              lower_limit=lower_limit)
            new_point.generate_random_point()
            self.points.append(copy.deepcopy(new_point))

    def generate_neighbour_collection(self):
        neighbour = copy.deepcopy(self)

        for ix in xrange(self.num_points):
            neighbour.points[ix].generate_neighbour()

        return neighbour


if __name__ == '__main__':
    print("Collection classes defined in this script")
