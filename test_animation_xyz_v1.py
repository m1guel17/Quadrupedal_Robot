import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from FwO import trotz, transl, trotx
from IK_resolver import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

L = 20
W = 10

l1 = 5
l2 = 12.5
l3 = 12.5


# Front_Left Leg ===================================================================
origin = np.array([np.matrix(np.eye(4))])
origin_ = np.array([np.matrix(np.eye(4))* trotz(90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(90)])
initial_angle = 0

matrix = origin * trotz(90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(90) * transl(W/2, 0, L/2)
T01 = matrix * trotz(initial_angle) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-90)
T23 = T12 * trotz(45) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-90) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)

x0 = [matrix[0,3], T01[0,3]]
y0 = [matrix[1,3], T01[1,3]]
z0 = [matrix[2,3], T01[2,3]]

x1 = [T12[0,3], T23[0,3]]
y1 = [T12[1,3], T23[1,3]]
z1 = [T12[2,3], T23[2,3]]

x2 = [T23[0,3], T34[0,3]]
y2 = [T23[1,3], T34[1,3]]
z2 = [T23[2,3], T34[2,3]]

# Plot the initial line
line0, = ax.plot(x0, y0, z0, marker='o')
line1, = ax.plot(x1, y1, z1, marker='o')
line2, = ax.plot(x2, y2, z2, marker='o')




# Back_Left Leg ===================================================================
origin = np.array([np.matrix(np.eye(4))])
origin_ = np.array([np.matrix(np.eye(4))* trotz(90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(90)])
initial_angle = 0

matrix2 = origin * trotz(90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(90) * transl(W/2, 0, -L/2)
T01 = matrix2 * trotz(initial_angle) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-90)
T23 = T12 * trotz(45) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-90) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)

x3 = [matrix2[0,3], T01[0,3]]
y3 = [matrix2[1,3], T01[1,3]]
z3 = [matrix2[2,3], T01[2,3]]

x4 = [T12[0,3], T23[0,3]]
y4 = [T12[1,3], T23[1,3]]
z4 = [T12[2,3], T23[2,3]]

x5 = [T23[0,3], T34[0,3]]
y5 = [T23[1,3], T34[1,3]]
z5 = [T23[2,3], T34[2,3]]

# Plot the initial line
line3, = ax.plot(x3, y3, z3, marker='o')
line4, = ax.plot(x4, y4, z4, marker='o')
line5, = ax.plot(x5, y5, z5, marker='o')



# Function to update the line
def update_line(X, Y, Z, X2, Y2, Z2):
    
    angle, angle2, angle3 = solve_L([10+X,10+Y,-17.67+Z], l1, l2, l3) # 10 / 10 / - 17.67 final position of feet
    
    angle = angle*180/np.pi
    angle2 = angle2*180/np.pi
    angle3 = angle3*180/np.pi
    
    T01 = matrix * trotz(angle) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
    T12 = T01 * trotz(-90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-90)
    T23 = T12 * trotz(angle2) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
    T34 = T23 * trotz(angle3) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
        
    x0 = [matrix[0,3], T01[0,3]]
    y0 = [matrix[1,3], T01[1,3]]
    z0 = [matrix[2,3], T01[2,3]]
    line0.set_data(x0, y0)
    line0.set_3d_properties(z0)
    
    x1 = [T12[0,3], T23[0,3]]
    y1 = [T12[1,3], T23[1,3]]
    z1 = [T12[2,3], T23[2,3]]
    line1.set_data(x1, y1)
    line1.set_3d_properties(z1)
    
    x2 = [T23[0,3], T34[0,3]]
    y2 = [T23[1,3], T34[1,3]]
    z2 = [T23[2,3], T34[2,3]]
    line2.set_data(x2, y2)
    line2.set_3d_properties(z2)
    
    
    
    angle4, angle5, angle6 = solve_L([-10+X2,10+Y2,-17.67+Z2], l1, l2, l3) # 10 / 10 / - 17.67 final position of feet
    
    angle4 = angle4*180/np.pi
    angle5 = angle5*180/np.pi
    angle6 = angle6*180/np.pi
    
    T01 = matrix2 * trotz(angle4) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
    T12 = T01 * trotz(-90) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-90)
    T23 = T12 * trotz(angle5) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
    T34 = T23 * trotz(angle6) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
    
    x3 = [matrix2[0,3], T01[0,3]]
    y3 = [matrix2[1,3], T01[1,3]]
    z3 = [matrix2[2,3], T01[2,3]]
    line3.set_data(x3, y3)
    line3.set_3d_properties(z3)
    
    x4 = [T12[0,3], T23[0,3]]
    y4 = [T12[1,3], T23[1,3]]
    z4 = [T12[2,3], T23[2,3]]
    line4.set_data(x4, y4)
    line4.set_3d_properties(z4)
    
    x5 = [T23[0,3], T34[0,3]]
    y5 = [T23[1,3], T34[1,3]]
    z5 = [T23[2,3], T34[2,3]]
    line5.set_data(x5, y5)
    line5.set_3d_properties(z5)
    
    
    
    fig.canvas.draw_idle()

# Function to update the plot based on slider input
def update(val):
    X = slider0.val - 10
    Y = slider1.val - 5 
    Z = slider2.val 
    
    X2 = slider0.val + 10
    Y2 = slider1.val - 5 
    Z2 = slider2.val 
    
    update_line(X, Y, Z, X2, Y2, Z2)


# Adding a xyz sliders

slider_ax0 = fig.add_axes([0.2, 0.15, 0.65, 0.03])
slider0 = Slider(slider_ax0, 'X', -5., 5.0, valinit=0)
slider0.on_changed(update)

slider_ax1 = fig.add_axes([0.2, 0.1, 0.65, 0.03])
slider1 = Slider(slider_ax1, 'Y', -5.0, 5.0, valinit=0)
slider1.on_changed(update)

slider_ax2 = fig.add_axes([0.2, 0.05, 0.65, 0.03])
slider2 = Slider(slider_ax2, 'Z', -5.0, 5.0, valinit=0)
slider2.on_changed(update)

# Show the plot
plt.show()