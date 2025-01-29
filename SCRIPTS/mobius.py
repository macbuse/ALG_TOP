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
t= 1                                                                       
x = (4 + 0.5 * v * np.cos(u / 2 + t)) * np.cos(u)
y = (4 + 0.5 * v * np.cos(u / 2 + t)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2 + t)

#triangulate in the way you want
simplices = np.vstack([ np.array(list(zip(range(xw),
                  range(xw)[1:],
                  range(xw,2*xw)))) + k*xw for k in range(yw-1) ])

simplices2 = np.vstack([ np.array(list(zip(range(xw)[1:],
                  range(xw,2*xw)[1:],
                  range(xw,2*xw)))) + k*xw for k in range(yw-1) ])

simplices = simplices.tolist() + simplices2.tolist()

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices,
                         title=dict(text="Mobius strip"),)
fig.show()
