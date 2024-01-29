import numpy as np


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
        # we can add more checks as we make the LICs

    def lic0(self):
        pass

    def lic1(self):
        for i in range(self.num_points-2):
            x_i = self.points[i][0]
            x_i_plus_one = self.points[i+1][0]
            x_i_plus_two = self.points[i+2][0]
            y_i = self.points[i][1]
            y_i_plus_one = self.points[i+1][1]
            y_i_plus_two = self.points[i+2][1]
            
            AB = [x_i_plus_one-x_i,y_i_plus_one-y_i]
            BC = [x_i_plus_two-x_i_plus_one,y_i_plus_two-y_i_plus_one]
            CA = [x_i-x_i_plus_two,y_i-y_i_plus_two]
            
            # Two cases: 

            # Case 1: Longest side is diameter

            # Checks which side is the longest, and which points span the longest side
            if np.linalg.norm(AB) > np.linalg.norm(BC) and np.linalg.norm(AB) > np.linalg.norm(CA):
                longest_side = AB
                other_point = [x_i_plus_two,y_i_plus_two]
                midpoint = [x_i,y_i]+[1/2*AB[0],1/2*AB[1]]

            elif np.linalg.norm(BC) > np.linalg.norm(AB) and np.linalg.norm(BC) > np.linalg.norm(CA):
                longest_side = BC
                other_point = [x_i,y_i]
                midpoint = [x_i_plus_one,y_i_plus_one]+[1/2*BC[0],1/2*BC[1]]


            elif np.linalg.norm(CA) > np.linalg.norm(BC) and np.linalg.norm(CA) > np.linalg.norm(AB):
                longest_side = CA
                other_point = [x_i_plus_one,y_i_plus_one]
                midpoint = [x_i_plus_two,y_i_plus_two]+[[1/2*CA[0],1/2*CA[1]]]

            # Checks if the point not on the diameter is in the circle
            if ((other_point[0]-midpoint[0])**2  + (other_point[1]-midpoint[1])**2 < np.linalg.norm(longest_side)**2):
                r = np.linalg.norm(longest_side)/2 # computes radius as half of the longest side in triangel

            # Case 2: All points are on circle, radius is given by the triangel spanning the circle
            else:
                area = 1/2 * np.linalg.norm(np.cross(AB,BC)+np.cross(BC,CA)+np.cross(CA,AB))
                r = (np.linalg.norm(AB)*np.linalg.norm(BC)*np.linalg.norm(CA))/(4*area)

            if r > self.radius1:
                return True

        return False

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
        pass

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
