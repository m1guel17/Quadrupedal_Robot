import numpy as np
from Quadrupedal_Model import Kinematic_Model

KM = Kinematic_Model()

def solve_L(coord , L1=KM.l1, L2=KM.l2, L3=KM.l3, W = KM.W, L = KM.L, start_height = -17.67766952966369):   # DELETE L1 AND START_HEIGHT AFTER TESTING ANIMATIONS 
    #check_error(coord , L1, L2, L3)
    z = coord[0]                    # X
    x = coord[1] + L1               # Y
    y = coord[2] + start_height     # Z
    
    θ1 = np.arctan(np.sqrt(x**2 + y**2 - L1**2) / L1) + np.arctan2(y, x)
    θ2 = np.arctan(-z/ np.sqrt(x**2 + y**2 - L1**2)) + np.arccos((L1**2 - L2**2 + L3**2 - x**2 - y**2 - z**2)/(-2*L2*np.sqrt(x**2 + y**2 + z**2 - L1**2)))
    θ3 = - np.pi + np.arccos((L1**2 + L2**2 + L3**2 - x**2 - y**2 -z**2) / (2*L2*L3))

    angles = np.array([θ1,θ2,θ3])    
    return angles
    
def solve_R(coord , L1, L2, L3):
    #check_error(coord , L1, L2, L3)
    z = coord[0]
    x = coord[1]
    y = coord[2]
    
    θ1 = np.pi + np.arctan2(y, x) - np.arctan(np.sqrt(x**2 + y**2 - L1**2) / L1) 
    θ2 = np.arctan2(-np.sqrt(x**2 + y**2 - L1**2), z) - np.arccos((x**2 + y**2 + z**2 - L1**2)/(2*L2*np.sqrt(x**2 + y**2 + z**2 - L1**2))) + np.pi/2
    θ3 = np.pi - np.arccos((L2**2 + L3**2 - x**2 - y**2 -z**2 + L1**2) / (2*L2*L3))
    
    angles = np.array([θ1,θ2,θ3])    
    return angles
    
"""    
solve_L([7,-8,-4],5,10,10)
print("  ")
print("  ")
print("  ")
solve_R([-7,-8,-4],5,10,10)



coord = [-7,-8,-4]
x = coord[0]
y = coord[1]
z = coord[2]

L1,L2,L3 = [5,10,10]

"""

def check_error(coord , L1, L2, L3):
    
    if type(coord) != list or len(coord) != 3:
        if type(coord) != list:
            string = type(coord)
            string = str(string).split("'")
            string = string[1]
            raise ValueError("The coord argument must be a list. You declared a {} variable.".format(string))
        if len(coord) != 3:
            raise ValueError("The coord array must contain 3 values. {} values were given.".format(len(coord)))
    
    
    """     
    if len(coord) != 3:
        raise ValueError("The coord array must contain 3 values. {} values were given in coord argument".format(len(coord)))
    
    try:
        if len(L1) != 1:
            raise ValueError("The L1 array must contain 1 value. {} values were given.".format(len(L1)))
    except:
        try:
            if type(L1) != int:
                raise ValueError("The L1 array must be an integer. {} was given.".format(type(L1)))
        except:
            print("ya we")
    try:
        if len(L2) != 1:
            raise ValueError("The L2 array must contain 1 value. {} values were given.".format(len(L2)))
    except:
        try:
            if type(L2) != int:
                raise ValueError("The L2 array must be an integer. {} was given.".format(type(L2)))
        except:
            print("ya we")
    try:
        if len(L3) != 1:
            raise ValueError("The L3 array must contain 1 value. {} values were given.".format(len(L2)))
    except:
        try:
            if type(L3) != int:
                raise ValueError("The L3 array must be an integer. {} was given.".format(type(L3)))
        except:
            print("ya we")
    """
    """
    rECHECK
    if type(L1) != int:
        if len(L1) != 1:
            raise ValueError("The L1 array must contain 1 value. {} values were given.".format(len(L1)))
    
    if type(L2) != int:
        if len(L2) != 1:
            raise ValueError("The L2 array must contain 1 value. {} values were given.".format(len(L2)))
    
    if type(L3) != int:
        if len(L3) != 1:
            raise ValueError("The L3 array must contain 1 value. {} values were given.".format(len(L3)))
    """
    
    
    
    """
    if len(L2) != 1 or type(L2) != int:
        raise ValueError("The L2 array must contain 1 value. {} values were given.".format(len(L2)))
    if len(L3) != 1 or type(L3) != int:
        raise ValueError("The L3 array must contain 1 value. {} values were given.".format(len(L3)))
    """





    