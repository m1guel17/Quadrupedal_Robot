from Plot import *
from FwO import trotz, transl, trotx
import numpy as np

L = 20
W = 10

l1 = 5
l2 = 12.5
l3 = 12.5

origin = np.array([np.matrix(np.eye(4))])
origin_ = np.array([np.matrix(np.eye(4))* trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)])

# Body dimentions
FRS = origin * transl(L/2, -W/2, 0)
FLS = origin * transl(L/2, W/2, 0)
BRS = origin * transl(-L/2,-W/2, 0)
BLS = origin * transl(-L/2, W/2, 0)
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
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
T23 = T12 * trotz(np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
FR = np.array([matrix, T01, T12, T23, T34])

# Back_Right Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(-W/2, 0, -L/2)
T01 = matrix * trotz(0) * transl(0, 0, 0) * transl(-l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
T23 = T12 * trotz(np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
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
graph([FL,BR,FR,BL])#, show_fw=True)