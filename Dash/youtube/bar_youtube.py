import re

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)
# external_stylesheets=[dbc.themes.DARKLY])

pd.set_option('display.max_columns', 30)
yt = pd.read_csv("./assets/data/CAvideos.csv")


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
    # publish_time
    df['publish_time'] = pd.to_datetime(df['publish_time'])

    # making object to numeric
    df['views'] = df['views'].astype('Int64')
    df['likes'] = df['likes'].astype('Int64')
    df['dislikes'] = df['dislikes'].astype('Int64')
    df['comment_count'] = df['comment_count'].astype('Int64')

    return df


yt = clean_data(yt)
yt['video_short_names'] = yt['title'].apply(lambda x: search_words(x))


# print(yt.head())


def most_likes_video(df_data=None):
    df_data = df_data[df_data['trending_date'] == '2017-11-14']
    df_data = df_data.sort_values(by='likes', ascending=False)[:10]
    df_data = df_data.sort_values(by='likes')
    dt = df_data['trending_date'][0]

    fig = px.bar(data_frame=df_data, width=500,
                 height=400,
                 title=f"Video vs Likes Date:{dt}",
                 x='likes', y='video_short_names', text='likes',
                 custom_data=['likes', 'title'],
                 labels={"video_short_names": ""},

                 hover_data={'likes': True, 'title': True, 'video_short_names': False})

    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_yaxes(title_standoff=0)
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=40)))

    fig.update_yaxes(
        ticksuffix=" ",
        title_standoff=0,
        # showline=True, linewidth=4,linecolor='black'

    )
    fig.update_layout(title_xref="paper")
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
    return fig


def most_views_video(df_data=None):
    df_data = df_data[df_data['trending_date'] == '2017-11-14']
    df_data = df_data.sort_values(by='views', ascending=False)[:10]
    df_data = df_data.sort_values(by='views')
    dt = df_data['trending_date'][0]
    fig = px.bar(data_frame=df_data, width=500,
                 height=400,
                 # template='plotly_dark',

                 title=f"Video vs views Date:{dt}",
                 x='views', y='video_short_names', text='views',
                 custom_data=['views', 'title'],
                 hover_data={'views': True, 'title': True, 'video_short_names': False})
    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(margin=(dict(l=0, r=0, b=0, t=40)))
    fig.update_yaxes(
        ticksuffix=" ",
        # showline=True, linewidth=3,linecolor='black'
    )
    fig.update_layout(dict(title_xref="paper",title_yref="paper"))
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
    return fig


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


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    [

        dbc.Row([dbc.Col(dcc.Graph(id='most_views', figure=most_views_video(yt), config={
            'displaylogo': False,
            'modeBarButtonsToRemove': ['toggleSpikelines', 'hoverCompareCartesian']
        }, )
                         , width={'size': 5}),

                 dbc.Col(dcc.Graph(id='most_likes', figure=most_likes_video(yt),
                                   config={

                                       'displaylogo': False,
                                       'modeBarButtonsToRemove': ['toggleSpikelines', 'hoverCompareCartesian']
                                   }
                                   )
                         , width={'size': 5})

                 ]
                )
    ])
