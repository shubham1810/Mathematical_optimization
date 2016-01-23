__author__ = 'Shubham Dokania'

import numpy as np


def evaluate(point):
    test = Function()
    return test.sphere(point)


class Function:
    def __init__(self):
        pass

    def sphere(self, x):
        z = 0
        for i in xrange(len(x)):
            z += x[i] ** 2
        return z

    def ackley(self, x):
        z1, z2 = 0, 0

        for i in xrange(len(x)):
            z1 += x[i] ** 2
            z2 += np.cos(2.0 * np.pi * x[i])

        return (-20.0 * np.exp(-0.2 * np.sqrt(z1 / len(x)))) - np.exp(z2 / len(x)) + np.e + 20.0


if __name__ == '__main__':
    print("A collection of several Test functions for optimizations")
