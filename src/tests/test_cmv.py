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

    def test_lic_4(self) -> None:
        params = self.parameters.copy()

        # Test Case 1:
        # Input:
        # - Q_PTS is an int with value 4
        # - points are 4 verticies with 1 vertex in each quadrant
        # - QUADS is an int with value 3
        # Expected behavior: LIC 4 is True.
        params['Q_PTS'] = 4
        params['QUADS'] = 3
        points = np.array([
            [1, 1],
            [-1, 1],
            [-1, -1],
            [1, -1],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic4())

        # Test Case 2:
        # Input:
        # - Q_PTS is an int with value 4
        # - points are 4 verticies with 1 vertex in each quadrant,
        # but one vertex is the origin
        # - QUADS is an int with value 3
        # Expected behavior: LIC 4 is True.
        params['Q_PTS'] = 4
        params['QUADS'] = 3
        points = np.array([
            [0, 0],
            [-1, 1],
            [-1, -1],
            [1, -1],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic4())

        # Test Case 3:
        # Input:
        # - Q_PTS is an int with value 4
        # - points are 4 verticies all in quadrant 1
        # - QUADS is an int with value 3
        # Expected behavior: LIC 4 is False.
        params['Q_PTS'] = 4
        params['QUADS'] = 3
        points = np.array([
            [1, 1],
            [2, 1],
            [1, 2],
            [2, 2],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic4())

    def test_lic_5(self) -> None:
        params = self.parameters.copy()

        # Test Case 1:
        # Input:
        # - points are 2 verticies with x1 > x2
        # Expected behavior: LIC 5 is True.
        points = np.array([
            [2, 1],
            [1, 1],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic5())

        # Test Case 2:
        # Input:
        # - points are 2 verticies with x1 = x2
        # Expected behavior: LIC 5 is False.
        points = np.array([
            [1, 1],
            [1, 1],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic5())

        # Test Case 3:
        # Input:
        # - points are 2 verticies with x1 < x2
        # Expected behavior: LIC 5 is False.
        points = np.array([
            [1, 1],
            [2, 1],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic5())

        # Test Case 4:
        # Input:
        # - points are 5 verticies with x1 < x2 < x3 < x4 < x5
        # Expected behavior: LIC 5 is False.
        points = np.array([
            [1, 1],
            [2, 1],
            [3, 1],
            [4, 1],
            [5, 1],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic5())

        # Test Case 5:
        # Input:
        # - points are 5 verticies with x1 < x2 > x3 < x4 < x5
        # Expected behavior: LIC 5 is True.
        points = np.array([
            [1, 1],
            [2, 1],
            [1, 1],
            [3, 1],
            [4, 1],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic5())

    def test_lic_6(self) -> None:
        params = self.parameters.copy()

        # Test Case 1:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 1
        # - points are 3 verticies with distance between the line
        #   between the first and last vertex and the middle vertex
        #   equal to 2: (0,0), (2,2), (4,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is True.
        params['N_PTS'] = 3
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [2, 2],
            [4, 0],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic6())

        # Test Case 2:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 1
        # - points are 3 verticies with distance between the line
        #   between the first and last vertex and the middle vertex
        #   equal to 1: (0,0), (2,1), (4,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 3
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [2, 1],
            [4, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 3:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 2
        # - points are 3 verticies with distance between the line
        #   between the first and last vertex and the middle vertex
        #   equal to 1: (0,0), (2,1), (4,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 3
        params['DIST'] = 2
        points = np.array([
            [0, 0],
            [2, 1],
            [4, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 4:
        # Input:
        # - N_PTS is an int with value 5
        # - DIST is an int with value 1
        # - points are 5 verticies all on a straight line:
        #   (0,0), (1,0), (2,0), (3,0), (4,0).
        # - NUMPOINTS is an int with value 5
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 5
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 5:
        # Input:
        # - N_PTS is an int with value 5
        # - DIST is an int with value 1
        # - points are 5 verticies all on a straight line,
        #   except for the third vertex which is at a distance
        #   of 2 from the line between the first and last vertex:
        #   (0,0), (1,0), (2,2), (3,0), (4,0).
        # - NUMPOINTS is an int with value 5
        # Expected behavior: LIC 6 is True.
        params['N_PTS'] = 5
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [1, 0],
            [2, 2],
            [3, 0],
            [4, 0],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic6())

        # Test Case 6:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 1
        # - points are 3 verticies where p1 = p3:
        #   (0,0), (2,0), (0,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is True.
        params['N_PTS'] = 3
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [2, 0],
            [0, 0],
        ])
        num_points = points.shape[0]
        self.assertTrue(Cmv(params, points, num_points).lic6())

        # Test Case 7:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 1
        # - points are 3 verticies where p1 = p3:
        #   (0,0), (1,0), (0,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 3
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [1, 0],
            [0, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 8:
        # Input:
        # - N_PTS is an int with value 2
        # - DIST is an int with value 1
        # - points are 2 verticies: (0,0), (1,0).
        # - NUMPOINTS is an int with value 2
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 2
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [1, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 9:
        # Input:
        # - N_PTS is an int with value 4
        # - DIST is an int with value 1
        # - points are 3 verticies: (0,0), (1,0), (2,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 4
        params['DIST'] = 1
        points = np.array([
            [0, 0],
            [1, 0],
            [2, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())

        # Test Case 10:
        # Input:
        # - N_PTS is an int with value 3
        # - DIST is an int with value 0
        # - points are 3 verticies: (0,0), (1,0), (2,0).
        # - NUMPOINTS is an int with value 3
        # Expected behavior: LIC 6 is False.
        params['N_PTS'] = 3
        params['DIST'] = 0
        points = np.array([
            [0, 0],
            [1, 0],
            [2, 0],
        ])
        num_points = points.shape[0]
        self.assertFalse(Cmv(params, points, num_points).lic6())
        


if __name__ == '__main__':
    unittest.main()