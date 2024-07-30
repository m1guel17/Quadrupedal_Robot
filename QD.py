from Operators import *
import numpy as np

# Quadruped Dimensions
class Quad_model:
    def __init__(self):
        self.angles_l = np.array([0,  np.pi/4, -np.pi/2])
        self.angles_r = np.array([0, -np.pi/4,  np.pi/2])
        
        self.L = 20
        self.W = 10
        
        self.l1 = 5
        self.l2 = 12.5
        self.l3 = 12.5
        
        origin = np.array([np.matrix(np.eye(4))]) * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)
        T01 = origin * trotz(self.angles_l[0]) * transl(0, 0, 0) * transl(self.l1, 0, 0) * trotx(0)
        T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
        T23 = T12 * trotz(self.angles_l[1]) * transl(0, 0, 0) * transl(self.l2, 0, 0) * trotx(0)
        T34 = T23 * trotz(self.angles_l[2]) * transl(0, 0, 0) * transl(self.l3, 0, 0) * trotx(0)
        
        self.start_height = T34[2,3]
        