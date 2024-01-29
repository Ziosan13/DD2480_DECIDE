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

    def test_lic_2(self):
        params = self.parameters.copy()
        points = np.array([[1, 1],[0, 0],[0, 1]]) 
        num_points = points.shape[0]
        
        # Test Case 1:
        # Input: 
        # EPSILON is 0.0
        # The points form an angle = pi/4
        # Expect: LIC0 is true 
        params["EPSILON"] = 0
        self.assertTrue(Cmv(params, points, num_points).lic2())

        # Test Case 2:
        # Input: 
        # EPSILON is 5pi/6
        # The points form an angle = pi/4
        # Expect: LIC0 is false 
        params["EPSILON"] = 5*np.pi/6
        self.assertFalse(Cmv(params, points, num_points).lic2())

        points = np.array([[1, 0],[0, 0],[-1, 0]]) 
        num_points = points.shape[0]
        
        # Test Case 3:
        # Input: 
        # EPSILON is 0
        # The points form an angle = pi/2 
        # Expect: LIC0 is false 
        params["EPSILON"] = 0
        self.assertFalse(Cmv(params, points, num_points).lic2())

        points = np.array([[1, 0],[0, 0],[0, 1],[1,2]]) 
        num_points = points.shape[0]

        # Test Case 4:
        # Input: 
        # EPSILON is 0.1
        # The points form an angle = pi/2 and angle = 3pi/4
        # Expect: LIC0 is true 
        params["EPSILON"] = 0.1
        self.assertTrue(Cmv(params, points, num_points).lic2())

        # Test Case 5:
        # Input: 
        # EPSILON is 4pi/5
        # The points form an angle = pi/2 and angle = 3pi/4
        # Expect: LIC0 is false 
        params["EPSILON"] = 4*np.pi/5
        self.assertFalse(Cmv(params, points, num_points).lic2())

        # Test Case 6:
        # Input: 
        # EPSILON is 1.11
        # The points form an angle = pi/2 and angle = 3pi/4
        # Expect: LIC0 is true 
        params["EPSILON"] = 1.11
        self.assertTrue(Cmv(params, points, num_points).lic2())


if __name__ == '__main__':
    unittest.main()