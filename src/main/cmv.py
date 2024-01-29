import numpy as np
from functools import reduce

class Cmv:
    """
    CMV - Conditions Met Vector
    A class containing 15 methods, one for each LIC.
    Each method returns True if the LIC is satisfied, False otherwise.
    The result of each method is stored in a list: cmv.
    """

    def __init__(self, parameters, points, num_points) -> None:
        self.length1 = parameters["LENGTH1"]
        self.radius1 = parameters["RADIUS1"]
        self.epsilon = parameters["EPSILON"]
        self.area1 = parameters["AREA1"]
        self.q_pts = parameters["Q_PTS"]
        self.quads = parameters["QUADS"]
        self.dist = parameters["DIST"]
        self.n_pts = parameters["N_PTS"]
        self.k_pts = parameters["K_PTS"]
        self.a_pts = parameters["A_PTS"]
        self.b_pts = parameters["B_PTS"]
        self.c_pts = parameters["C_PTS"]
        self.d_pts = parameters["D_PTS"]
        self.e_pts = parameters["E_PTS"]
        self.f_pts = parameters["F_PTS"]
        self.g_pts = parameters["G_PTS"]
        self.length2 = parameters["LENGTH2"]
        self.radius2 = parameters["RADIUS2"]
        self.area2 = parameters["AREA2"]

        self.points = points
        self.num_points = num_points

        self.cmv = np.zeros(15, dtype="bool_")
        self.check_parameters()
        self.cmv_calc()

    def cmv_calc(self):
        self.cmv[0] = self.lic0()
        self.cmv[1] = self.lic1()
        self.cmv[2] = self.lic2()
        self.cmv[3] = self.lic3()
        self.cmv[4] = self.lic4()
        self.cmv[5] = self.lic5()
        self.cmv[6] = self.lic6()
        self.cmv[7] = self.lic7()
        self.cmv[8] = self.lic8()
        self.cmv[9] = self.lic9()
        self.cmv[10] = self.lic10()
        self.cmv[11] = self.lic11()
        self.cmv[12] = self.lic12()
        self.cmv[13] = self.lic13()
        self.cmv[14] = self.lic14()
        return self.cmv
    
    def check_parameters(self):
        """
        Checks that parameters are well-formed.
        Raises exceptions otherwise.
        """
        if (type(self.area1) is not float) and (type(self.area1) is not int):
            raise TypeError(
                'AREA1 parameter in parameters input must be a number.')
        if (self.area1 < 0):
            raise ValueError(
                'AREA1 parameter in parameters input must be positive.')
        if (type(self.radius1) is not float) and (type(self.radius1) is not int):
            raise TypeError(
                'RADIUS1 parameter in parameters input must be a number.')
        if (self.radius1 < 0):
            raise ValueError(
                'RADIUS1 parameter in parameters input must be positive.')
        if (type(self.a_pts) is not int) or (type(self.b_pts) is not int):
            raise TypeError('A_PTS and B_PTS parameters must be integers.')
        if (self.a_pts < 1 or self.b_pts < 1):
            raise ValueError('A_PTS and B_PTS must be greater than 1.')
        # we can add more checks as we make the LICs

    def lic0(self):
        pass

    def lic1(self):
        pass

    def lic2(self):
        pass

    def lic3(self):
        """
        This LIC is True if there exists at least one 
        set of three consecutive data points that are 
        the vertices of a triangle with area greater than AREA1. 

        Conditions on parameters: 
        - (0 <= AREA1)
        """
        for i in range(self.num_points - 2):
            delta = np.linalg.det(np.c_[self.points[i:(i+3)], np.ones((3, 1))])
            A = 0.5*np.abs(delta)
            if (A > self.area1):
                return True

        return False

    def lic4(self):
        pass

    def lic5(self):
        pass

    def lic6(self):
        pass

    def lic7(self):
        pass

    def lic8(self):
        """
        This LIC is True if there exists at least one 
        set of three data points separated by exactly A PTS and B PTS 
        consecutive intervening points, respectively, 
        that cannot be contained within or on a circle of radius RADIUS1. 
        The condition is not met when NUMPOINTS < 5.

        Conditions on parameters: 
        - (0 <= RADIUS1)
        - (1 <= A_PTS)
        - (1 <= B_PTS)
        - (A_PTS + B_PTS <= (NUMPOINTS - 3))
        """

        if self.num_points < 5:
            return False
        
        for i in range(self.num_points - (self.a_pts + self.b_pts) - 2):
            points_of_interest = np.array(
                [self.points[i], self.points[i + (self.a_pts + 1)], self.points[i + (self.a_pts + self.b_pts + 2)]])
            
            delta = np.linalg.det(np.c_[points_of_interest, np.ones((3, 1))])
            x_matrix = np.c_[np.array(
                [p[0]*p[0] + p[1]*p[1] for p in points_of_interest]), points_of_interest[:, 1], np.ones((3, 1))]
            y_matrix = np.c_[np.array(
                [p[0]*p[0] + p[1]*p[1] for p in points_of_interest]), points_of_interest[:, 0], np.ones((3, 1))]
            x_circumcenter = (1/(2*delta))*np.linalg.det(x_matrix)
            y_circumcenter = -(1/(2*delta))*np.linalg.det(y_matrix)
            circumcenter = np.array([x_circumcenter, y_circumcenter])
            if reduce(lambda acc, p: acc and (np.linalg.norm(p - circumcenter) > self.radius1), points_of_interest, np.linalg.norm(points_of_interest[0] - circumcenter) > self.radius1):
                return True

    def lic9(self):
        pass

    def lic10(self):
        pass

    def lic11(self):
        pass

    def lic12(self):
        pass

    def lic13(self):
        pass

    def lic14(self):
        pass
