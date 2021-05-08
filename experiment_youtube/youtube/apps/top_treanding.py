import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import  dash_bootstrap_components as dbc
def top_10_trending_videos(df=None):
    from filtter_data import top_treanding
    df = top_treanding(df)

    fig = px.bar(df, x='likes/views', y='video_short_names',
                 hover_data={'video_short_names': True},
                 animation_frame='t_date',

                 color='likes/views',
                 color_continuous_scale=px.colors.sequential.Purples,

                 text='likes/views',
                 orientation='h', range_x=(0, 0.6),
                 )
    fig.update_layout(margin=dict(t=40, b=0, l=0, r=0), plot_bgcolor='#C1C3D4',
                      paper_bgcolor='#EAE6EA')

    fig.update_yaxes(automargin=True)

    # fig.update_xaxes(showgrid=False)



    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 5000
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 5000

    fig['layout']['updatemenus'][0]['pad'] = dict(r=10, t=50)
    fig['layout']['sliders'][0]['pad'] = dict(r=10, t=30, b=20)
    fig.layout.sliders[0].font = dict(family="Overpass", size=18, color="blue")
    fig.layout.sliders[0].activebgcolor = "red"
    fig.layout.sliders[0].borderwidth = 5
    fig.layout.sliders[0].bgcolor = "#9192FF"
    fig.update_traces(textposition='auto')

    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Treanding Videos With Date", className="card-title",style={"color":"#0E0E1B"}),
                    dcc.Graph(figure=fig)
                ]
            ), style={"backgroundColor": "#EAE6EA", 'textAlign': 'center',"borderRadius": "20px"}
        )
    )
    return ht