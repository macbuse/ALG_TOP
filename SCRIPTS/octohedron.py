#! /home/macbuse/miniconda3/bin/python3.11

# https://community.plotly.com/t/show-edges-of-the-mesh-in-a-mesh3d-plot/33614/6
# https://plotly.com/~empet/14749/mesh3d-with-intensities-and-flatshading/#/

import numpy as np
import plotly.graph_objects as go

# Define the vertices of the octahedron
verts = np.array([
    [1, 0, 0],   # Vertex 0
    [-1, 0, 0],  # Vertex 1
    [0, 1, 0],   # Vertex 2
    [0, -1, 0],  # Vertex 3
    [0, 0, 1],   # Vertex 4
    [0, 0, -1]   # Vertex 5
])

# Define the faces of the octahedron (triangular faces)
faces = np.array([
    [0, 2, 4],  # Top front face
    [2, 1, 4],  # Top left face
    [1, 3, 4],  # Top back face
    [3, 0, 4],  # Top right face
    [0, 3, 5],  # Bottom front face
    [3, 1, 5],  # Bottom left face
    [1, 2, 5],  # Bottom back face
    [2, 0, 5]   # Bottom right face
])

# Transpose vertices for plotting
x, y, z = verts.T
i, j, k = faces.T

pl_mygrey=[0, 'rgb(153, 153, 153)'], [1., 'rgb(255,255,255)']
# Create the mesh for the octahedron

mvim.api.nvim_set_keymap('n', '<leader>pp', ':w<CR>:!python3 %<CR>', { noremap = true, silent = true })
y3dmesh = go.Mesh3d( x=x, y=y, z=z, 
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
         title="Octahedron",
         font=dict(size=16, color='white'),
         width=700,
         height=700,
         scene_xaxis_visible=False,
         scene_yaxis_visible=False,
         scene_zaxis_visible=False,
         paper_bgcolor='rgb(150,150,150)',
       
        )

fig = go.Figure(data=my3dmesh, layout=layout)
fig.show()
