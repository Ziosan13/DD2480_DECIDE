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

    def lic0(self):
        pass

    def lic1(self):
        pass

    def lic2(self):
        for i in range(self.num_points-2):
            x_i = self.points[i][0]
            x_i_plus_one = self.points[i+1][0]
            x_i_plus_two = self.points[i+2][0]
            y_i = self.points[i][1]
            y_i_plus_one = self.points[i+1][1]
            y_i_plus_two = self.points[i+2][1]

            BA = [x_i-x_i_plus_one,y_i-y_i_plus_one]
            BC = [x_i_plus_two-x_i_plus_one,y_i_plus_two-y_i_plus_one]

            angle = np.arccos(np.dot(BA,BC)/(np.linalg(BA)*(np.linalg(BC))))

            if angle < np.pi - self.epsilon:
                return True
            
            elif angle > np.pi + self.epsilon:
                return True
        
        return False

            
 

    def lic3(self):
        pass

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
