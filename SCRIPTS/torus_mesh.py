#! /home/macbuse/miniconda3/bin/python3.11

import plotly.figure_factory as ff

import numpy as np

#squares nearly
xw, yw = 20,11

u = np.linspace(0, 2*np.pi, xw) 
v = np.linspace(0,2*np.pi, yw) - np.pi/2
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

# x = (3 + (np.cos(v)))*np.cos(u)
# y = (3 + (np.cos(v)))*np.sin(u)
# z = np.sin(v)

x = (3 + (np.cos(v)))*np.cos(u)
y = (3 + (np.cos(v)))*np.sin(u)
z = np.sin(v)

T1 = np.array([0,1,xw])
T2 = np.array([1,xw+1,xw])
simplices1 = [ T1 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 
simplices2 = [ T2 + k for k in range(xw*(yw-1))
               if (k+1) % xw != 0] 

simplices = simplices1 +  simplices2
# simplices = simplices[::2]

# print(simplices)
fig = ff.create_trisurf(x=x, y=y, z=z,
                         simplices=simplices,
                         title=dict(text="Torus"), aspectratio=dict(x=1, y=1, z=0.3))
fig.show()

# fig.write_html("torus.html")
