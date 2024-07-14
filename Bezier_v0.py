import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = np.array([50,100,140,150,150,150,-100,0,0,-151.5,-151.5,-141,-100,-50]) /10
z = np.array([-250,-250,-250,-180,-180,-180,-70,-180,-160.5,-160.5,-160.5,-250,-250,-250]) / 10

t = sp.symbols("t")
N = len(x)

def fact(f):
  aux = 1
  for i in range(np.abs(f)):
    aux = aux*(i+1)
  return aux

def comb(n,i):
  aux = fact(n-1)/(fact(i)*fact(n-1-i))
  return aux

tBz = np.linspace(0, 1,20) # Time from 0 -> 1 in num=20 for smooth planning

# Bernstein Polynomial
sum_tx = 0
sum_ty = 0
for i in range(N):
    aux = 0
    aux = comb(N,i)*(t**i)*((1-t)**(N-1-i))
    sum_tx = sum_tx + aux*x[i]
    sum_ty = sum_ty + aux*z[i]
    
xBz = np.zeros((1,len(tBz)))[0] # Bernstein Polynomial empty array to find every point for x
yBz = np.zeros((1,len(tBz)))[0] # Bernstein Polynomial empty array to find every point for z

# Bezier Curve
for i in range(len(tBz)):
    xBz[i] = sum_tx.subs(t,tBz[i]) # Parametric Bezier-Bernstein polynomial to find every point for x
    yBz[i] = sum_ty.subs(t,tBz[i]) # Parametric Bezier-Bernstein polynomial to find every point for z


#fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d', proj_type = 'ortho')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.scatter(x, 0, z)
ax.plot(x,np.zeros((14,1)),z, dashes=[4, 4])
ax.plot(xBz,np.zeros((20,1)), yBz)

plt.show()