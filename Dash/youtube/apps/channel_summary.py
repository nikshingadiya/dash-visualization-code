import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table


# import pandas as pd
#
# # external_stylesheets=[dbc.themes.DARKLY])
#
# pd.set_option('display.max_columns', 30)
# yt = pd.read_csv("./assets/data/CAvideos.csv")
#
#
# def search_words(text):
#     result = re.findall(r'\w+', text)
#     result = result[0:3]
#     return " ".join(result)
#
#
# def datef(x):
#     l, m, n = x[0], x[1], x[2]
#     x[0] = l
#     x[1] = n
#     x[2] = m
#     return str("20" + x[0] + "-" + x[1] + "-" + x[2])
#
#
# def clean_data(df):
#     #   trending_date
#     df['trending_date'] = df['trending_date'].str.replace(".", "-")
#     df['trending_date'] = df['trending_date'].str.split("-").apply(lambda x: datef(x))
#     df['trending_date'] = pd.to_datetime(df['trending_date'])
#
#     # yt['regular_date'] = yt['trending_date'].apply(lambda x: x.date())
#     # publish_time
#     df['publish_time'] = pd.to_datetime(df['publish_time'])
#
#     # making object to numeric
#     df['views'] = df['views'].astype('Int64')
#     df['likes'] = df['likes'].astype('Int64')
#     df['dislikes'] = df['dislikes'].astype('Int64')
#     df['comment_count'] = df['comment_count'].astype('Int64')
#
#     return df


def filter_describe_data(df=None, channel_name=None):
    df = df[df['channel_title'] == channel_name]
    df = df.drop(['category_id'], axis=1)
    df = df.describe().drop(['25%', '75%'], axis=0)
    df.loc[:,'measurement'] = df.index
    df = df.round(0)
    df = df.reset_index(0, drop=True)
    df = df[['measurement', 'views', 'likes', 'comment_count', 'dislikes']]
    # df = df[df['measurement'] == '50%'] = 'median'


    return df


def channel_label_value_dict(df=None):
    channel_list = df['channel_title']

    channel_dict = [{'label': i, 'value': i} for i in channel_list]


    return channel_dict


def stastics_table(yt):
    df = filter_describe_data(yt, "NAV")
    print(df)
    return layout_return(yt, df)


def layout_return(yt, df):
    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Channel Stastics"),

                    dcc.Dropdown(
                        id='demo-dropdown',
                        options=channel_label_value_dict(yt), optionHeight=35, value="NAV",
                        searchable=True,
                        search_value="",
                        placeholder="Select a Channel",
                        style={'font-size': '15px', 'color': '#010106',
                               "height": "40px",
                               "text-align": "center",

                               'white-space': 'nowrap', 'text-overflow': 'ellipsis'},

                    ),
                    html.Br(),
                    html.Br(),
                    html.Br(),

                    dash_table.DataTable(id='table',
                                         columns=[{"name": i, "id": i} for i in df.columns],
                                         data=df.to_dict('records'),
                                         style_table={"overflowX": 'auto', 'overflowY': 'auto'},
                                         editable=False,
                                         style_data_conditional=[
                                             {
                                                 'if': {
                                                     'state': 'active'  # 'active' | 'selected'
                                                 },
                                                 'backgroundColor': '#393E3E',
                                                 'border': "1px solid #393E3E"

                                             } for i in df.columns
                                         ],

                                         style_as_list_view=True,

                                         style_cell_conditional=[
                                                                    {
                                                                        'if': {'column_id': i},
                                                                        'textAlign': 'left',

                                                                    } for i in
                                                                    ['views', 'likes', 'dislikes', 'comment_count']

                                                                ] +
                                                                [
                                                                    {

                                                                        'if': {'column_id': i},
                                                                        'textAlign': 'center'
                                                                    } for i in ['measurement']

                                                                ],

                                         style_header={
                                             'backgroundColor': 'white',
                                             'fontWeight': 'bold',
                                              "color":"black",
                                         },
                                         style_data={'border': '#393E3', 'backgroundColor': '#393E3E ',
                                                     'lineHeight': '20px',
                                                     'color': '#D0D3D4'},
                                         style_cell={'overflow': 'hidden', 'padding': '5px',
                                                     'minheight': 1200, 'minWidth': 125}
                                         )
                ]
            ), style={"height": "540px", "backgroundColor": "#082255", 'textAlign': 'center', "padding": "5px", },
            body=True
        )
    )

    return ht
