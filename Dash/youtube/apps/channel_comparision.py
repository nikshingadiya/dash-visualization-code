import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import  dash
from app import app

def channel_label_value_dict(df=None):

    channel_list = df['channel_title']
    channel_dict = [{'label': i, 'value': i} for i in channel_list]

    return channel_dict
def make_all_option(yt):
    all_option={}
    for i in yt['category'].unique():
        all_option[i]=yt[yt['category']==i]['channel_title']
    return all_option





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
                                options=channel_label_value_dict(yt) , optionHeight=35, value="NAV",
                                searchable=True,
                                search_value="",
                                placeholder="Select a Channel",persistence_type='memory',
                                style={'font-size': '15px', 'color': '#010106',
                                       "height": "40px",
                                       "text-align": "center",

                                       'white-space': 'nowrap', 'text-overflow': 'ellipsis'},

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
                                options=channel_label_value_dict(yt), optionHeight=35, value="NAV",
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
            ],style={"backgroundColor": "#082255", 'textAlign': 'center'}),

        ])

    ])


    return ht

def fillter_category(df,category="Music"):
    df=df[df['category']=="Music"]
    channel_label_value_dict(df)

def update_box_channel(X=None):
    fig = px.box(X)

    #     fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    #     fig.update_layout(plot_bgcolor='#673725',
    #                       paper_bgcolor='#ADBC6E', )
    fig.update_yaxes(
        ticksuffix=" ",
        # showline=True, linewidth=3,linecolor='black'
    )
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    fig.update_layout(plot_bgcolor='#673435',
                      paper_bgcolor='#ADBC6E', )

    return fig