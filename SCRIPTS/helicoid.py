#! /home/macbuse/miniconda3/bin/python3.11


import plotly.graph_objs as go
import numpy as np 

s = np.linspace(0,6*np.pi, 100)

Z = np.exp(1j*s)
x = Z.real
y = Z.imag

z = s/3

circle = go.Scatter3d(x=x, y=y, z=0*z, mode="lines",
                        line=dict(width=4, color="red"))

helicoid = go.Scatter3d(x=x, y=y, z=z, mode="lines",
                        line=dict(width=2, color="blue"))
k = 0

vertical_line = go.Scatter3d(x=x[[k,k]], y=y[[k,k]], 
                             z=z[[k,k]], mode="lines",
                        line=dict(width=3, color="red"))

points = go.Scatter3d(x=x[[k,k]], y=y[[k,k]], 
                             z=z[[k,k]], mode="markers",
                         marker=dict(size=10, color="red"))


title = "Helicoid"

fig = go.Figure(data=[vertical_line,points,circle,helicoid])

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



frames=[go.Frame( data=[
    go.Scatter3d(x=x[[k,k]], y=y[[k,k]], z=z[[0,k]]),
    go.Scatter3d(x=x[[k,k]], y=y[[k,k]], z=z[[0,k]])
],

                       traces=[0,1]) for k in range(100) ]


fig.update(frames=frames)
fig.show()
fig.write_html(f"{title.replace(' ','_')}.html")
