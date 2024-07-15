# ======= Libería basada en Robotics Toolbox de Peter Corke para MATLAB =======
import numpy as np
# =============================================================================
    # Pure Rotation about the x-axis | Rotation about the n-axis | ROLL
def trotx(x, unit = "rad"):
    return np.matrix([[1,         0,         0, 0],
                      [0, np.cos(x),-np.sin(x), 0],
                      [0, np.sin(x), np.cos(x), 0],
                      [0,         0,         0, 1]])

# =============================================================================
# Pure Rotation about the y-axis | Rotation about the o-axis | PITCH
def troty(y, unit = "rad"):
    return np.matrix([[np.cos(y), 0, np.sin(y), 0],
                      [0,         1,         0, 0],
                      [-np.sin(y),0, np.cos(y), 0],
                      [0,         0,         0, 1]])

# =============================================================================
# Pure Rotation about the z-axis | Rotation about the a-axis | YAW
def trotz(z, unit = "rad"):
    return np.matrix([[np.cos(z),-np.sin(z), 0, 0],
                      [np.sin(z), np.cos(z), 0, 0],
                      [0,         0,         1, 0],
                      [0,         0,         0, 1]])

# =============================================================================
# Composed Rotations | trotx(x)@troty(y)@trotz(z)
def trotxyz(x,y,z):
    if x != 0. or y != 0. or z != 0.:
        return trotx(x)*troty(y)*trotz(z)
    else:
        return np.identity(4)
    
# =============================================================================
# Pure Translation along the xyz axes | Pure Translation along the noa axes
def transl(x,y,z):
    return np.matrix([[1, 0, 0, x],
                      [0, 1, 0, y],
                      [0, 0, 1, z],
                      [0, 0, 0, 1]])

# =============================================================================
# Rotation and Translation
def RT(orientation, position):
    roll = orientation[0]
    pitch = orientation[1]
    yaw = orientation[2]
    x = position[0]
    y = position[1]
    z = position[2]
    translation = np.matrix([[1, 0, 0, x],
                             [0, 1, 0, y],
                             [0, 0, 1, z],
                             [0, 0, 0, 1]])
    rotation = trotxyz(roll, pitch, yaw)
    return rotation * translation

# =============================================================================
# Transform a vector to a desired rotation and location
def transform(coord,rotation,translation):
    v = np.array([  [coord[0]],
                    [coord[1]],
                    [coord[2]],
                    [      1]])
    
    tranformVector = RT(rotation, translation) * v
    return np.array([tranformVector[0, 0], tranformVector[1, 0], tranformVector[2, 0]])