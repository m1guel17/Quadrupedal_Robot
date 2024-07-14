import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.widgets import Button
import time

#colors = ['r', 'g', 'b']
colors = ['#ff0000', '#00da00', '#0000ff']
labels = ['x', 'y', 'z']

class Fig:
    def closefig(self, event):
        plt.close(fig)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d', proj_type = 'ortho')

ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

Fig = Fig()
#pos_close = fig.add_axes([0.85, 0.05, 0.1, 0.05])
#bclose = Button(pos_close, 'Close figure')
#bclose.on_clicked(Fig.closefig)
#plt.get_current_fig_manager().full_screen_toggle()
plt.show()
#manager = plt.get_current_fig_manager(); manager.full_screen_toggle()

def graph_body(array, color = False, alpha = 0.8):
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for i in range(len(array)):
        x = np.append(x, array[i][0,3])
        y = np.append(y, array[i][1,3])
        z = np.append(z, array[i][2,3])
        
    x = np.append(x, array[0][0,3])
    y = np.append(y, array[0][1,3])
    z = np.append(z, array[0][2,3])
    
    verts = [list(zip(x,y,z))]
    v_color = [list(zip(x[:-1],y[:-1],z[:-1]))]
    
    ax.add_collection3d(Line3DCollection(verts, colors='k', linewidths=1.5))#1, linestyles=':'))
    if color == True:
        ax.add_collection3d(Poly3DCollection(v_color, alpha=alpha, facecolors='#ffc800'))
    
def graph(frameworks_array, length = 2, show_fw = False): #length: scale factor for vector
    for i in range(len(frameworks_array)):        
        for j in range(len(frameworks_array[i])):
            if len(frameworks_array[i]) == 1:
                matrix = frameworks_array[i]
                x, y, z = matrix[0][0,3] , matrix[0][1,3], matrix[0][2,3]
                u, v, w = matrix[0][:3,0] , matrix[0][:3,1], matrix[0][:3,2]
            else:
                matrix = frameworks_array[i][j]
                x, y, z = matrix[0,3] , matrix[1,3], matrix[2,3]
                u, v, w = matrix[:3,0] , matrix[:3,1], matrix[:3,2]
                #print("="*15, f'{i} Framework {j}{j+1}', "="*15, "\n", np.round(matrix, 3), "\n")
            vectors = np.array([u,v,w])
            
            if show_fw == True or len(frameworks_array) == 1: # Show frameworks per joint
                for vector, color, label in zip(vectors, colors, labels):
                    ax.quiver(x, y, z,  vector[0], vector[1], vector[2],  color = color, arrow_length_ratio = 0.3, length = length)
                    ax.text(x + 1.25*length*vector[0], y + 1.25*length*vector[1], z + 1.25*length*vector[2],  f'{label}{j}', color = color, fontsize = 10)
                    
            if j < len(frameworks_array[i]) - 1: # Print links in between joints
                if not(np.round(frameworks_array[i][j][0,3],2) == np.round(frameworks_array[i][j+1][0,3],2) and np.round(frameworks_array[i][j][1,3],2) == np.round(frameworks_array[i][j+1][1,3],2) and np.round(frameworks_array[i][j][2,3],2) == np.round(frameworks_array[i][j+1][2,3],2)):
                    ax.scatter(frameworks_array[i][j + 1][0,3], frameworks_array[i][j + 1][1,3], frameworks_array[i][j + 1][2,3], marker = 'o', color = '#151515', linewidths = 2.5)       # Plot 'o' joints
                    ax.plot([x, frameworks_array[i][j + 1][0,3]],       # x_i to x_i+1
                            [y, frameworks_array[i][j + 1][1,3]],       # y_i to y_i+1
                            [z, frameworks_array[i][j + 1][2,3]],       # z_i to z_i+1
                            color = 'gray',
                            linewidth = 2)
                    #print(f'lines{i}_{j}{j+1}')
                #else:
                    #print(f'line_{i}_{j}{j+1}', "wasn't plotted because", f'{i}_T{j-1}{j}', "and", f'{i}_T{j}{j+1}',"are in the same xyz origin")
                #print("="*44, "\n\n")