import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from IK_resolver import *
from DK_solver import xyz_left
from Quadrupedal_Model import Kinematic_Model

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

KM = Kinematic_Model()
matrix_FL = KM.matrix_FL
matrix_BL = KM.matrix_BL

# Initial lines for Front Left leg
x01FL, y01FL, z01FL, x12FL, y12FL, z12FL, x23FL, y23FL, z23FL = xyz_left(matrix_FL, last = False) 
line0, = ax.plot(x01FL, y01FL, z01FL, marker='o')
line1, = ax.plot(x12FL, y12FL, z12FL, marker='o')
line2, = ax.plot(x23FL, y23FL, z23FL, marker='o')

# Initial lines for Back Left leg
x01BL, y01BL, z01BL, x12BL, y12BL, z12BL, x23BL, y23BL, z23BL = xyz_left(matrix_BL, last = False)
line3, = ax.plot(x01BL, y01BL, z01BL, marker='o')
line4, = ax.plot(x12BL, y12BL, z12BL, marker='o')
line5, = ax.plot(x23BL, y23BL, z23BL, marker='o')



def update_line(X, Y, Z):
    angle0, angle1, angle2 = solve_L([X, Y, Z]) 
    x0, y0, z0, x1, y1, z1, x2, y2, z2 = xyz_left(matrix_FL, angles = [angle0, angle1,angle2], last = False)

    line0.set_data(x0, y0)
    line0.set_3d_properties(z0)
    line1.set_data(x1, y1)
    line1.set_3d_properties(z1)
    line2.set_data(x2, y2)
    line2.set_3d_properties(z2)
        
    angle0, angle1, angle2 = solve_L([X, Y, Z])
    x01BL, y01BL, z01BL, x12BL, y12BL, z12BL, x23BL, y23BL, z23BL = xyz_left(matrix_BL, angles = [angle0, angle1,angle2], last = False)

    line3.set_data(x01BL, y01BL)
    line3.set_3d_properties(z01BL)
    line4.set_data(x12BL, y12BL)
    line4.set_3d_properties(z12BL)
    line5.set_data(x23BL, y23BL)
    line5.set_3d_properties(z23BL)
    

    fig.canvas.draw_idle()

def update(val):
    X = slider0.val
    Y = slider1.val
    Z = slider2.val 
    update_line(X, Y, Z)




ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

slider_ax0 = fig.add_axes([0.2, 0.15, 0.65, 0.03])
slider0 = Slider(slider_ax0, 'X', -5., 5.0, valinit=0)
slider0.on_changed(update)

slider_ax1 = fig.add_axes([0.2, 0.1, 0.65, 0.03])
slider1 = Slider(slider_ax1, 'Y', -5.0, 5.0, valinit=0)
slider1.on_changed(update)

slider_ax2 = fig.add_axes([0.2, 0.05, 0.65, 0.03])
slider2 = Slider(slider_ax2, 'Z', -5.0, 5.0, valinit=0)
slider2.on_changed(update)

plt.show()