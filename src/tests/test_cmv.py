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

    def test_lic_8(self) -> None:
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

        combined_points = np.array([
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

        num_points = points.shape[0]

        # Test Case 1:
        # Input:
        # - RADIUS1 is strictly greater than 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.6
        self.assertFalse(Cmv(params, points, num_points).lic8())

        # Test Case 2:
        # Input:
        # - RADIUS1 is equal to 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.5
        self.assertFalse(Cmv(params, points, num_points).lic8())

        # Test Case 3:
        # Input:
        # - RADIUS1 is strictly less than 2.5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 8 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.4
        self.assertTrue(Cmv(params, points, num_points).lic8())

        # Test Case 4:
        # Input:
        # - NUMPOINTS is strictly less than 5
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 1
        params['B_PTS'] = 1
        params['RADIUS1'] = 0.0
        self.assertFalse(Cmv(params, np.array([[1, 1]]), 1).lic8())

        # Test Case 5:
        # Input:
        # - RADIUS1 is greater than 0.0
        # - points have the same coordinates
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 0.1
        self.assertFalse(Cmv(params, combined_points, num_points).lic8())

        # Test Case 6:
        # Input:
        # - RADIUS1 is equal to 0.0
        # - points have the same coordinates
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 0.0
        self.assertFalse(Cmv(params, combined_points, num_points).lic8())

        # Test Case 7:
        # Input:
        # - RADIUS1 is strictly less than 2.5
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 8 is True.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.4
        self.assertTrue(Cmv(params, colinear_points, num_points).lic8())

        # Test Case 8:
        # Input:
        # - RADIUS1 is equal to 2.5
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.5
        self.assertFalse(Cmv(params, colinear_points, num_points).lic8())

        # Test Case 9:
        # Input:
        # - RADIUS1 is strictly greater than 2.5
        # - points at indices 2, 6, 11
        #   are colinear and the maximum
        #   distance between them is 5.0
        # Expected behavior: LIC 8 is False.
        params['A_PTS'] = 3
        params['B_PTS'] = 4
        params['RADIUS1'] = 2.6
        self.assertFalse(Cmv(params, colinear_points, num_points).lic8())

        # Test Case 10:
        # Input:
        # - A_PTS is negative
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['A_PTS'] = -1
            params['B_PTS'] = 1
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

        # Test Case 11:
        # Input:
        # - B_PTS is negative
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['A_PTS'] = 1
            params['B_PTS'] = -1
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

        # Test Case 12:
        # Input:
        # - RADIUS1 is negative
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['A_PTS'] = 1
            params['B_PTS'] = 1
            params['RADIUS1'] = -1.0
            Cmv(params, points, num_points).lic8()

        # Test Case 13:
        # Input:
        # - A_PTS is a float
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises TypeError.
        with self.assertRaises(TypeError):
            params['A_PTS'] = 1.0
            params['B_PTS'] = 1
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

        # Test Case 14:
        # Input:
        # - B_PTS is a float
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises TypeError.
        with self.assertRaises(TypeError):
            params['A_PTS'] = 1
            params['B_PTS'] = 1.0
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

        # Test Case 15:
        # Input:
        # - RADIUS1 is not a number
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises TypeError.
        with self.assertRaises(TypeError):
            params['A_PTS'] = 1
            params['B_PTS'] = 1
            params['RADIUS1'] = "hi"
            Cmv(params, points, num_points).lic8()

        # Test Case 16:
        # Input:
        # - A_PTS is strictly less than 1
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['A_PTS'] = 0
            params['B_PTS'] = 1
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

        # Test Case 17:
        # Input:
        # - B_PTS is strictly less than 1
        # - points at indices 2, 6, 11
        #   form a 3-4-5 triangle that is contained
        #   in a circle of radius 2.5
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            params['A_PTS'] = 1
            params['B_PTS'] = 0
            params['RADIUS1'] = 0.0
            Cmv(params, points, num_points).lic8()

    #Tests if LIC9 returns true when angle falls within range < (PI - epsilon) or > (pI + epsilon)
    def test_lic9_true(self):
        test_points = np.array([
                        [5.0, 2.0],
                        [8.0, 6.0],
                        [3.0, -2.0],
                        [2.0, 2.0],
                        [1.0,3.0],
                        [1.0, 2.0],
                        [2.0, 2.0],
                        [2.0,1.0],
                        [1.0, 2.0],
                        [5.0,2.0]
                    ])

        parameters_changed = self.parameters.copy()
        parameters_changed["C_PTS"] = 2

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        result = cmv_changed.lic9()
        self.assertTrue(result)

    #Tests that LIC 9 returns false if there is no angle that falls within the range < (PI - epsilon) or > (PI + epsilon)
    def test_lic9_false_epsilon_not_met(self):
        test_points = np.array([
                        [1.0, 0.0],
                        [2.0, 6.0],
                        [3.0, 3.0],
                        [6.0, 4.0],
                        [5.0,0.0],
                        [2.0, -2.0]
                    ])

        parameters_changed = self.parameters.copy()
        parameters_changed["EPSILON"] = np.pi - 1

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        result = cmv_changed.lic9()
        self.assertFalse(result)

    #Tests that points that coincide with the vertex are not used to calculate the LIC
    def test_lic9_false_all_points_coincide(self):
        test_points = np.array([
                        [1.0, 0.0],
                        [2.0, 6.0],
                        [1.0, 0.0],
                        [6.0, 4.0],
                        [1.0, 0.0],
                    ])

        parameters_changed = self.parameters.copy()
        parameters_changed["EPSILON"] = np.pi - 1

        cmv_changed = Cmv(parameters_changed, test_points, len(test_points))
        result = cmv_changed.lic9()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()