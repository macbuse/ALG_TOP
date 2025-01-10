# https://community.plotly.com/t/show-edges-of-the-mesh-in-a-mesh3d-plot/33614/6
# https://plotly.com/~empet/14749/mesh3d-with-intensities-and-flatshading/#/


import numpy as np
import plotly.graph_objects as go

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Vertices of an icosahedron
verts = np.array([
    [-1,  phi,  0],
    [ 1,  phi,  0],
    [-1, -phi,  0],
    [ 1, -phi,  0],
    [ 0, -1,  phi],
    [ 0,  1,  phi],
    [ 0, -1, -phi],
    [ 0,  1, -phi],
    [ phi,  0, -1],
    [ phi,  0,  1],
    [-phi,  0, -1],
    [-phi,  0,  1]
])

# Normalize vertices for a unit icosahedron
verts /= np.linalg.norm(verts[0])

# Faces (triangles)
faces = np.array([
    [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
    [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
    [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
    [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
])








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
    name='Octahedron',
    # opacity=0.5
)

my3dmesh.update(cmin=-7,# atrick to get a nice plot (z.min()=-3.31909)
               lighting=dict(ambient=0.18,
                             diffuse=1,
                             fresnel=0.1,
                             specular=1,
                             roughness=0.05,
                             facenormalsepsilon=1e-15,
                             vertexnormalsepsilon=1e-15),
               lightposition=dict(x=100,
                                  y=200,
                                  z=0
                                 )
                      );

# Plot the octahedron
layout = go.Layout(
         title="Icosahedron",
         font=dict(size=16, color='white'),
         width=700,
         height=700,
         scene_xaxis_visible=False,
         scene_yaxis_visible=False,
         scene_zaxis_visible=False,
         paper_bgcolor='rgb(150,150,150)',
       
        )

fig = go.Figure(data=my3dmesh, layout=layout)
fig.write_html('Icosahedron.html', auto_open=True)
