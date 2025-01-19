import plotly.graph_objects as go
import numpy as np 

x=[0, 0, 1, 1, 0, 0, 1, 1]
y=[0, 1, 1, 0, 0, 1, 1, 0]
z=[0, 0, 0, 0, 1, 1, 1, 1]

i= [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6]
j= [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
k= [0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2]

verts = np.zeros((4,3))
verts[1:,:] = np.identity(3)

faces = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]

verts = np.zeros((8,3))
verts[1:4,:] = np.identity(3)
verts[5:,:]  = -np.identity(3)

ff = np.array([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
faces = np.zeros((8,3))
faces[:4,:] = ff
faces[4:,:] = ff + 4

x,y,z = verts.T
i,j,k = np.array(faces).T

my3dmesh = go.Mesh3d(x=x,y=y,z=z, 
                     i=i, j=j, k=k, 
                     intensity = np.linspace(1, 1, 8, endpoint=True),
                     name='y')
fig = go.Figure(data=my3dmesh)
fig.show()
