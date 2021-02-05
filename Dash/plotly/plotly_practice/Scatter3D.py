import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
df = pd.read_csv("../Dataset/citrus.csv").dropna()

pd.set_option('display.max_columns', 30)


fig = px.scatter_3d(df,
                    height=800,
                    width=1000,
                    template='gridon',
                    x='weight',
                    y='blue',
                    z='red',
                    opacity=0.8,
                    symbol='name',
                    symbol_map={'orange':'square-open','grapefruit':'hexagram-open-dot'},
                    # color_discrete_sequence=['orange','blue'],
                    # color='name'
                    )

app.layout = html.Div([
    dcc.Graph(id='Scatter3d', figure=fig)
])
