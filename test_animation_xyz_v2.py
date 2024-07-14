import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from FwO import trotz, transl, trotx
from IK_resolver import *
from Quad_def import xyz_FL
from Quadrupedal_Model import Kinematic_Model

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

KM = Kinematic_Model()


matrix_FL = KM.matrix_FL
x01, y01, z01, x12, y12, z12, x23, y23, z23 = xyz_FL(matrix_FL)
x_ = x23[1]
y_ = y23[1]
z_ = z23[1]
print(z_)
line0, = ax.plot(x01, y01, z01, marker='o')
line1, = ax.plot(x12, y12, z12, marker='o')
line2, = ax.plot(x23, y23, z23, marker='o')

matrix_BL = KM.matrix_BL
x01BL, y01BL, z01BL, x12BL, y12BL, z12BL, x23BL, y23BL, z23BL = xyz_FL(matrix_BL)

line3, = ax.plot(x01BL, y01BL, z01BL, marker='o')
line4, = ax.plot(x12BL, y12BL, z12BL, marker='o')
line5, = ax.plot(x23BL, y23BL, z23BL, marker='o')

def update_line(X, Y, Z):
    global z_, matrix_FL, matrix_BL
    angle0, angle1, angle2 = solve_L([X, Y, Z + z_]) # change 5 with l1 and -17.67 with z_
    x0, y0, z0, x1, y1, z1, x2, y2, z2 = xyz_FL(matrix_FL, [angle0, angle1,angle2])

    line0.set_data(x0, y0)
    line0.set_3d_properties(z0)
    line1.set_data(x1, y1)
    line1.set_3d_properties(z1)
    line2.set_data(x2, y2)
    line2.set_3d_properties(z2)
    #fig.canvas.draw_idle()
        
    angle0, angle1, angle2 = solve_L([X, Y, Z + z_]) # change 5 with l1 and -17.67 with z_
    x01BL, y01BL, z01BL, x12BL, y12BL, z12BL, x23BL, y23BL, z23BL = xyz_FL(matrix_BL, [angle0, angle1,angle2])

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