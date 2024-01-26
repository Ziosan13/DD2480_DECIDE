import unittest
import numpy as np
from main.decide import Decide

class test_decide(unittest.TestCase):

    def setUp(self):
        # Create sample input for testing, replace if necessary
        rng = np.random.default_rng()
        numpoints = 10
        points = rng.random((numpoints,2))
        parameters = {'param1': 1, 'param2': 2}
        lcm = rng.random((15,15))
        puv = rng.random((15))

        # Initialize Decide instance
        self.decide = Decide(numpoints, points, parameters, lcm, puv)

    def test_initialization(self):
        # Used for testing if the initialization of Decide is correct
        self.assertEqual(self.decide.numpoints, 10)
        self.assertFalse(self.decide.launch)

if __name__ == '__main__':
    unittest.main()