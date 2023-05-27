import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import  dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

def drop_down_category(yt):
    ht = html.Div(
            dbc.Card
                (
                dbc.CardBody

                    (
                    [html.H3("Videos Category ", className="card-title"),
                    dcc.Dropdown(
                        id="category_name",persistence_type='memory',
                        options=[{"label": x, "value": x}
                                 for x in yt['category'].unique()],
                        value=yt['category'][1],
                        clearable=False,
                        style={'font-size': '15px', 'color': '#010106',
                               "height": "40px",
                               "text-align": "center",

                               'white-space': 'nowrap', 'text-overflow': 'ellipsis'},
                    ),

                ]
                ), style={"backgroundColor": "#082255", 'textAlign': 'center'}
            )
        )
    return ht