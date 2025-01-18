# https://community.plotly.com/t/show-edges-of-the-mesh-in-a-mesh3d-plot/33614/6
# https://plotly.com/~empet/14749/mesh3d-with-intensities-and-flatshading/#/

import numpy as np
import plotly.graph_objects as go
import json 

verts = np.zeros((4,3))
verts[1:,:] = np.identity(3)

faces = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]

verts = np.zeros((12,3)).astype(int)
verts[1:4,:] = np.identity(3)
verts[5:8,:] = -np.identity(3) 
verts[9:,:] = np.identity(3)
verts[4:,:] += [0,0,1]

ff = np.array([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
faces = np.zeros((12,3),dtype=int)
faces[:4,:] = ff
faces[4:8,:] = ff + 4
faces[8:,:] = ff + 8

with open('simplicial.json','w') as fp:
    json.dump({'name' : 'simplicial_complex',
               'vertices': verts.tolist(),
              'faces': faces.tolist()},fp)

fn = 'icosahedron.json'
with open(fn,'r') as fp:
    data = json.load(fp)

verts = np.array(data['vertices'])
faces = np.array(data['faces']).astype(int)

# Transpose vertices for plotting
x, y, z = verts.T
i, j, k = faces.T

pl_mygrey=[0, 'rgb(153, 153, 153)'], [1., 'rgb(255,255,255)']
# Create the mesh for the octahedron

my3dmesh = go.Mesh3d( x=x, y=y, z=z, 
 i=i, j=j, k=k,
    colorscale=pl_mygrey, 
    intensity= z,
    flatshading=True,
    showscale=False,
    name=data['name'],
    # opacity=0.5
)

my3dmesh.update(cmin=-7,# atrick to get a nice plot (z.min()=-3.31909)
               lighting=dict(ambient=0.18,
                             diffuse=1,
                             fresnel=0.1,
                             specular=1,
                             roughness=0.05,
                             facenormalsepsilon=0,
                             vertexnormalsepsilon=0),
               lightposition=dict(x=100,
                                  y=200,
                                  z=0
                                 )
                      );

# Plot the mesh
layout = go.Layout(
         title=data['name'],
         font=dict(size=16, color='white'),
         width=700,
         height=700,
         scene_xaxis_visible=False,
         scene_yaxis_visible=False,
         scene_zaxis_visible=False,
         paper_bgcolor='rgb(200,200,200)',
       
        )

fig = go.Figure(data=my3dmesh,
                layout=layout)
fig.show()
