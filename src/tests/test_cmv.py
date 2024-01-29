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
        #self.cmv = Cmv(self.self.parameters, self.points, self.num_points)

    def test_lic_3(self) -> None:
        params = self.parameters.copy()

        points = np.array([
            [1, 1],
            [1, 5],
            [4, 1],
        ])

        colinear_points = np.array([
            [2.5, 3],
            [1, 5],
            [4, 1],
        ])

        same_points = np.array([
            [1, 1],
            [1, 1],
            [1, 1],
        ])

        num_points = points.shape[0]

        # Test Case 1:
        # Input:
        # - AREA1 is a float with value strictly less than 6.0
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is True.
        params['AREA1'] = 5.9
        self.assertTrue(Cmv(params, points, num_points).lic3())

        # Test Case 2:
        # Input:
        # - AREA1 is a float with value equal to 6.0
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 6.0
        self.assertFalse(Cmv(params, points, num_points).lic3())

        # Test Case 3:
        # Input:
        # - AREA1 is a float with value strictly greater than 6
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 6.1
        self.assertFalse(Cmv(params, points, num_points).lic3())

        # Test Case 4:
        # Input:
        # - AREA1 is an int with value strictly less than 6
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is True.
        params['AREA1'] = 5
        self.assertTrue(Cmv(params, points, num_points).lic3())

        # Test Case 5:
        # Input:
        # - AREA1 is an int with value equal to 6
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 6
        self.assertFalse(Cmv(params, points, num_points).lic3())

        # Test Case 6:
        # Input:
        # - AREA1 is an int with value strictly greater than 6
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 7
        self.assertFalse(Cmv(params, points, num_points).lic3())

        # Test Case 7:
        # Input:
        # - AREA1 is a float with value equal to 0.0
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: LIC 3 is True.
        params['AREA1'] = 0.0
        self.assertTrue(Cmv(params, points, num_points).lic3())

        # Test Case 8:
        # Input:
        # - AREA1 is a float with value strictly less than 6.0
        # - points form a 3-4-5 triangle of area equal to 6.0
        #   and their coordinates are negative
        # Expected behavior: LIC 3 is True.
        params['AREA1'] = 5.9
        self.assertTrue(Cmv(params, -points, num_points).lic3())

        # Test Case 9:
        # Input:
        # - AREA1 is a float with value equal to 6.0
        # - points form a 3-4-5 triangle of area equal to 6.0
        #   and their coordinates are negative
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 6.0
        self.assertFalse(Cmv(params, -points, num_points).lic3())

        # Test Case 10:
        # Input:
        # - AREA1 is a float with value strictly greater than 6
        # - points form a 3-4-5 triangle of area equal to 6.0
        #   and their coordinates are negative
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 6.1
        self.assertFalse(Cmv(params, -points, num_points).lic3())

        # Test Case 11:
        # Input:
        # - AREA1 is a float with value strictly greater than 0.0
        # - points are colinear
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 1.0
        self.assertFalse(Cmv(params, colinear_points, num_points).lic3())

        # Test Case 12:
        # Input:
        # - AREA1 is a float with value strictly greater than 0.0
        # - points are the same
        # Expected behavior: LIC 3 is False.
        params['AREA1'] = 1.0
        self.assertFalse(Cmv(params, same_points, num_points).lic3())

        # Test Case 13:
        # Input:
        # - AREA1 is negative
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['AREA1'] = -1.0
            Cmv(params, points, num_points).lic3()

        # Test Case 14:
        # Input:
        # - AREA1 is not a number
        # - points form a 3-4-5 triangle of area equal to 6.0
        # Expected behavior: raises TypeError.
        with self.assertRaises(TypeError):
            params['AREA1'] = "hi"
            Cmv(params, points, num_points).lic3()

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