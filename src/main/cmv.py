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
        for i in range(len(self.points)-1):
            x_i = self.points[i][0]
            x_i_plus_one = self.points[i+1][0]
            y_i = self.points[i][1]
            y_i_plus_one = self.points[i+1][1]
            
            distance = np.sqrt((x_i-x_i_plus_one)**2+(y_i-y_i_plus_one)**2)

            if distance > self.length1:
                return True
        
        return False

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

            angle = np.arccos(np.dot(BA,BC)/(np.linalg.norm(BA)*(np.linalg.norm(BC))))

            if angle < np.pi - self.epsilon:
                return True
            
            elif angle > np.pi + self.epsilon:
                return True
        
        return False

            
 

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
        """
        There exists at least one set of three data points separated 
        by exactly C PTS and D PTS consecutive intervening points, 
        respectively, that form an angle such that:

        angle < (PI − EPSILON) or angle > (PI + EPSILON)

        The second point of the set of three points is always the vertex of the angle.
        If either of the other points coincide with the vertex, the angle is disregarded.

        Conditions on parameters: 
        1≤C PTS,1≤D PTS
        C PTS+D PTS ≤ NUMPOINTS−3
        """
        lic_passed = False

        if (self.c_pts > 0 and self.d_pts > 0 and self.num_points >= 5):

            for i in range (self.num_points - (self.c_pts + self.d_pts + 2)):
                p1 = self.points[i]
                p2 = self.points[i + self.c_pts +1]
                p3 = self.points[i + self.c_pts + self.d_pts +2]

                if ((p2[0] == p1[0] and p2[1] == p1[1]) or (p2[0] == p3[0] and p2[1] == p3[1])):
                    continue

                vector1 = p2 - p1
                vector2 = p2 - p3
                dot_product = np.dot(vector1,vector2)
                norm1 = np.linalg.norm(vector1)
                norm2 = np.linalg.norm(vector2)

                angle = np.arccos(dot_product/(norm1 * norm2))

                if(angle < (np.pi - self.epsilon) or angle > (np.pi + self.epsilon)):
                    lic_passed = True
                
        return lic_passed
                    
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
