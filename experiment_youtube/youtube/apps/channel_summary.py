import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table



def filter_describe_data(df=None, channel_name=None):
    df = df[df['channel_title'] == channel_name].copy()
    df = df.drop(['category_id'], axis=1).copy()
    df = df.describe().drop(['25%', '75%'], axis=0).copy()
    df.loc[:,'measurement'] = df.index.copy()
    df = df.round(0).copy()
    df = df.reset_index(0, drop=True).copy()
    df = df[['measurement', 'views', 'likes', 'comment_count', 'dislikes']].copy()
    # df = df[df['measurement'] == '50%'] = 'median'
    print(df)

    return df


def channel_label_value_dict(df=None):
    channel_list = df['channel_title'].copy()
    channel_dict = [{'label': i, 'value': i} for i in channel_list]

    return channel_dict


def stastics_table(yt):
    df = filter_describe_data(yt, "NAV").copy()
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
            ), style={"height": "540px", "borderRadius": "20px", "backgroundColor": "#082255", 'textAlign': 'center', "padding": "5px", },
            body=True
        )
    )
    return ht
