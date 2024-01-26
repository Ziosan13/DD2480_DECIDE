import unittest
import numpy as np
from main.cmv import Cmv

class test_cmv(unittest.TestCase):

    def setUp(self):
        # Create sample input for testing, replace if necessary
        parameters = {
            "LENGTH1": 2,
            "RADIUS1": 1,
            # add others as needed
            "AREA2": 5
        }
        rng = np.random.default_rng()
        numpoints = 10
        points = rng.random((numpoints,2))
        lcm = rng.random((15,15))
        puv = rng.random((15))

        # Initialize Decide instance
        self.cmv = Cmv(numpoints, points, parameters, lcm, puv)

if __name__ == '__main__':
    unittest.main()