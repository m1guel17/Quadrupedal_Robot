from FwO import trotz, transl, trotx
import numpy as np
from Quadrupedal_Model import Kinematic_Model

KM = Kinematic_Model()

l1 = KM.l1
l2 = KM.l2
l3 = KM.l3

#matrix_FL = KM.matrix_FL

def xyz_FL(origin, angles = [0, np.pi/4, -np.pi/2]):
    
    T01 = origin * trotz(angles[0]) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
    T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
    T23 = T12 * trotz(angles[1]) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
    T34 = T23 * trotz(angles[2]) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
    #return matrix, T12, T23, T34
    
    x0 = [origin[0,3], T12[0,3]]
    y0 = [origin[1,3], T12[1,3]]
    z0 = [origin[2,3], T12[2,3]]

    x1 = [T12[0,3], T23[0,3]]
    y1 = [T12[1,3], T23[1,3]]
    z1 = [T12[2,3], T23[2,3]]

    x2 = [T23[0,3], T34[0,3]]
    y2 = [T23[1,3], T34[1,3]]
    z2 = [T23[2,3], T34[2,3]]
    
    return x0, y0, z0, x1, y1, z1, x2, y2, z2









