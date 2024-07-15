from FwO import trotz, transl, trotx
from DK_solver import xyz_left
from QD import Quad_model
import numpy as np

QM = Quad_model()

# Robot Kinematic model
class Kinematic_Model:
    def __init__(self):
        self.angles_l = np.matrix([0,  np.pi/4, -np.pi/2])
        self.angles_r = np.matrix([0, -np.pi/4,  np.pi/2])
        
        self.L = QM.L
        self.W = QM.W
        
        self.l1_ = QM.l1
        self.l2_ = QM.l2
        self.l3_ = QM.l3
        
        # Origins for each leg 
        self.matrix_FL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(self.W/2, 0, self.L/2)
        self.matrix_BL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(self.W/2, 0, -self.L/2)
        self.matrix_FR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0, self.L/2)
        self.matrix_BR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0, -self.L/2)
        
        #Fw4 position - Front Left leg
        self.x4fl_, self.y4fl_, self.z4fl_ = xyz_left(self.matrix_FL, m = [self.l1_, self.l2_, self.l3_])
        #Fw4 position - Back Left leg
        self.x4bl_, self.y4bl_, self.z4bl_ = xyz_left(self.matrix_BL, m = [self.l1_, self.l2_, self.l3_])
        
