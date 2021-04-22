import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def view_analysis(yt):

    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [html.H3("Treanding Date vs Views(videos)", className="card-title"),
                dcc.Dropdown(
                    id="title_name",persistence_type='memory',
                    options=[{"label": x, "value": x}
                             for x in yt['title'].unique()],
                    value=yt['title'][1],
                    clearable=False,
                    style={'font-size': '15px', 'color': '#010106',
                           "height": "40px",
                           "text-align": "center",

                           'white-space': 'nowrap', 'text-overflow': 'ellipsis'},
                ),
                html.Br(),
                dcc.Graph(id="time-series-chart"),
            ]
            ), style={"backgroundColor": "#082255", 'textAlign': 'center',"borderRadius": "20px"}
        )
    )

    return ht
