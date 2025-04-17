#! /home/macbuse/miniconda3/bin/python3.11


import plotly.figure_factory as ff
import numpy as np


turns = 1
xw, yw = turns*20 , 5
u = np.linspace(0, turns*2*np.pi, xw)                          
v = np.linspace(-1,1,yw)                                              
u,v = np.meshgrid(u,v)
u = u.flatten()
v = .5*v.flatten()                                                      
t = 0                                                                       
x = (8 + 0.5 * v * np.cos(u / 2 + t)) * np.cos(u)
y = (8 + 0.5 * v * np.cos(u / 2 + t)) * np.sin(u)
z = (0.5 * v * np.sin(u / 2 + t))

x = (3 + (np.cos(v)))*np.cos(u)
y = (3 + (np.cos(v)))*np.sin(u)
z = np.sin(v)

#triangulate in the way you want
T1 = np.array([0,1,xw])
T2 = np.array([1,xw+1,xw])
simplices1 = [ T1 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 
simplices2 = [ T2 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 

simplices = simplices1 +  simplices2

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices,
                         title=dict(text="Mobius strip"),)
fig.show()
