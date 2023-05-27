import time
from timeit import default_timer as timer
s = time.time()
import re
# import modin.pandas as pd
import dash
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from channel_summary import filter_describe_data
from channel_summary import stastics_table
from channel_comparision import box_channel
from channel_comparision import channel_box
from view_analysis_date import view_analysis

# external_stylesheets=[dbc.themes.DARKLY])

pd.set_option('display.max_columns', 30)
yt = pd.read_csv("data/CAvideos.csv")
e = time.time()
print("importing_time", e - s)



s = time.time()
def search_words(text):
    result = re.findall(r'\w+', text)
    result = result[0:3]
    return " ".join(result)


def datef(x):
    l, m, n = x[0], x[1], x[2]
    x[0] = l
    x[1] = n
    x[2] = m
    return str("20" + x[0] + "-" + x[1] + "-" + x[2])


def clean_data(df):
    #   trending_date
    df['trending_date'] = df['trending_date'].str.replace(".", "-")
    df['trending_date'] = df['trending_date'].str.split("-").apply(lambda x: datef(x))
    df['trending_date'] = pd.to_datetime(df['trending_date'])

    # yt['regular_date'] = yt['trending_date'].apply(lambda x: x.date())
    # publish_time
    df['publish_time'] = pd.to_datetime(df['publish_time'])

    # making object to numeric
    df['views'] = df['views'].astype('Int64')
    df['likes'] = df['likes'].astype('Int64')
    df['dislikes'] = df['dislikes'].astype('Int64')
    df['comment_count'] = df['comment_count'].astype('Int64')
    df['video_short_names'] = df['title'].apply(lambda x: search_words(x))

    return df


yt = clean_data(yt)

s = time.time()

# print(yt.head())
def top_10_trending_videos(df=None):
    from filtter_data import top_treanding
    df=top_treanding(df)

    fig = px.bar(df, x='likes/views', y='video_short_names',
                 hover_data={'video_short_names': True},
                 animation_frame='t_date',

                 color='likes/views',
                 color_continuous_scale=px.colors.sequential.haline,

                 text='likes/views',
                 orientation='h', range_x=(0, 0.6),
                 )
    fig.update_layout(margin=dict(t=40, b=0, l=0, r=0))

    fig.update_yaxes(automargin=True)

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 5000
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 5000

    fig['layout']['updatemenus'][0]['pad'] = dict(r=5, t=60)
    fig['layout']['sliders'][0]['pad'] = dict(r=5, t=40)
    fig.update_traces(textposition='auto')
    fig.update_layout(plot_bgcolor='#673435',
                      paper_bgcolor='#ADBC6E')

    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Treanding Videos With Date", className="card-title"),
                    dcc.Graph(figure=fig)
                ]
            ), style={"backgroundColor": "#082255", 'textAlign': 'center'}
        )
    )
    return ht


def most_likes_video(df_data=None):
    from filtter_data import most_likes
    df_data=most_likes(df_data)

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
    df_data= most_views(df_data)
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


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            # main_title()
                        ], width=12),

                    ], align='center', justify="around"),
                html.Br(),
                dbc.Row([
                    dbc.Col(
                        [
                            # top_10_trending_videos(df=yt),


                        ], width={'size': 8}),
                    dbc.Col(
                        [
                            # stastics_table(yt),

                        ], width={'size': 4}),

                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col(
                        [
                            # most_views_video(df_data=yt),

                        ], width={'size': 6}),
                    dbc.Col(
                        [
                           # most_likes_video(df_data=yt)
                        ], width={'size': 6}
                    ),
                ], align='center'),
                html.Br(),
                dbc.Row
                    (
                    dbc.Col(
                        [
                            channel_box(yt)
                        ], width={'size': 12}
                    )

                ),
                dbc.Row
                    (
                    dbc.Col(
                        [
                            # view_analysis(yt)
                        ], width={'size': 12}
                    )

                )

            ]
        ), color='grey'
    ),
    dcc.Store("id-channel-storage",data={}),
    dcc.Store("id-channel-storage1",data={})


])





@app.callback(
    dash.dependencies.Output('id-channel-storage', 'data'),
    [dash.dependencies.Input('channel-dropdown', 'value')
     ,dash.dependencies.Input('views/likes', 'value')]
)
def update_output(*value):
    X = yt[yt['channel_title'] == value[0]][value[1]]

    return box_channel(X)


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


@app.callback(
    dash.dependencies.Output('id-channel-storage1', 'data'),
    [dash.dependencies.Input('channel-dropdown1', 'value')
        , dash.dependencies.Input('views/likes1', 'value')]
)
def update_output(*value):
    X = yt[yt['channel_title'] == value[0]][value[1]]

    return box_channel(X)


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

# @app.callback(
#     dash.dependencies.Output('table', 'data'),
#     [dash.dependencies.Input('demo-dropdown', 'value')]
# )
# def update_output(value):
#     df = filter_describe_data(yt, value)
#     return df.to_dict('records')
#

# @app.callback(
#     Output('clientside-store-figure', 'data'),
#     [dash.dependencies.Input('demo-dropdown', 'value')],
# )
# def update_store_data(value):
#     df = filter_describe_data(yt, value)
#     print(df.to_dict("records"))
#     return df.to_dict('records')
#
# # Clientside callback
# app.clientside_callback(
#     """
#        function(data) {
#             if(data === undefined) {
#                 return '';
#             }
#             return data;
#         }
#         """,
#     Output('table', 'data'),
#     Input('clientside-store-figure', 'data'),
#     Input('demo-dropdown', 'value')
#
#
# )

# Channel Comparision
#
# @app.callback(
#     dash.dependencies.Output('channel_box', 'figure'),
#     [dash.dependencies.Input('channel-dropdown', 'value'),
#      dash.dependencies.Input('views/likes', 'value')])
# def update_output(*value):
#     X = yt[yt['channel_title'] == value[0]][value[1]]
#
#     return box_channel(X)
# @app.callback(
#     dash.dependencies.Output('channel_box1', 'figure'),
#     [dash.dependencies.Input('channel-dropdown1', 'value'),
#      dash.dependencies.Input('views/likes1', 'value')])
# def update_output(*value):
#     X = yt[yt['channel_title'] == value[0]][value[1]]
#
#     return box_channel(X)



#
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
#

if __name__ == '__main__':
    app.run_server(port=8082,debug=True,dev_tools_ui=True)
