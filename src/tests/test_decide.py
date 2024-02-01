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

    def test_puv(self):
        # Test Case 1:
        # Input:
        # - PUV is all 1s
        # Expected behavior: PUV is equal to the expected PUV.
        expected_puv = [True for _ in range(15)]
        self.decide.load_puv_from_file('../data/puv_test_1.txt')
        self.assertTrue((self.decide.puv == expected_puv).all())

        # Test Case 2:
        # Input:
        # - PUV is all 0s
        # Expected behavior: PUV is equal to the expected PUV.
        expected_puv = [False for _ in range(15)]
        self.decide.load_puv_from_file('../data/puv_test_0.txt')
        self.assertTrue((self.decide.puv == expected_puv).all())

        # Test Case 3:
        # Input:
        # - PUV is not of length 15
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            self.decide.load_puv_from_file('../data/puv_test_17_inputs.txt')
        
        # Test Case 4:
        # Input:
        # - PUV has a wrong value (3)
        # Expected behavior: raises ValueError.
        with self.assertRaises(ValueError):
            self.decide.load_puv_from_file('../data/puv_test_none_01_char.txt')
        
        # Test Case 5:
        # Input:
        # - PUV validity test
        # Expected behavior: PUV is equal to the expected PUV.
        expected_puv = [True, True, False, False, True, True, True, False, True, True, False, True, False, True, True]
        self.decide.load_puv_from_file('../data/puv_test_valid.txt')
        self.assertTrue((self.decide.puv == expected_puv).all())

    def test_compute_pum_true(self):
        # Test Case 1:
        # Input:
        # - CMV and LCM is as in example from specification
        # - Expected PUM is as example from specification
        # Expected behavior: PUM is equal to the expected PUM.
        test_cmv = [False,True,True,True,False,False,True,False,True,False,True,False,True,False]
        self.decide.load_lcm_from_file('../data/lcm_example_1.txt')
        pum_array = [[True,False,True,False],
                        [False,True,True,True],
                        [True,True,True,True],
                        [False,True,True,True]]
        expected_pum = np.vstack([
            np.c_[pum_array, np.full((4, 11), True)], 
            np.full((11, 15), True)
        ])
        
        output_pum = self.decide.calc_pum(self.decide.lcm,test_cmv)

        self.assertTrue((output_pum == expected_pum).all())
        
    def test_compute_pum_false(self):
        # Test Case 1:
        # Input:
        # - CMV and LCM is as in example from specification
        # - Expected PUM has been changed to not be the same as from specification
        # Expected behavior: PUM is not equal to the expected PUM.
        test_cmv = [False,True,True,True,False,False,True,False,True,False,True,False,True,False]
        self.decide.load_lcm_from_file('../data/lcm_example_1.txt')
        pum_array = [[False,False,False,False],
                        [False,True,True,True],
                        [True,True,True,True],
                        [False,True,True,True]]
        expected_pum = np.vstack([
            np.c_[pum_array, np.full((4, 11), True)], 
            np.full((11, 15), True)
        ])
        
        output_pum = self.decide.calc_pum(self.decide.lcm,test_cmv)

        self.assertFalse((output_pum == expected_pum).all())

    def test_decide(self):
        # Test Case 1:
        # Input:
        # - Inputs are as in example 1 from specification
        # Expected behavior: LAUNCH signal is False.
        numpoints = 3
        points = np.array([
            [1, 1],
            [4, 1],
            [4, 5],
        ])
        parameters = {
            "LENGTH1": 1000,
            "RADIUS1": 0.1,
            "EPSILON": np.pi/4,
            "AREA1": 0.1,
            "Q_PTS": 3,
            "QUADS": 3,
            "DIST": 1000,
            "N_PTS": 3,
            "K_PTS": 1,
            "A_PTS": 1,
            "B_PTS": 1,
            "C_PTS": 1,
            "D_PTS": 1,
            "E_PTS": 1,
            "F_PTS": 1,
            "G_PTS": 4,
            "LENGTH2": 1,
            "RADIUS2": 1,
            "AREA2": 1
        }
        decide_instance = Decide(numpoints, points, parameters, None, self.decide.puv)
        decide_instance.load_lcm_from_file('../data/lcm_example_1.txt')
        # Making sure LICs are as in the example from specification
        # Only first 4 ones are used
        self.assertFalse(decide_instance.cmv.cmv[0])
        self.assertTrue(decide_instance.cmv.cmv[1])
        self.assertTrue(decide_instance.cmv.cmv[2])
        self.assertTrue(decide_instance.cmv.cmv[3])

        decide_instance.decide()

        self.assertFalse(decide_instance.launch)

        # Test Case 2:
        # Input:
        # - Inputs are as in example 1 from specification
        # - But we change LCM[0,1], LCM[0,3], LCM[1,0] and LCM[3,0] to ORR
        # Expected behavior: LAUNCH signal is True.
        decide_instance.lcm[0,1] = 'ORR'
        decide_instance.lcm[1,0] = 'ORR'
        decide_instance.lcm[0,3] = 'ORR'
        decide_instance.lcm[3,0] = 'ORR'

        decide_instance.decide()

        self.assertTrue(decide_instance.launch)

        # Test Case 3:
        # - LCM and PUV are such that only LICs 4, 7, 10, 13 matter
        # - They must all be True 
        numpoints = 5
        points = np.array([[-1,-1], [1,1], [-1,1], [1,-1], [2,2]])
        puv = np.array([False, False, False, False, True, False, False, True, False, False, True, False, False, True, False])
        parameters = {
            "LENGTH1": 0.5,
            "RADIUS1": 0.5,
            "EPSILON": 0.0,
            "AREA1": 0.1,
            "Q_PTS": 3,
            "QUADS": 2,
            "DIST": 10.0,
            "N_PTS": 3, 
            "K_PTS": 1,
            "A_PTS": 1,
            "B_PTS": 1,
            "C_PTS": 1,
            "D_PTS": 1,
            "E_PTS": 1,
            "F_PTS": 1,
            "G_PTS": 1,
            "LENGTH2": 10.0,
            "RADIUS2": 10.0,
            "AREA2": 10.0
        }
        decide_instance = Decide(numpoints, points, parameters, None, puv)
        decide_instance.load_lcm_from_file('../data/lcm_testcase_3.txt')

        # Making sure relevant LICs i.e. 4, 7, 10, 13 are True
        self.assertTrue(decide_instance.cmv.cmv[4])
        self.assertTrue(decide_instance.cmv.cmv[7])
        self.assertTrue(decide_instance.cmv.cmv[10])
        self.assertTrue(decide_instance.cmv.cmv[13])

        decide_instance.decide()
        self.assertTrue(decide_instance.launch)

if __name__ == '__main__':
    unittest.main()