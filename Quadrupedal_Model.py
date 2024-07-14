import numpy as np
from FwO import trotz, transl, trotx

class Kinematic_Model:
    def __init__(self):
        self.angles_l = np.matrix([0,  np.pi/4, -np.pi/2])
        self.angles_r = np.matrix([0, -np.pi/4,  np.pi/2])
        
        self.L = 20
        self.W = 10
        
        self.l1 = 5
        self.l2 = 12.5
        self.l3 = 12.5
        
        self.matrix_FL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(self.W/2, 0, self.L/2)
        self.matrix_BL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(self.W/2, 0, -self.L/2)
        self.matrix_FR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0, self.L/2)
        self.matrix_BR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0, -self.L/2)
        
        
        
        
        