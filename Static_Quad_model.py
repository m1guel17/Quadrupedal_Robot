from Plot import *
from Operators import trotz, transl, trotx
import numpy as np
from Quadrupedal_Model import Kinematic_Model

KM = Kinematic_Model()
L = KM.L
W = KM.W
l1 = KM.l1_
l2 = KM.l2_
l3 = KM.l3_

origin = np.array([np.matrix(np.eye(4))])
origin_ = np.array([np.matrix(np.eye(4))* trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)])

# Body dimentions
FRS = KM.matrix_FR
FLS = KM.matrix_FL
BRS = KM.matrix_BR
BLS = KM.matrix_BL
body = np.array([FRS, BRS, BLS, FLS])

# Front_Left Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(W/2, 0, L/2)
T01 = matrix * trotz(0) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
T23 = T12 * trotz(np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
FL = np.array([matrix, T01, T12, T23, T34])

# Front_Right Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-W/2, 0, L/2)
T01 = matrix * trotz(0) * transl(0, 0, 0) * transl(-l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)
T23 = T12 * trotz(-np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
FR = np.array([matrix, T01, T12, T23, T34])

# Back_Right Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-W/2, 0, -L/2)
T01 = matrix * trotz(0) * transl(0, 0, 0) * transl(-l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)
T23 = T12 * trotz(-np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
BR = np.array([matrix, T01, T12, T23, T34])

# Back_Left Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(W/2, 0, -L/2)
T01 = matrix * trotz(0) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
T23 = T12 * trotz(np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)

# Array the body 
BL = np.array([matrix, T01, T12, T23, T34])

graph_body(body)
graph([origin_], 4)
graph([FL,BR,FR,BL], show_fw=True)