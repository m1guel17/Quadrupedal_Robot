import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from Operators import trotz, transl, trotx

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

origin = np.array([np.matrix(np.eye(4))])
origin_ = np.array([np.matrix(np.eye(4))* trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2)])

initial_angle = 0

# Front_Left Leg ===================================================================
matrix = origin * trotz(np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(np.pi/2) * transl(W/2, 0, L/2)
T01 = matrix * trotz(initial_angle) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
T23 = T12 * trotz(np.pi/4) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
T34 = T23 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)

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

# Function to update the line
def update_line(angle, angle2, angle3):
    T01 = matrix * trotz(angle) * transl(0, 0, 0) * transl(l1, 0, 0) * trotx(0)
    T12 = T01 * trotz(-np.pi/2) * transl(0, 0, 0) * transl(0, 0, 0) * trotx(-np.pi/2)
    T23 = T12 * trotz(angle2) * transl(0, 0, 0) * transl(l2, 0, 0) * trotx(0)
    T34 = T23 * trotz(-angle3) * transl(0, 0, 0) * transl(l3, 0, 0) * trotx(0)
        
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
    
    fig.canvas.draw_idle()

# Function to update the plot based on slider input
def update(val):
    angle0 = slider0.val * np.pi/180
    angle1 = slider1.val * np.pi/180
    angle2 = slider2.val * np.pi/180
    update_line(angle0, angle1, angle2)

# Add a slider for angle input
slider_ax0 = fig.add_axes([0.2, 0.15, 0.65, 0.03])
slider0 = Slider(slider_ax0, 'Angle', -45.0, 45.0, valinit=initial_angle)
slider0.on_changed(update)

slider_ax1 = fig.add_axes([0.2, 0.1, 0.65, 0.03])
slider1 = Slider(slider_ax1, 'Angle2', -60.0, 60.0, valinit=45)
slider1.on_changed(update)

slider_ax2 = fig.add_axes([0.2, 0.05, 0.65, 0.03])
slider2 = Slider(slider_ax2, 'Angle3', 0.0, 135.0, valinit=90)
slider2.on_changed(update)

# Show the plot
plt.show()