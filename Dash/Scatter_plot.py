import plotly.graph_objs as go

import plotly.offline as pyo

import numpy as np

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data1 = [go.Scatter(x=random_x, y=random_y, mode='markers',
                    marker=dict(size=12,
                                color='rgb(51,100,251)',
                                symbol='diamond',
                                line={'width': 2})
                    )]
layout1 = go.Layout(title="numpy-fig", xaxis=dict(title="x_value"), yaxis=dict(title="y_value"))
fig1 = go.Figure(data1, layout1)
pyo.plot(fig1, filename='Scatter_plot.html')
