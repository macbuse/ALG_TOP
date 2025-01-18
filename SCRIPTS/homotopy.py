import plotly.graph_objects as go
import numpy as np

# Generate curve data
npts = 100
n_curves = 100

s = np.linspace(0, 2*np.pi, npts)

def P(z):
    return z**2 + z + 1


title = "Homotopy to a circle"
# title = "Not a homotopy to a circle"
Z = np.exp(1j*s)
W = P(2*Z)
Z = Z**2

H = [(1-t)*W + t*Z for t in np.linspace(0,1,n_curves)]


gamma0 = go.Scatter(x=H[0].real, y=H[0].imag, 
                     mode="lines",
                     line=dict(width=2, color="red"))

gammat = go.Scatter(x=H[0].real, y=H[0].imag, 
                     mode="lines",
                     line=dict(width=2, color="blue"))

gamma1 = go.Scatter(x=H[n_curves-1].real, y=H[n_curves-1].imag, 
                     mode="lines",
                     line=dict(width=2, color="red"))

origin = go.Scatter(x=[0], y=[0], mode="markers",
                    marker=dict(size=10, color="black"))

# Create figure
fig = go.Figure( data=[gammat, gamma0, gamma1, origin])

#this is the range of the plot
xm = min(H[0].real) - 1
xM = max(H[0].real) + 1
ym = min(H[0].imag) - 1
yM = max(H[0].imag) + 1

fig.update_layout(width=600, height=600,

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

fig.update( frames=[go.Frame( data=[go.Scatter(x=H[k].real,
                                               y=H[k].imag)],
                             traces=[0]) for k in range(npts) ])

fig.show()
fig.write_html(f"{title.replace(' ','_')}.html")
