import numpy as np
import math
from functools import reduce
from math import isclose

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
        if (type(self.radius2) is not float) and (type(self.radius1) is not int):
            raise TypeError(
                'RADIUS2 parameter in parameters input must be a number.')
        if (self.radius2 < 0):
            raise ValueError(
                'RADIUS2 parameter in parameters input must be positive.')
        if (type(self.a_pts) is not int) or (type(self.b_pts) is not int):
            raise TypeError('A_PTS and B_PTS parameters must be integers.')
        if (self.a_pts < 1 or self.b_pts < 1):
            raise ValueError('A_PTS and B_PTS must be greater than 1.')
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
        """
        This LIC is True if there exists at least one set of
        Q_PTS consecutive data points that lie in more than
        QUADS quadrants. QUADS: [1,3], Q_PTS: [2, NUMPOINTS]
        """
        for i in range(self.num_points):
            if i + self.q_pts > self.num_points:
                break
            points = self.points[i:i+self.q_pts]
            quadrants = [False for _ in range(4)]
            for point in points:
                if point[0] >= 0 and point[1] >= 0:
                    quadrants[0] = True
                elif point[0] <= 0 and point[1] >= 0:
                    quadrants[1] = True
                elif point[0] <= 0 and point[1] <= 0:
                    quadrants[2] = True
                elif point[0] >= 0 and point[1] <= 0:
                    quadrants[3] = True
            quads = 0
            for q in quadrants:
                if q:
                    quads += 1
            if quads > self.quads:
                return True
        return False
            

    def lic5(self):
        """
        This LIC is True if there exists at least one set of
        two consecutive data points, (X[i], Y[i]) and (X[j], Y[j]),
        such that X[j] - X[i] < 0. 
        """
        for i in range(self.num_points - 1):
            if self.points[i+1][0] - self.points[i][0] < 0:
                return True
        return False

    def lic6(self):
        """
        This LIC is True if there exists at least one set of
        N_PTS consecutive data points such that at least one of
        the points lies a distance greater than DIST from the
        line joining the first and last of these N_PTS points.
        If the first point = last point, then the distance
        is calculated as the distance between this point
        and the other points respectively.
        
        If NUMPOINTS < 3 or 3 <= N_PTS <= NUMPOINTS or DIST <= 0,
        the LIC is false.
        """
        if self.num_points < 3 or self.n_pts < 3 or self.n_pts > self.num_points or self.dist <= 0:
            return False
        for i in range(self.num_points - self.n_pts + 1):
            if np.linalg.norm(self.points[i] - self.points[i+self.n_pts-1]) == 0:
                for j in range(i+1, i+self.n_pts-1):
                    if np.linalg.norm(self.points[j] - self.points[i]) > self.dist:
                        return True
            else:
                for j in range(i+1, i+self.n_pts-1):
                    if np.linalg.norm(np.cross(self.points[i+self.n_pts-1] - self.points[i], self.points[j] - self.points[i])) / np.linalg.norm(self.points[i+self.n_pts-1] - self.points[i]) > self.dist:
                        return True


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
            
            # Colinear points
            if isclose(np.linalg.det(np.vstack([points_of_interest.T, np.ones((1, 3))])), 0, abs_tol=1e-9):
                norms = np.array([[np.linalg.norm(points_of_interest[i] - points_of_interest[j])
                                    for i in range(points_of_interest.shape[0])] for j in range(points_of_interest.shape[0])])
                if np.max(norms) > 2*self.radius1:
                    return True
                else:
                    continue
            
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
            
        return False

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
        """
        This LIC is True if exists at least one set of 
        three data points separated by exactly E PTS and 
        F PTS consecutive intervening points, respectively, 
        that are the vertices of a triangle with area greater than AREA1. 
        """
        if self.num_points < 5 or self.e_pts < 1 or self.f_pts < 1 or (self.e_pts + self.f_pts + 2) > self.num_points:
            return False
        
        else:
            for i in range (self.num_points - (self.c_pts + self.d_pts + 2)):
                p1 = self.points[i + self.c_pts +1]-self.points[i]
                p2 = self.points[i + self.c_pts + self.d_pts +2]-self.points[i]
                area=math.abs(p1[0]*p2[1]-p1[1]*p2[0])/2
                if area>self.area1:
                    return True
            return False
                


    def lic11(self):
        pass

    def lic12(self):
        pass

    def lic13(self):
        """
        This LIC is True if there exists at least one
        set of three data points, separated by exactly A PTS and B PTS
        consecutive intervening points, respectively,
        that cannot be contained within or on a circle of radius RADIUS1. 
        In addition, there exists at least one set of three data points 
        (which can be the same or different from the three data points just mentioned)
        separated by exactly A PTS and B PTS consecutive intervening points, 
        respectively, that can be contained in or on a circle of radius RADIUS2. 
        Both parts must be true for the LIC to be true. 
        The condition is not met when NUMPOINTS < 5.

        Conditions on parameters: 
        - (0 <= RADIUS1)
        - (0 <= RADIUS2)
        - (1 <= A_PTS)
        - (1 <= B_PTS)
        - (A_PTS + B_PTS <= (NUMPOINTS - 3))
        """

        if self.num_points < 5:
            return False
        
        conditions = np.zeros(2, dtype='bool_')

        for i in range(self.num_points - (self.a_pts + self.b_pts) - 2):
            points_of_interest = np.array(
                [self.points[i], self.points[i + (self.a_pts + 1)], self.points[i + (self.a_pts + self.b_pts + 2)]])

            # Colinear points
            if isclose(np.linalg.det(np.vstack([points_of_interest.T, np.ones((1, 3))])), 0, abs_tol=1e-9):
                norms = np.array([[np.linalg.norm(points_of_interest[i] - points_of_interest[j])
                                 for i in range(points_of_interest.shape[0])] for j in range(points_of_interest.shape[0])])
                if np.max(norms) > self.radius1:
                    conditions[0] = True
                if not (np.max(norms) > self.radius2):
                    conditions[1] = True
                continue

            delta = np.linalg.det(np.c_[points_of_interest, np.ones((3, 1))])
            x_matrix = np.c_[np.array(
                [p[0]*p[0] + p[1]*p[1] for p in points_of_interest]), points_of_interest[:, 1], np.ones((3, 1))]
            y_matrix = np.c_[np.array(
                [p[0]*p[0] + p[1]*p[1] for p in points_of_interest]), points_of_interest[:, 0], np.ones((3, 1))]
            x_circumcenter = (1/(2*delta))*np.linalg.det(x_matrix)
            y_circumcenter = -(1/(2*delta))*np.linalg.det(y_matrix)
            circumcenter = np.array([x_circumcenter, y_circumcenter])
            if reduce(lambda acc, p: acc and (np.linalg.norm(p - circumcenter) > self.radius1), points_of_interest, np.linalg.norm(points_of_interest[0] - circumcenter) > self.radius1):
                conditions[0] = True
            if not reduce(lambda acc, p: acc and (np.linalg.norm(p - circumcenter) > self.radius2), points_of_interest, np.linalg.norm(points_of_interest[0] - circumcenter) > self.radius2):
                conditions[1] = True

        return np.all(conditions)

    def lic14(self):
        pass
