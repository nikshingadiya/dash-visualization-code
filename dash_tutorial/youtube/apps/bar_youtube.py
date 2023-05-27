import pathlib

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from app import app
from channel_comparision import update_box_channel, channel_box
from channel_summary import filter_describe_data
from channel_summary import stastics_table
from most_like_static import most_likes_video, most_views_video
from select_category import drop_down_category
from top_treanding import top_10_trending_videos
from view_analysis_date import view_analysis

pd.set_option('display.max_columns', 30)
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
yt = pd.DataFrame()
for chunk in pd.read_csv(DATA_PATH.joinpath("CAvideos1.csv"), chunksize=10000):
    yt = pd.concat([yt, chunk])
    break


# print(yt.head())


def main_title():
    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H1("Youtube Analysis ", className="text-center mb-4"),

                ]
            ), style={"backgroundColor": "#082255"}
        )
    )
    return ht


# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

layout = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            main_title()
                        ], width=12),

                    ], align='center', justify="around"),
                html.Br(),
                dbc.Row([
                    dbc.Col(
                        [
                            top_10_trending_videos(df=yt),

                        ], width={'size': 8}),
                    dbc.Col(
                        [
                            stastics_table(yt),

                        ], width={'size': 4}),

                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col(
                        [
                            most_views_video(df_data=yt),

                        ], width={'size': 6}),
                    dbc.Col(
                        [
                            most_likes_video(df_data=yt)
                        ], width={'size': 6}
                    ),
                ], align='center'),
                html.Br(),
                dbc.Row(
                    dbc.Col(
                        [
                            drop_down_category(yt)
                        ], width={'size': 12}
                    )
                ),
                html.Br(),
                dbc.Row
                    (
                    dbc.Col(
                        [
                            channel_box(yt)
                        ], width={'size': 12}
                    )

                ),
                html.Br(),

                dbc.Row
                    (
                    dbc.Col(
                        [
                            view_analysis(yt)
                        ], width={'size': 12}
                    )

                )

            ]
        ), color='grey'
    ),

    dcc.Store(
        id='clientside-store-figure', data={}
    ),
    dcc.Store("id-channel-storage", data={}),
    dcc.Store("id-channel-storage1", data={}),
    dcc.Store("time-series-data", data={})

])


@app.callback(
    Output('clientside-store-figure', 'data'),
    [dash.dependencies.Input('demo-dropdown', 'value')],
)
def update_store_data(value):
    df = filter_describe_data(yt, value)
    print(df.to_dict("records"))

    return df.to_dict('records')


# Clientside callback
app.clientside_callback(
    """
       function(data) {
            if(data === undefined) {
                return '';
            }
            return data;
        }
        """,
    Output('table', 'data'),
    Input('clientside-store-figure', 'data'),
    Input('demo-dropdown', 'value')
)


## box plot
@app.callback(
    dash.dependencies.Output('id-channel-storage', 'data'),
    [dash.dependencies.Input('channel-dropdown', 'value')
        , dash.dependencies.Input('views/likes', 'value'),
     dash.dependencies.Input('category_name', 'value')]
)
def update_store_data(*value):
    X = yt[yt['channel_title'] == value[0]][value[1]]

    return update_box_channel(X)


# # Clientside callback
app.clientside_callback(
    """

   function(figure_data) {
       if(figure_data === undefined) {
           return {'data': [], 'layout': {}};
       }
       const fig = Object.assign({}, figure_data, {
               'layout': {
                   ...figure_data.layout

               }
       });
        return fig;
        }
   """,
    Output('channel_box', 'figure'),
    Input('id-channel-storage', 'data')

)


#
# @app.callback(
#     dash.dependencies.Output('table', 'data'),
#     [dash.dependencies.Input('demo-dropdown', 'value')]
# )
# def update_output(value):
#     df = filter_describe_data(yt, value)
#     return df.to_dict('records')
# Channel Comparision

# @app.callback(
#     dash.dependencies.Output('channel_box', 'figure'),
#     [dash.dependencies.Input('channel-dropdown', 'value'),
#      dash.dependencies.Input('views/likes', 'value')])
# def update_output(*value):
#     X = yt[yt['channel_title'] == value[0]][value[1]]
#
#     return box_channel(X)
#
#
# @app.callback(
#     dash.dependencies.Output('channel_box1', 'figure'),
#     [dash.dependencies.Input('channel-dropdown1', 'value'),
#      dash.dependencies.Input('views/likes1', 'value')])
# def update_output(*value):
#     X = yt[yt['channel_title'] == value[0]][value[1]]
#
#     return box_channel(X)

# @app.callback(
#     dash.dependencies.Output("time-series-chart", "figure"),
#     [dash.dependencies.Input("title_name", "value")])
# def update_layout(value):
#     Y = yt[yt['title'] == value]
#     Y = Y[Y['views'] > 100000]
#     Y = Y[['trending_date', 'views']]
#     fig = px.line(Y, x='trending_date', y='views')
#     fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
#     fig.update_layout(plot_bgcolor='#673435',
#                       paper_bgcolor='#ADBC6E', xaxis_tickformat='%H:%M <br> %d %B (%a)<br>%Y')
#
#     return fig

# @app.callback():
#     dash.dependencies.Output('id-channel-storage1', 'data')
#   dash.dependencies.Input('category_name', 'value')

@app.callback(
    dash.dependencies.Output('id-channel-storage1', 'data'),
    [dash.dependencies.Input('channel-dropdown1', 'value')
        , dash.dependencies.Input('views/likes1', 'value'),
     ]
)
def update_store_data(*value):
    X = yt[yt['channel_title'] == value[0]][value[1]]

    return update_box_channel(X)


# # Clientside callback
app.clientside_callback(
    """

    function(figure_data) {
        if(figure_data === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign ({},figure_data, {
                'layout': {
                    ...figure_data.layout

                }
        });
         return fig;
         }
    """,
    Output('channel_box1', 'figure'),
    Input('id-channel-storage1', 'data')

)


# box plot

@app.callback(
    dash.dependencies.Output("time-series-data", "data"),
    [dash.dependencies.Input("title_name", "value")])
def update_view_analysis(value):
    Y = yt[yt['title'] == value]
    Y.loc[:, 'views_log10_scale'] = np.log10(Y['views'])

    Y = Y[['trending_date', 'views_log10_scale']]
    fig = px.line(Y, x='trending_date', y='views_log10_scale')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=30)))
    fig.update_layout(plot_bgcolor='#673435',
                      paper_bgcolor='#ADBC6E', xaxis_tickformat='%H:%M <br> %d %B (%a)<br>%Y')

    return fig


app.clientside_callback(
    """

    function(figure_data) {
        if(figure_data === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign ({},figure_data, {
                'layout': {
                    ...figure_data.layout

                }
        });
         return fig;
         }
    """,
    Output('time-series-chart', 'figure'),
    Input('time-series-data', 'data')

)

# if __name__ == '__main__':
#     app.run_server(port=8083, debug=True, dev_tools_ui=True)
