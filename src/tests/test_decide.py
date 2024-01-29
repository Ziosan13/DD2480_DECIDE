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
        puv = rng.random((15))

        # Initialize Decide instance
        self.decide = Decide(numpoints, points, self.parameters, lcm, puv)

    def test_initialization(self):
        # Used for testing if the initialization of Decide is correct
        self.assertEqual(self.decide.numpoints, 10)
        self.assertFalse(self.decide.launch)

    def test_load_lcm_from_file(self):
        self.decide.load_lcm_from_file('../data/lcm_example_1.txt')

        base_array = np.array([
            ["ANDD", "ANDD", "ORR", "ANDD"],
            ["ANDD", "ANDD", "ORR", "ORR"],
            ["ORR", "ORR", "ANDD", "ANDD"],
            ["ANDD", "ORR", "ANDD", "ANDD"],
        ])
        expected_lcm_1 = np.vstack([np.c_[base_array, np.full((4, 11), "NOTUSED")], np.full((11, 15), "NOTUSED")])
        self.assertTrue((self.decide.lcm == expected_lcm_1).all())

        self.decide.load_lcm_from_file('../data/lcm_example_2.txt')
        expected_lcm_2 = np.vstack([
            np.c_[base_array, np.full((4, 10), "NOTUSED"), np.full((4, 1), "ORR")], 
            np.c_[np.full((10, 14), "NOTUSED"), np.full((10, 1), "ORR")], 
            np.full((1, 15), "ORR")
        ])
        self.assertTrue((self.decide.lcm == expected_lcm_2).all())

        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_not_symmetric.txt')

        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_wrong_shape.txt')

        with self.assertRaises(ValueError):
            self.decide.load_lcm_from_file('../data/lcm_test_wrong_value.txt')


if __name__ == '__main__':
    unittest.main()