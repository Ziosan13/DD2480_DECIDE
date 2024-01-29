import unittest
import numpy as np
from main.cmv import Cmv

class test_cmv(unittest.TestCase):

    def setUp(self):
        # Create sample input for testing, replace if necessary
        parameters = {
            "LENGTH1": 2,
            "RADIUS1": 1,
            "EPSILON": 0.1,
            "AREA1": 1,
            "Q_PTS": 1,
            "QUADS": 1,
            "DIST": 1,
            "N_PTS": 1,
            "K_PTS": 1,
            "A_PTS": 1,
            "B_PTS": 1,
            "C_PTS": 1,
            "D_PTS": 1,
            "E_PTS": 1,
            "F_PTS": 1,
            "G_PTS": 1,
            "LENGTH2": 1,
            "RADIUS2": 1,
            "AREA2": 1
        }
        rng = np.random.default_rng()
        num_points = 10
        points = rng.random((num_points,2))
        # Dont think these are needed
        #lcm = rng.random((15,15))
        #puv = rng.random((15))

        # Initialize Decide instance
        self.cmv = Cmv(parameters, points, num_points)

if __name__ == '__main__':
    unittest.main()