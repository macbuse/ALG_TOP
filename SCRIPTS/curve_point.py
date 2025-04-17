#! /home/macbuse/miniconda3/bin/python3.11

import plotly.graph_objects as go
import numpy as np
# Generate curve data
npts = 100
t = np.linspace(0, 2*np.pi, npts)

Z = 2*np.exp(1j*t)
Z = 1+ Z + Z**2
x = Z.real
y = Z.imag
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = np.min(y) - 1.5
yM = np.max(y) + 1.5
xx = Z.real
yy = Z.imag


# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=[xx[0]], y=[yy[0]],
                     mode="markers",
                     marker=dict(color="red", size=10)),
          go.Scatter(x=[0,xx[0]], y=[0,yy[0]],
                     mode="lines",
                     marker=dict(color="red", size=10))]
)

fig.update_layout(width=600, height=600,
        # xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        # yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Kinematic Generation of a Planar Curve", title_x=0.5,
        updatemenus = [dict(type = "buttons",
        buttons = [
            dict(

                args = [None, {"frame": {"duration": 20, 
                                         "redraw": False
                                         },
                                "fromcurrent": True, "transition": {"duration": 10}}],

                label = "Play",
                method = "animate",

                )])])

fig.update(
    frames=[go.Frame(
        data=[
        go.Scatter(x=[x[k]], y=[y[k]]),
        go.Scatter(x=[0,xx[k]], y=[0,yy[k]]),
        ], 
        traces=[1,2])
        for k in range(npts)
        ]
)

fig.show()
