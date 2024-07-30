import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from IK_solver import *
from DK_solver import *
from Quadrupedal_Model import Kinematic_Model

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d', proj_type = 'ortho')
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])
ax.set_xlabel('X axis - L')
ax.set_ylabel('Y axis - w')
ax.set_zlabel('Z axis')

QM = Kinematic_Model()
matrix_FL = QM.matrix_FL
matrix_BL = QM.matrix_BL
matrix_FR = QM.matrix_FR
matrix_BR = QM.matrix_BR

# Plot lines for body
lb01, = ax.plot([matrix_FL[0,3], matrix_BL[0,3]], [matrix_FL[1,3], matrix_BL[1,3]], [matrix_FL[2,3], matrix_BL[2,3]], color='k')
lb12, = ax.plot([matrix_BL[0,3], matrix_BR[0,3]], [matrix_BL[1,3], matrix_BR[1,3]], [matrix_BL[2,3], matrix_BR[2,3]], color='k')
lb23, = ax.plot([matrix_BR[0,3], matrix_FR[0,3]], [matrix_BR[1,3], matrix_FR[1,3]], [matrix_BR[2,3], matrix_FR[2,3]], color='k')
lb31, = ax.plot([matrix_FR[0,3], matrix_FL[0,3]], [matrix_FR[1,3], matrix_FL[1,3]], [matrix_FR[2,3], matrix_FL[2,3]], color='k')

# ================================================ INITIAL PLOT IN REST POSITION ================================================
# Initial lines for Front Left leg
x01FL, y01FL, z01FL, x12FL, y12FL, z12FL, x23FL, y23FL, z23FL = get_xyz(matrix_FL, only_last = False, rl = "l") 
line0, = ax.plot(x01FL, y01FL, z01FL, marker='o')
line1, = ax.plot(x12FL, y12FL, z12FL, marker='o')
line2, = ax.plot(x23FL, y23FL, z23FL, marker='o')

# Initial lines for Back Left leg
x01BL, y01BL, z01BL, x12BL, y12BL, z12BL, x23BL, y23BL, z23BL = get_xyz(matrix_BL, only_last = False, rl = "l")
line3, = ax.plot(x01BL, y01BL, z01BL, marker='o')
line4, = ax.plot(x12BL, y12BL, z12BL, marker='o')
line5, = ax.plot(x23BL, y23BL, z23BL, marker='o')

# Initial lines for Front Right leg
x01FR, y01FR, z01FR, x12FR, y12FR, z12FR, x23FR, y23FR, z23FR = get_xyz(matrix_FR, angles = [0, -np.pi/4, np.pi/2], only_last = False, rl = "r") 
line6, = ax.plot(x01FR, y01FR, z01FR, marker='o')
line7, = ax.plot(x12FR, y12FR, z12FR, marker='o')
line8, = ax.plot(x23FR, y23FR, z23FR, marker='o')

# Initial lines for Back Right leg
x01BR, y01BR, z01BR, x12BR, y12BR, z12BR, x23BR, y23BR, z23BR = get_xyz(matrix_BR, angles = [0, -np.pi/4, np.pi/2], only_last = False, rl = "r")
line9,  = ax.plot(x01BR, y01BR, z01BR, marker='o')
line10, = ax.plot(x12BR, y12BR, z12BR, marker='o')
line11, = ax.plot(x23BR, y23BR, z23BR, marker='o')

def update_line(X, Y, Z):
    # Front Left leg plot update
    angle0, angle1, angle2 = solve_L([X, Y, Z]) 
    x0, y0, z0, x1, y1, z1, x2, y2, z2 = get_xyz(matrix_FL, angles = [angle0, angle1,angle2], only_last = False, rl = "l")
    line0.set_data(x0, y0)
    line0.set_3d_properties(z0)
    line1.set_data(x1, y1)
    line1.set_3d_properties(z1)
    line2.set_data(x2, y2)
    line2.set_3d_properties(z2)
    
    # Back Left leg plot update
    angle3, angle4, angle5 = solve_L([X, Y, Z])
    x3, y3, z3, x4, y4, z4, x5, y5, z5 = get_xyz(matrix_BL, angles = [angle3, angle4, angle5], only_last = False, rl = "l")
    line3.set_data(x3, y3)
    line3.set_3d_properties(z3)
    line4.set_data(x4, y4)
    line4.set_3d_properties(z4)
    line5.set_data(x5, y5)
    line5.set_3d_properties(z5)
    
    # Front Right leg plot update
    angle6, angle7, angle8 = solve_R([X, Y, Z]) 
    x6, y6, z6, x7, y7, z7, x8, y8, z8 = get_xyz(matrix_FR, angles = [angle6, angle7, angle8], only_last = False, rl = "r")
    line6.set_data(x6, y6)
    line6.set_3d_properties(z6)
    line7.set_data(x7, y7)
    line7.set_3d_properties(z7)
    line8.set_data(x8, y8)
    line8.set_3d_properties(z8)
    
    # Back Right leg plot update
    angle9, angle10, angle11 = solve_R([X, Y, Z])
    x9, y9, z9, x10, y10, z10, x11, y11, z11 = get_xyz(matrix_BR, angles = [angle9, angle10, angle11], only_last = False, rl = "r")
    line9.set_data(x9, y9)
    line9.set_3d_properties(z9)
    line10.set_data(x10, y10)
    line10.set_3d_properties(z10)
    line11.set_data(x11, y11)
    line11.set_3d_properties(z11)

    fig.canvas.draw_idle()

def update(val):
    X = slider0.val
    Y = slider1.val
    Z = slider2.val 
    update_line(X, Y, Z)

# Sliders in plotting
slider_ax0 = fig.add_axes([0.1, 0.09, 0.3, 0.025])
slider0 = Slider(slider_ax0, 'X', -5., 5.0, valinit=0)
slider0.on_changed(update)

slider_ax1 = fig.add_axes([0.1, 0.06, 0.3, 0.025])
slider1 = Slider(slider_ax1, 'Y', -5.0, 5.0, valinit=0)
slider1.on_changed(update)

slider_ax2 = fig.add_axes([0.1, 0.03, 0.3, 0.025])
slider2 = Slider(slider_ax2, 'Z', -5.0, 5.0, valinit=0)
slider2.on_changed(update)

plt.show()