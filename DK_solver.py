from Operators import trotz, transl, trotx
from QD import Quad_model
import numpy as np

QM = Quad_model()
# Direct Kinematics using transformation matrix for quadrupedal robot
def get_xyz(origin, m = [5,12.5,12,5], angles = [0, np.pi/4, -np.pi/2], rl = "r", only_last = True):
    coef = (1 if rl == "l" else -1)
    T01 = origin * trotz(angles[0]) * transl(0, 0, 0) * transl(coef*m[0], 0, 0) * trotx(0)
    T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2*coef)
    T23 = T12 * trotz(angles[1]) * transl(0, 0, 0) * transl(m[1], 0, 0) * trotx(0)
    T34 = T23 * trotz(angles[2]) * transl(0, 0, 0) * transl(m[2], 0, 0) * trotx(0)
    
    x0 = [origin[0,3], T12[0,3]]
    y0 = [origin[1,3], T12[1,3]]
    z0 = [origin[2,3], T12[2,3]]

    x1 = [T12[0,3], T23[0,3]]
    y1 = [T12[1,3], T23[1,3]]
    z1 = [T12[2,3], T23[2,3]]

    x2 = [T23[0,3], T34[0,3]]
    y2 = [T23[1,3], T34[1,3]]
    z2 = [T23[2,3], T34[2,3]]
    
    if only_last != True:
        return x0, y0, z0, x1, y1, z1, x2, y2, z2
    else:
        return x2[1], y2[1], z2[1]
