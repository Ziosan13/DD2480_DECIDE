import unittest
import numpy as np
from main.cmv import Cmv

class test_cmv(unittest.TestCase):

    def setUp(self):
        # Create sample input for testing, replace if necessary
        self.parameters = {
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
        self.cmv = Cmv(self.parameters, points, num_points)

    def test_lic_1(self):
        params = self.parameters.copy()
        points = np.array([[1, 1],[3, 1],[2, 1.5]]) 
        num_points = points.shape[0]

        # Test Case 1:
        # Input: 
        # RADIUS1 is 0.1
        # The points form a circle with radius r = sqrt(0.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 0.1
        self.assertTrue(Cmv(params, points, num_points).lic1())

        # Test Case 2:
        # Input: 
        # RADIUS1 is 1
        # The points form a circle with radius r = sqrt(0.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 1
        self.assertFalse(Cmv(params, points, num_points).lic1())

        # Test Case 3:
        # Input: 
        # RADIUS1 is 5
        # The points form a circle with radius r = sqrt(0.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 5
        self.assertFalse(Cmv(params, points, num_points).lic1())

        points = np.array([[1, 1],[3, 1],[2, 1.5],[4,4]]) 
        num_points = points.shape[0]

        # Test Case 4:
        # Input: 
        # RADIUS1 is 0.1
        # The points form a circle with radius r = sqrt(0.5) and one with r=sqrt(6.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 0.1
        self.assertTrue(Cmv(params, points, num_points).lic1())

        # Test Case 5:
        # Input: 
        # RADIUS1 is 1
        # The points form a circle with radius r = sqrt(0.5) and one with r=sqrt(6.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 1
        self.assertTrue(Cmv(params, points, num_points).lic1())

        # Test Case 5:
        # Input: 
        # RADIUS1 is 2
        # The points form a circle with radius r = sqrt(0.5) and one with r=sqrt(6.5)
        # Expect: LIC0 is true 
        params["RADIUS1"] = 2
        self.assertFalse(Cmv(params, points, num_points).lic1())


if __name__ == '__main__':
    unittest.main()