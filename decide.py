import numpy as np


class Decide:
    """
    A class to compute the decide function, which decides
    if a missile should be launched.

    Attributes
    ----------
    numpoints: int
        the number of planar data points
    points: np.ndarray
        array containing the coordinates of data points
    parameters: dict
        dictionary holding parameters for LIC's
    lcm: np.ndarray
        logical connector matrix
    puv: np.ndarray
        preliminary unlocking vector
    cmv: np.ndarray
        conditions met vector
    pum: np.ndarray
        preliminary unlocking matrix
    fuv: np.ndarray
        final unlocking vector
    launch: bool
        final launch / no launch decision

    Methods
    -------
    decide():
        generates a boolean signal which determines
        whether an interceptor should be launched based
        on input radar tracking information.
    """

    def __init__(self, numpoints, points, parameters, lcm, puv) -> None:
        """
        Assigns given inputs to corresponding attributes 
        and initializes the outputs to their correct data type.

        Parameters
        ----------
        numpoints: int
            the number of planar data points
        points: np.ndarray
            array containing the coordinates of data points
        parameters: dict
            dictionary holding parameters for LIC's
        lcm: np.ndarray
            logical connector matrix
        puv: np.ndarray
            preliminary unlocking vector
        """

        # Inputs
        self.numpoints = numpoints
        self.points = points
        self.parameters = parameters
        self.lcm = lcm
        self.puv = puv

        # Outputs initialization
        self.cmv = np.zeros(15, dtype="bool_")
        self.pum = np.zeros((15, 15))
        self.fuv = np.zeros(15, dtype="bool_")
        self.launch = False

    def decide(self):
        """
        Prints a boolean signal to the 
        standard output using all class attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # compute LICs

        # compute PUM

        # compute FUV

        # compute LAUNCH

        print("YES" if self.launch else "NO")
