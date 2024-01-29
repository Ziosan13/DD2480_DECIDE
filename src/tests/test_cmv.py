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

    def test_lic_13(self) -> None:
        params = self.parameters.copy()

        points = np.array([
            [6, 5],
            [3, 6],
            [1, 1],
            [12, 10],
            [7, 5],
            [5, 6],
            [1, 5],
            [4, 8],
            [1, 3],
            [7, 4],
            [5, 5],
            [4, 1]]
        )

        same_points = np.array([
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5],
            [6, 5]]
        )

        colinear_points = np.array([
            [6, 5],
            [3, 6],
            [2.5, 3],
            [12, 10],
            [7, 5],
            [5, 6],
            [1, 5],
            [4, 8],
            [1, 3],
            [7, 4],
            [5, 5],
            [4, 1]]
        )

        num_points = points.shape[0]

        # Test Case 1:
        # Input:
        # - RADIUS1 is strictly less than 2.5
        # - RADIUS2 is strictly greater than 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 13 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.4
        params['RADIUS2'] = 2.6
        self.assertTrue(Cmv(params, points, num_points).lic13())

        # Test Case 2:
        # Input:
        # - RADIUS1 is strictly less than 2.5
        # - RADIUS2 is equal to 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 13 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.4
        params['RADIUS2'] = 2.5
        self.assertTrue(Cmv(params, points, num_points).lic13())

        # Test Case 3:
        # Input:
        # - RADIUS1 is strictly less than 2.5
        # - RADIUS2 is close to zero
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 13 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.4
        params['RADIUS2'] = 0.1
        self.assertFalse(Cmv(params, points, num_points).lic13())

        # Test Case 4:
        # Input:
        # - RADIUS1 is strictly greater than 2.5
        # - RADIUS2 is strictly greater than 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 13 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.6
        params['RADIUS2'] = 2.6
        self.assertFalse(Cmv(params, points, num_points).lic13())

        # Test Case 5:
        # Input:
        # - RADIUS1 is greater than 0.0
        # - RADIUS2 is greater than 0.0
        # - points have the same coordinates
        # Expected behavior: LIC 13 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 0.1
        params['RADIUS2'] = 0.1
        self.assertFalse(Cmv(params, same_points, num_points).lic13())

        # Test Case 6:
        # Input:
        # - RADIUS1 is strictly less than 5.0
        # - RADIUS2 is strictly greater than 5.0
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 13 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 4.9
        params['RADIUS2'] = 5.1
        self.assertTrue(Cmv(params, colinear_points, num_points).lic13())

        # Test Case 7:
        # Input:
        # - RADIUS1 is strictly less than 5.0
        # - RADIUS2 is equal to 5.0
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 13 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 4.9
        params['RADIUS2'] = 5.0
        self.assertTrue(Cmv(params, colinear_points, num_points).lic13())

        # Test Case 8:
        # Input:
        # - RADIUS1 is strictly less than 5.0
        # - RADIUS2 is strictly less than 5.0
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 13 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 4.9
        params['RADIUS2'] = 0.1
        self.assertFalse(Cmv(params, colinear_points, num_points).lic13())

        # Test Case 9:
        # Input:
        # - RADIUS1 is strictly greater than 5.0
        # - RADIUS2 is strictly greater than 5.0
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 13 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 5.1
        params['RADIUS2'] = 5.1
        self.assertFalse(Cmv(params, colinear_points, num_points).lic13())

if __name__ == '__main__':
    unittest.main()