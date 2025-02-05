#! /home/macbuse/miniconda3/bin/python3.11


import plotly.graph_objs as go
import numpy as np 

def rot(t):
    return np.array([[np.cos(t), -np.sin(t), 0],
                     [np.sin(t), np.cos(t), 0],
                     [0, 0, 1]])

turns = 1
sides = 8
xw, yw = 4 , sides + 1
u = np.linspace(0, np.pi, xw) 
v = np.linspace(0,2*np.pi,yw) 

ring = np.array([[0]*yw,np.cos(v) + 2, np.sin(v)])
verts = [rot(t) @ ring for t in u]

x, y, z = np.concatenate(verts, axis=1)

# x, y, z = [], [], []
# for t in u[:]:
#     verts = rot(t) @ ring
#     x.extend(verts[0])
#     y.extend(verts[1])
#     z.extend(verts[2])




points = go.Scatter3d(x=x, y=y, z=z, mode="markers",
                         marker=dict(size=10, color="red"))

title = "Helicoid"

fig = go.Figure(data=[points])

xm = ym = -1.5
xM = yM = 1.5

fig.update_layout(width=600, height=800,

         xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
         yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),

        title_text=title, title_x=0.5,

        updatemenus = [dict(type = "buttons",
        buttons = [
            dict(

                args = [None, {"frame": {"duration": 200, 
                                         "redraw": True
                                         },
                                "fromcurrent": True,
                               "transition": {"duration": 5}}],

                label = "Play",
                method = "animate",

                )])])






fig.show()
fig.write_html(f"{title.replace(' ','_')}.html")
