#! /home/macbuse/miniconda3/bin/python3.11

import plotly.graph_objects as go
import numpy as np

# Generate curve data
n_pts = 80
n_curves = 100


T = np.linspace(0,2*np.pi,n_pts)
Z = np.exp(1J*T)
RC = 1 + .5*Z
RL =  np.log(np.abs(RC)) + 1J*np.arctan2(RC.imag,RC.real)

W = Z.real + 3.5J*Z.imag 

title = "Non affine homotopy to a circle"

HH = [(1-t)*W + t*RL for t in np.linspace(0,1,n_curves)]
H = np.exp(HH) + 3


gamma0 = go.Scatter(x=H[0].real, y=H[0].imag, 
                     mode="lines",
                     line=dict(width=2, color="red"))

gammat = go.Scatter(x=H[0].real, y=H[0].imag, 
                     mode="lines",
                     line=dict(width=2, color="blue"))

gamma1 = go.Scatter(x=H[n_curves-1].real, y=H[n_curves-1].imag, 
                     mode="lines",
                     line=dict(width=2, color="red"))

origin = go.Scatter(x=[3], y=[0], mode="markers",
                    marker=dict(size=10, color="black"))

gamma_hat = go.Scatter(x=HH[0].real, y=HH[0].imag, 
                     mode="lines",
                     line=dict(width=2, color="blue"))

#this is the range of the plot
xm = -1
xM = 6
ym = -3.5
yM = 3.5

box = go.Scatter(x=[xm, 1, 1, xm, xm], y=[ym, ym, yM, yM, ym],
                 fill="toself", 
                 # color="rgba(1,0,0,0.2)",
                 fillcolor="rgba(1,0,0,0.1)")


# Create figure
fig = go.Figure(data=[gammat, gamma0, gamma1, origin, gamma_hat,
                box])


fig.update_layout(width=700, height=700,

         xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
         yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),

        title_text=title, title_x=0.5,

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

frames=[go.Frame( data=[go.Scatter(x=H[k].real, y=H[k].imag),
                        go.Scatter(x=HH[k].real,y = HH[k].imag)],
                 traces=[0,4]) for k in range(n_curves) ]

fig.update(frames=frames)
fig.show()
fig.write_html(f"{title.replace(' ','_')}.html")
