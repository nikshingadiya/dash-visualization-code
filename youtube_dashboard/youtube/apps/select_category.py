import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import  dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

def make_all_option(yt):
    all_option={}
    for i in yt['category'].unique():
        all_option[i]=yt[yt['category']==i]['channel_title']
    return all_option

def drop_down_category(yt):
    ht = html.Div(
            dbc.Card
                (
                dbc.CardBody

                    (
                    [html.H3("Videos Category ", className="card-title",style={"color":"#1E1E35"}),
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
                ), style={"backgroundColor": "#EAE6EA", 'textAlign': 'center',"borderRadius": "20px"}
            )
        )
    return ht