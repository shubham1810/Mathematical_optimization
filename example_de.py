__author__ = 'Shubham Dokania'

import time

from src import differential_evolution as DE


if __name__ == '__main__':
    number_of_runs = 5
    val = 0
    print_time = True

    for i in xrange(number_of_runs):
        start = time.clock()
        de = DE.DifferentialEvolution(num_iterations=1000, dim=2, CR=0.4, F=0.48)
        val += de.simulate()
        if print_time:
            print(time.clock() - start)

    print("Final average of all runs: "), (val / number_of_runs)

