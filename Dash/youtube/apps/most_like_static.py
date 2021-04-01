import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
def most_likes_video(df_data=None):
    from filtter_data import most_likes
    df_data = most_likes(df_data)

    fig = px.bar(data_frame=df_data,
                 # title=f"Video vs Likes Date:{dt}",
                 x='likes', y='video_short_names', text='likes',
                 custom_data=['likes', 'title'],
                 labels={"video_short_names": ""},

                 hover_data={'likes': True, 'title': True, 'video_short_names': False})

    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    fig.update_layout(plot_bgcolor='#673435',
                      paper_bgcolor='#ADBC6E')
    fig.update_yaxes(
        ticksuffix=" ",
        # showline=True, linewidth=3,linecolor='black'
    )
    # fig.update_layout(dict(title_xref="paper", title_yref="paper"))
    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Likes vs Videos", className="card-title"),
                    dcc.Graph(figure=fig)
                ]
            ), style={"backgroundColor": "#082255", 'textAlign': 'center'}
        )
    )

    return ht


def most_views_video(df_data=None):
    from filtter_data import most_views
    df_data = most_views(df_data)
    fig = px.bar(data_frame=df_data,
                 # template='plotly_dark',

                 # title=f"Video vs views Date:{dt}",
                 x='views', y='video_short_names', text='views',
                 custom_data=['views', 'title'],
                 hover_data={'views': True, 'title': True, 'video_short_names': False})
    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    fig.update_layout(plot_bgcolor='#673435',
                      paper_bgcolor='#ADBC6E', )
    fig.update_yaxes(
        ticksuffix=" ",
        # showline=True, linewidth=3,linecolor='black'
    )
    # fig.update_layout(dict(title_xref="paper", title_yref="paper"))
    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Views vs Videos", className="card-title"),
                    dcc.Graph(figure=fig)
                ]
            ), style={"backgroundColor": "#082255", 'textAlign': 'center'}
        )
    )
    return ht

