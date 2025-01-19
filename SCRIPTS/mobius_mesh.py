import plotly.figure_factory as ff

import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(0, 2*np.pi, 24)
v = np.linspace(-1, 1, 8)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

tp = 1 + 0.5*v*np.cos(u/2.)
x = tp*np.cos(u)
y = tp*np.sin(u)
z = 0.5*v*np.sin(u/2.)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig = ff.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices,
                         title=dict(text="Mobius Band"))
fig.show()
