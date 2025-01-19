import numpy as np
import plotly.graph_objects as go
from scipy.spatial import ConvexHull

# Define the golden ratio
phi = (1 + np.sqrt(5)) / 2

# Define the vertices of a regular dodecahedron
verts = np.array([
    [1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1],  # Front vertices
    [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1],  # Back vertices
    [0, phi, 1 / phi], [0, -phi, 1 / phi], [0, phi, -1 / phi], [0, -phi, -1 / phi],  # Middle vertices
    [1 / phi, 0, phi], [-1 / phi, 0, phi], [1 / phi, 0, -phi], [-1 / phi, 0, -phi],  # Side vertices
    [phi, 1 / phi, 0], [-phi, 1 / phi, 0], [phi, -1 / phi, 0], [-phi, -1 / phi, 0]   # Top/bottom vertices
])

# Normalize vertices to make them unit length (for stellation)
verts = verts / np.linalg.norm(verts, axis=1).max()

# Compute the convex hull to get faces
hull = ConvexHull(verts)
faces = hull.simplices

# Transpose vertices for plotting
x, y, z = verts.T
i, j, k = faces.T

# Create the mesh for the stellated dodecahedron
my3dmesh = go.Mesh3d(
    x=x, y=y, z=z,
    i=i, j=j, k=k,
    intensity=np.linspace(1, 1, len(verts), endpoint=True),
    name='Stellated Dodecahedron',
    opacity=0.8
)

# Plot the stellated dodecahedron
fig = go.Figure(data=my3dmesh)
fig.show()
