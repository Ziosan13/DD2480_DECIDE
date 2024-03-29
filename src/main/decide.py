import numpy as np
from main.cmv import Cmv

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

    def __init__(self, numpoints: int, points: np.ndarray, parameters: dict, lcm, puv) -> None:
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
        self.cmv = Cmv(parameters, points, numpoints)
        self.pum = np.zeros((15, 15))
        self.fuv = np.zeros(15, dtype="bool_")
        self.launch = False

    def load_lcm_from_file(self, file_path : str) -> None:
        """
        Generates an LCM matrix from a txt file 
        and assigns it to the current instance.
        The txt file must contain 15x15 values
        among 0 (for NOTUSED), 1 (for ORR) 
        and 2 (for ANDD). The matrix must 
        be symmetric (LCM == LCM.T).

        Parameters
        ----------
        file_path: str
            path to the txt file
        """
        lcm = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            row = []
            for char in line:
                if (char != '\n'):
                    match int(char):
                        case 0:
                            row.append('NOTUSED')
                        case 1:
                            row.append('ORR')
                        case 2:
                            row.append('ANDD')
                        case _:
                            raise ValueError("Wrong value in provided file.")
                        
            lcm.append(row)

        lcm = np.array(lcm)
        if (lcm.shape != (15, 15)):
            raise ValueError('Wrong shape for LCM matrix. Check the provided file.')
        if not (lcm == lcm.T).all():
            raise ValueError('LCM matrix is not symmetric. Check the provided file.')
        
        self.lcm = lcm

    def load_puv_from_file(self, file_path : str) -> list:
        """
        Generates a PUV vector from a txt file 
        and assigns it to the current instance.
        The txt file must contain 15 values
        among 0 (for FALSE) and 1 (for TRUE).

        Parameters
        ----------
        file_path: str
            path to the txt file
        """
        puv = []
        with open(file_path, 'r') as file:
            line = file.readline()

        for char in line:
            if (char != '\n'):
                match int(char):
                    case 0:
                        puv.append(False)
                    case 1:
                        puv.append(True)
                    case _:
                        raise ValueError("Wrong value in provided file.")
                        
        puv = np.array(puv)
        if (puv.shape != (15,)):
            raise ValueError('Wrong shape for PUV vector. Check the provided file.')
        
        self.puv = puv
        return puv

    def calc_pum(self,lcm,cmv):
        """
        Calculates the PUM Matrix from a LCM matrix and CMV array 

        Parameters
        ----------
        lcm: array
            Logical Connector Matrix
        cmv: array
            Conditions Met Vector

        Returns
        -------
        pum: array
            Preliminary Unlocking Matrix 
        """
        pum = np.empty((15, 15), dtype=bool)

        for i in range(len(lcm)):
            for j in range(len(lcm)):
                if(i == j):
                    pum[i][j] = True
                    continue
                match lcm[i][j]:
                    case 'NOTUSED':
                        pum[i][j] = True
                    case 'ANDD':
                        pum[i][j] = cmv[i] and cmv[j]
                    case 'ORR':
                        pum[i][j] = cmv[i] or cmv[j]
                    case _:
                        raise ValueError("Wrong value in LCM.")
                pum[j][i] = pum[i][j]
        return pum

    def compute_fuv(self):
        for i in range(15):
            if self.puv[i] == False: # If puv[i] is false, fuv[i] is always true
                self.fuv[i] = True
            
            else:   # else we check if
                falseFound = False

                for j in range(15): 
                    if i != j and self.pum[i][j] == False:
                        falseFound = True

                if not falseFound:
                    self.fuv[i] = True
        
        return self.fuv


    def decide(self) -> None:
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

        # compute PUM
        self.pum = self.calc_pum(self.lcm, self.cmv.cmv)

        # compute FUV
        self.compute_fuv()

        # compute LAUNCH
        self.launch = np.all(self.fuv)

        print("YES" if self.launch else "NO")
