__author__ = 'Shubham Dokania'

import collection
import point
import test_functions


def get_best_point(points):
    best = sorted(points, key=lambda x:x.z)[0]
    return best


if __name__ == '__main__':
    pass

