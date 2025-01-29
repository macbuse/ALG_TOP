#! /home/macbuse/miniconda3/bin/python3.11

import plotly.figure_factory as ff

import numpy as np
from scipy.spatial import Delaunay

turns = 8

u = np.linspace(0, turns*2*np.pi, turns*24)
v = np.linspace(1,2,10)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

x = v*np.cos(u)
y = v*np.sin(u)
z = u

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices,
                         title=dict(text="Cover of annulus"))
fig.show()
