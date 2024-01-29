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

    def test_lic_0(self):
        params = self.parameters.copy()
        points = np.array([[1, 1],[1, 2],[3, 2]]) # odd number of points 
        num_points = points.shape[0]
        
        # Test Case 1:
        # Input: 
        # LENGTH1 is 0.0
        # The first pair of points are 1 unit apart, the second is 2 units apart 
        # Expect: LIC0 is true 
        params["LENGTH1"] = 0
        self.assertTrue(Cmv(params, points, num_points).lic0())

        # Test Case 2:
        # Input: 
        # LENGTH1 is 0.1
        # The first pair of points are 1 unit apart, the second is 2 units apart 
        # Expect: LIC0 is true 
        params["LENGTH1"] = 0.1
        self.assertTrue(Cmv(params, points, num_points).lic0())

        # Test Case 3:
        # Input: 
        # LENGTH1 is 1.5
        # The first pair of points are 1 unit apart, the second is 2 units apart 
        # Expect: LIC0 is true 
        params["LENGTH1"] = 1.5
        self.assertTrue(Cmv(params, points, num_points).lic0())

         # Test Case 4:
        # Input: 
        # LENGTH1 is 2
        # The first pair of points are 1 unit apart, the second is 2 units apart 
        # Expect: LIC0 is false 
        params["LENGTH1"] = 2
        self.assertFalse(Cmv(params, points, num_points).lic0())

        # Test Case 5:
        # Input: 
        # LENGTH1 is 3
        # The first pair of points are 1 unit apart, the second is 2 units apart 
        # Expect: LIC0 is false 
        params["LENGTH1"] = 3
        self.assertFalse(Cmv(params, points, num_points).lic0())


        points = np.array([[1, 1],[1, 3],[3, 3],[0,0]]) # even number of points
        num_points = points.shape[0]

         # Test Case 6:
        # Input: 
        # LENGTH1 is 1
        # The first pair of points are 2 units apart, the second is 1 unit apart, the third is 3.61 units apart  
        # Expect: LIC0 is true 
        params["LENGTH1"] = 1
        self.assertTrue(Cmv(params, points, num_points).lic0())

        # Test Case 7:
        # Input: 
        # LENGTH1 is 2
        # The first pair of points are 1 unit apart, the second is 2 units apart, the third is 3.61 units apart
        # Expect: LIC0 is true 
        params["LENGTH1"] = 2
        self.assertTrue(Cmv(params, points, num_points).lic0())

        # Test Case 8:
        # Input: 
        # LENGTH1 is 4
        # The first pair of points are 1 unit apart, the second is 2 units apart, the third is 3.61 units apart 
        # Expect: LIC0 is false 
        params["LENGTH1"] = 4
        self.assertTrue(Cmv(params, points, num_points).lic0())

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

if __name__ == '__main__':
    unittest.main()