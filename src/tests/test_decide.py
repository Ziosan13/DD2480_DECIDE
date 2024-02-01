import unittest
import numpy as np
from main.decide import Decide

class test_decide(unittest.TestCase):

    def setUp(self):
        # Create sample input for testing, replace if necessary
        rng = np.random.default_rng()
        numpoints = 10
        points = rng.random((numpoints,2))
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
        lcm = rng.random((15,15))
        #puv = rng.random((15))
        
        #puv from example
        puv = [True,False,True,False,True,False,True,False,True,False,True,False,True,False,True]

        # Initialize Decide instance
        self.decide = Decide(numpoints, points, self.parameters, lcm, puv)

    def test_initialization(self):
        # Used for testing if the initialization of Decide is correct
        self.assertEqual(self.decide.numpoints, 10)
        self.assertFalse(self.decide.launch)

    def test_load_lcm_from_file(self):
        base_array = np.array([
            ["ANDD", "ANDD", "ORR", "ANDD"],
            ["ANDD", "ANDD", "ORR", "ORR"],
            ["ORR", "ORR", "ANDD", "ANDD"],
            ["ANDD", "ORR", "ANDD", "ANDD"],
        ])

        # Test Case 1:
        # Input:
        # - LCM example 1 from specification.
        # - Corresponding LCM created with NumPy
        # Expected behavior: equality is True.
        self.decide.load_lcm_from_file('../data/lcm_example_1.txt')
        expected_lcm = np.vstack([
            np.c_[base_array, np.full((4, 11), "NOTUSED")], 
            np.full((11, 15), "NOTUSED")
        ])
        self.assertTrue((self.decide.lcm == expected_lcm).all())

        # Test Case 2:
        # Input:
        # - LCM example 1 from specification.
        # - Not corresponding LCM created with NumPy
        # Expected behavior: equality is True.
        not_expected_lcm = np.vstack([
            np.c_[base_array, np.full((4, 10), "NOTUSED"), np.full((4, 1), "ORR")], 
            np.c_[np.full((10, 14), "NOTUSED"), np.full((10, 1), "ORR")], 
            np.full((1, 15), "ORR")
        ])
        self.assertFalse((self.decide.lcm ==  not_expected_lcm).all())

        # Test Case 3:
        # Input:
        # - Not symmetric LCM in file.
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_not_symmetric.txt')

        # Test Case 4:
        # Input:
        # - LCM of wrong shape in file.
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_wrong_shape.txt')

        # Test Case 5:
        # Input:
        # - LCM in file has a wrong value (3)
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_wrong_value.txt')

    def test_compute_fuv(self):

        # Example pum-matrix
        self.decide.pum = [['*',False,True,False,True,False,True,False,True,False,True,False,True,False,True],
                           [False,'*',True,True,True,True,True,True,True,True,True,True,True,True,True],
                           [True,True,'*',True,True,True,True,True,True,True,True,True,True,True,True],
                           [False,True,True,'*',True,True,True,True,True,True,True,True,True,True,True],
                           [True,True,True,True,'*',True,True,True,True,True,True,True,True,True,True],
                           [False,True,True,True,True,'*',True,True,True,True,True,True,True,True,True],
                           [True,True,True,True,True,True,'*',True,True,True,True,True,True,True,True],
                           [False,True,True,True,True,True,True,'*',True,True,True,True,True,True,True],
                           [True,True,True,True,True,True,True,True,'*',True,True,True,True,True,True],
                           [False,True,True,True,True,True,True,True,True,'*',True,True,True,True,True],
                           [True,True,True,True,True,True,True,True,True,True,'*',True,True,True,True],
                           [False,True,True,True,True,True,True,True,True,True,True,'*',True,True,True],
                           [True,True,True,True,True,True,True,True,True,True,True,True,'*',True,True],
                           [False,True,True,True,True,True,True,True,True,True,True,True,True,'*',True],
                           [True,True,True,True,True,True,True,True,True,True,True,True,True,True,'*']]

        # The expected fuv for the puv and pum given
        expected_fuv = [False,True,True,True,True,True,True,True,True,True,True,True,True,True,True]        

        # Test Case 1:
        # Input:
        # - PUM and PUV is as in example from specification
        # - Expected FUV is computed from these
        # Expected behavior: FUV is equal to the expected FUV.
        self.assertTrue((self.decide.compute_fuv() == expected_fuv).all())

        # Another fuv, that is not the expected one
        not_expected_fuv = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]        

        # Test Case 2:
         # Input:
        # - PUM and PUV is as in example from specification
        # - A FUV that is not the expected one is constructed 
        # Expected behavior: comuted FUV not is equal to the not_expected FUV.
        self.assertFalse((self.decide.compute_fuv() == not_expected_fuv).all())


if __name__ == '__main__':
    unittest.main()