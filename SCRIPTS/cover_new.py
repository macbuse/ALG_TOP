#! /home/macbuse/miniconda3/bin/python3.11

import plotly.figure_factory as ff
import numpy as np


turns = 5
xw, yw = turns*16, 5
u = np.linspace(0, turns*2*np.pi, xw)                          
v = np.linspace(1,2,yw)                                              
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()
                                                                       
x = v*np.cos(u)
y = v*np.sin(u)
z = u                                                                

##triangulate in the way you want
#simplices = np.vstack([ np.array(list(zip(range(xw),
#                  range(xw)[1:],
#                  range(xw,2*xw)))) + k*xw for k in range(yw-1) ])
#simplices2 = np.vstack([ np.array(list(zip(range(xw)[1:],
#                  range(xw,2*xw)[1:],
#                  range(xw,2*xw)))) + k*xw for k in range(yw-1) ])
#simplices = simplices.tolist() + simplices2.tolist()

T1 = np.array([0,1,xw])
T2 = np.array([1,xw+1,xw])
simplices1 = [ T1 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 
simplices2 = [ T2 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 
# simplices = simplices +  simplices2 

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices1 +  simplices2 ,
                         title=dict(text="Cover of annulus"))
fig.show()
