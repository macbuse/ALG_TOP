#! /home/macbuse/miniconda3/bin/python3.11
import plotly.figure_factory as ff
import numpy as np

def rotZ(t):
    return np.array([[np.cos(t), -np.sin(t), 0],
                     [np.sin(t), np.cos(t), 0],
                     [0, 0, 1]])

def rotY(t):
    return np.array([[np.cos(t), 0, np.sin(t)],
                     [0, 1, 0],
                     [-np.sin(t), 0, np.cos(t)]])

def rotX(t):
    return np.array([[1, 0, 0],
                     [0, np.cos(t), -np.sin(t)],
                     [0, np.sin(t), np.cos(t)]])

sides = 8
xw, yw = 41 , sides 
u = np.linspace(0, 2*np.pi, xw)
v = np.linspace(0,2*np.pi,yw) 

# ring = np.array([[0]*yw,4 + np.cos(v), np.sin(v)])

turns = 1.5

tv = np.array([0,2,0]).reshape(3,1)
ring = np.array([[0]*yw,[0]*yw, v/np.pi -1])
verts = [rotZ(t) @ (rotX(turns*t) @ ring + tv)   for t in u]
verts = np.concatenate(verts, axis=1)

x, y, z = verts

#triangulate in the way you want
T1 = np.array([0,1,yw])
T2 = np.array([1,yw+1,yw])
simplices1 = [ T1 + k for k in range(yw*(xw-1))
               if (k+1) % yw != 0] 
simplices2 = [ T2 + k for k in range(yw*(xw-1))
               if (k+1) % yw != 0] 

simplices = simplices1 +  simplices2
simplices= simplices[::2]

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",

                         simplices=simplices,
                         title=dict(text="Mobius strip"),)
fig.show()
