import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import  dash
from app import app






from select_category import  make_all_option
# code and plot setup
# settings
# pd.options.plotting.backend = "plotly"

# sample dataframe of a wide format


# plotly figure
# fig = df.plot(template = 'plotly_dark')

def channel_box(yt):
    ht = html.Div([
        dbc.Card([
            dbc.CardBody([

                dbc.Row(
                    [

                        dbc.Col([

                            dcc.Dropdown(
                                id='channel-dropdown',
                                options=[{'label': i, 'value': i} for i in make_all_option(yt)['Music']], optionHeight=35, value="NAV",
                                searchable=True,
                                search_value="",
                                placeholder="Select a Channel", persistence_type='memory',
                                style={'font-size': '15px', 'color': '#010106',
                                       "height": "40px",
                                       "text-align": "center",

                                       'white-space': 'nowrap', 'text-overflow': 'ellipsis'}


                            ),

                        ], width={'size': 3}),

                        dbc.Col([
                            dcc.Dropdown(
                                id='views/likes',persistence_type='memory',
                                options=[{'label': 'views', 'value': 'views'},
                                         {'label': 'likes', 'value': 'likes'}], optionHeight=35, value="views",
                                searchable=True,
                                search_value="",
                                placeholder="Option",
                                style={'font-size': '15px', 'color': '#010106',
                                       "height": "40px",
                                       "text-align": "center",

                                       'white-space': 'nowrap', 'text-overflow': 'ellipsis'},

                            )

                        ], width={'size': 3}),

                        dbc.Col([
                            dcc.Dropdown(
                                id='channel-dropdown1',
                                options=[{'label': i, 'value': i} for i in make_all_option(yt)['Music']], optionHeight=35, value="NAV",
                                searchable=True,
                                search_value="",
                                placeholder="Select a Channel",
                                style={'font-size': '15px', 'color': '#010106',
                                       "height": "40px",
                                       "text-align": "center",

                                       'white-space': 'nowrap', 'text-overflow': 'ellipsis'},

                            ),

                        ], width={'size': 3}),
                        dbc.Col([
                            dcc.Dropdown(
                                id='views/likes1',
                                options=[{'label': 'views', 'value': 'views'},
                                         {'label': 'likes', 'value': 'likes'}], optionHeight=35, value="views",
                                searchable=True,
                                search_value="",
                                placeholder="Option",
                                style={'font-size': '15px', 'color': '#010106',
                                       "height": "40px",
                                       "text-align": "center",

                                       'white-space': 'nowrap', 'text-overflow': 'ellipsis'},

                            )

                        ], width={'size': 3})

                    ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id="channel_box")

                    ], width={'size': 6}),

                    dbc.Col([
                        dcc.Graph(id="channel_box1")

                    ], width={'size': 6})
                ]
                )
            ],style={"backgroundColor": "#EAE6EA", 'textAlign': 'center', "borderRadius": "20px",}),

        ],style={ "borderRadius": "24px","backgroundColor": "#EAE6EA"})

    ],)


    return ht



def update_box_channel(X=None):
    fig = px.box(X,points="all")
    fig.update_traces(fillcolor="#6776FF")

    #     fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    #     fig.update_layout(plot_bgcolor='#673725',
    #                       paper_bgcolor='#ADBC6E', )
    fig.update_yaxes(
        ticksuffix=" ",
        # showline=True, linewidth=3,linecolor='black'
    )
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    fig.update_layout(plot_bgcolor='#C1C3D4',
                      paper_bgcolor='#EAE6EA', )
    fig.update_yaxes(showgrid=False)

    return fig