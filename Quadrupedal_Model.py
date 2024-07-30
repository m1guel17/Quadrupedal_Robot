from Operators import trotz, transl, trotx
from DK_solver import get_xyz
from QD import Quad_model
import numpy as np

QM = Quad_model()

# Robot Kinematic model
class Kinematic_Model:
    def __init__(self):        
        self.L = QM.L
        self.W = QM.W
        
        self.l1_ = QM.l1
        self.l2_ = QM.l2
        self.l3_ = QM.l3
        
        # Origins for each leg 
        self.matrix_FL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl( self.W/2, 0,  self.L/2)
        self.matrix_BL = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl( self.W/2, 0, -self.L/2)
        self.matrix_FR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0,  self.L/2)
        self.matrix_BR = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-self.W/2, 0, -self.L/2)
        
        #Fw4 position - Front Left leg
        self.x4fl_, self.y4fl_, self.z4fl_ = get_xyz(self.matrix_FL, angles = QM.angles_l, m = [self.l1_, self.l2_, self.l3_], rl = "l")
        #Fw4 position - Back Left leg
        self.x4bl_, self.y4bl_, self.z4bl_ = get_xyz(self.matrix_BL, angles = QM.angles_l, m = [self.l1_, self.l2_, self.l3_], rl = "l")
        #Fw4 position - Front Right leg
        self.x4fr_, self.y4fr_, self.z4fr_ = get_xyz(self.matrix_FR, angles = QM.angles_r, m = [self.l1_, self.l2_, self.l3_], rl = "l")
        #Fw4 position - Back Right leg
        self.x4br_, self.y4br_, self.z4br_ = get_xyz(self.matrix_BR, angles = QM.angles_r, m = [self.l1_, self.l2_, self.l3_], rl = "l")
        
