import unittest
import numpy as np
from main.cmv import Cmv
import copy

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
        self.num_points = 10
        self.points = rng.random((self.num_points,2))
        # Dont think these are needed
        #lcm = rng.random((15,15))
        #puv = rng.random((15))

        # Initialize Decide instance
        # I think this needs to be moved out for us to be able to modify the variables for test cases
        #self.cmv = Cmv(self.parameters, self.points, self.num_points)

    def test_lic7_k_pts_less_than_1(self):
    # Tests that num_points has to be more than 3 elements
        test_points = [
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (6.0, 5.0)
                    ]

        parameters_changed = copy.deepcopy(self.parameters)
        parameters_changed["K_PTS"] = 0.5

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        result = cmv_changed.lic7()
        self.assertFalse(result)

    def test_lic7_num_points_less_than_3(self):
    # Tests that num_points has to be more than 3 elements
        test_points = [
                        (1.0, 2.0),
                        (6.0, 5.0)
                    ]

        cmv_changed = Cmv(self.parameters, test_points, 2)
        result = cmv_changed.lic7()
        self.assertFalse(result)

    def test_lic7_distance_false(self):
    # Tests that if there is no distance greater than k_pts then the lic returns false
        test_points = [
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0)
                    ]
        parameters_changed = copy.deepcopy(self.parameters)
        parameters_changed["K_PTS"] = 3

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        print(str(cmv_changed.k_pts) + " kpts")
        result = cmv_changed.lic7()
        self.assertFalse(result)

    def test_lic7_distance_true(self):
    # Tests that if there is a distance >= lenght1 k_pts distance appart then lic is true
        test_points = [
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (1.0, 2.0),
                        (2.0, 2.0),
                        (2.0, 2.0),
                        (1.0, 2.0),
                        (6.0, 5.0)
                    ]
        parameters_changed = copy.deepcopy(self.parameters)
        parameters_changed["K_PTS"] = 2

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        print(str(cmv_changed.k_pts) + " kpts")
        result = cmv_changed.lic7()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()