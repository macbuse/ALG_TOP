#! /home/macbuse/miniconda3/bin/python3.11

import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure()

fig = px.scatter(SlopeInteractive, x = SlopeInteractive["Type"], y = SlopeInteractive["Value"], color = "X", animation_frame = SlopeInteractive["Wavelength"], animation_group="Value", hover_name = SlopeInteractive.index, category_orders = {"Wavelength" : wavelengthList}, range_y = [-0.02477, 0.0139])


fig.update_layout(updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, {"frame": {"duration": 200, "redraw": False}} ])])],
            title = "Animation of groups Derivative change from 1850-8000nm", 
            xaxis_title = "SHOULDERS                 Doublets                 NONSHOULDER SINGLETS", 
            yaxis_title = "Derivative values at X wavelength")


frames=[go.Frame(data=[go.Scatter(x=[1, 2], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
            go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])],
                     layout=go.Layout(title_text="End Title"))]

fig.show()
