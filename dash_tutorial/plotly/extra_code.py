import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# app.layout = html.Div(style={}, children=
# [
#   dbc.Row(
#       children=[html.H3(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text'],
#
#         }
#     )],justify="center", align="center", className="h-50",style={"height": "10px"}),
# dbc.Row(
#
#       children=[
#         dbc.Col(html.H3(
#         children='views vs videos',
#         style={
#             'textAlign': 'center',
#             'color': colors['text'],
#
#         }
#     ))],justify="left", align="center",style={ 'textAlign': 'center'}),
#
#     dbc.Row(
#         children=[
#
#             dbc.Col(
#
#                 dcc.Graph(id='most_views', figure=most_views_video(yt), config={
#                     'displaylogo': False,
#                     'modeBarButtonsToRemove': ['toggleSpikelines', 'hoverCompareCartesian'],
#                     'configmode': False,
#                 }, )
#                 , width={'size': 'auto'}),
#
#             dbc.Col(dcc.Graph(id='most_likes', figure=most_likes_video(yt),
#                               config={
#
#                                   'displaylogo': False,
#                                   'modeBarButtonsToRemove': ['toggleSpikelines', 'hoverCompareCartesian']
#                               }
#                               )
#                     , width={'size': 'auto'})
#
#         ]
#     )
# ])
#
# app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])
#
# app.layout = html.Div([
#             dbc.Card(
#
#                 dbc.CardBody
#                     (
#                     dbc.Row(
#                         [
#                         dbc.Col(
#                             [
#                             main_title()
#                         ], width={'size': 12})
#                     ]
#                     )
#                 ),
#
#
#             html.Br(),
#                 dbc.Row(
#                     [
#
#                     dbc.Col(
#                         [
#                             most_views_video(df_data=yt),
#
#                         ], width={'size': 5}),
#                     dbc.Col(
#                         [
#                             most_likes_video(df_data=yt)
#                         ], width={'size': 5}
#                     ),
#
#                 ]
#                 )
#             )
#
#
#         ]
#     )



# fig.update_layout(dict(title_xanchor='left',title_yanchor='auto'))
# fig.update_layout(title_pad_t=30)

# fig.update_layout(title_pad=dict(title_pad_t=2,title_pad_b=4,title_pad_r=4,title_pad_l=4))
# fig.update_layout()
# fig.update_layout(title_y= 1)
# fig.update_traces(marker_colorbar_tickwidth=10,selector=dict(type='bar'))
# fig.update_yaxes(visible=True,
#                  title_font={"size": 20},
#                  # tickwidth=100,
#
#                  title_standoff=1,
#                  # ticklen=30,
#                  # tickangle=90,
#                  automargin=True,
#
#                  # showticklabels=False,
#                  tickfont=dict(family='Rockwell', color='black', size=14)
#                  )


# fig.update_traces(marker_colorbar_tickwidth=10,selector=dict(type='bar'))
# fig.update_yaxes(visible=True,
#                  title_font={"size": 20},
#                  # tickwidth=100,
#
#                  title_standoff=2,
#                  # ticklen=30,
#                  # tickangle=90,
#                  automargin=True,
#
#                  # showticklabels=False,
#                  tickfont=dict(family='Rockwell', color='black', size=14)
#                  )

# def view_likes_bargrid(df=None):
#     df = df[df['trending_date'] == '2017-11-14']
#     dt = df['trending_date'][0]
#     fig = make_subplots(
#         rows=1, cols=2, horizontal_spacing=0.2,
#         subplot_titles=(f"Video vs views Date:{dt}", f"Video vs likes Date:{dt}"))
#     fig1 = most_views_video(df)
#     fig2 = most_likes_video(df)
#     fig.add_trace(fig1.data[0], row=1, col=1)
#     fig.add_trace(fig2.data[0], row=1, col=2)
#
#     # axis update
#
#     fig.update_yaxes(
#         ticksuffix="     ")
#     fig.update_xaxes(title_text="views", row=1, col=1)
#     fig.update_xaxes(title_text="likes", row=1, col=2)
#     fig.update_yaxes(title_text="videos_short_name", row=1, col=1)
#     fig.update_layout(dict(border=5))
#
#     fig.update_layout(margin=dict(l=30, r=20, t=50, b=20))
#     fig.update_layout(paper_bgcolor='#9CADCB')
#     # fig.update_layout(template='ggplot2'
#     # ['ggplot2', 'seaborn', 'simple_white', 'plotly',
#     #  'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
#     #  'ygridoff', 'gridon', 'none']
#     # )
#
#     return fig


#     fig.update_layout(updatemenus=[  dict(
#             type="frame1",
#             direction="right",

#             showactive=True)])


#     fig['layout']['sliders'][0]['transition']= {'duration': 300, 'easing': 'exp'}

#     fig.update_xaxes(rangeslider_visible=True)