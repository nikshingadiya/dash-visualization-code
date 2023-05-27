import pathlib

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

pd.set_option('display.max_columns', 30)
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
# app = dash.Dash(__name__)
from app import app

yt = pd.DataFrame()

for chunk in pd.read_csv(DATA_PATH.joinpath("CAvideos1.csv"), chunksize=10000):
    yt = pd.concat([yt, chunk])

yt = yt.sample(frac=0.05, replace=False)

df = yt.copy()
print(yt['category'].unique())
print(yt.shape[0])


def sunbrust_graph(dt):
    fig = px.sunburst(dt, color_discrete_sequence=px.colors.qualitative.D3, path=['category', "channel_title"],
                      values='views')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), plot_bgcolor='#673435',
                      paper_bgcolor='#EAE6EA')
    fig.update_traces(textinfo='label+percent parent')
    ht = html.Div(
        dbc.Card
            (
            dbc.CardBody

                (
                [
                    html.H3("Sunbrust", className="card-title"),
                    dcc.Graph(id="sunbrust", figure=fig)
                ]
            ), style={"backgroundColor": "#EAE6EA", 'textAlign': 'center', "borderRadius": "20px"}
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
                    html.H1("Youtube Analysis ", className="text-center mb-4", style={"color": "#353535"}),

                ]
            ), style={"backgroundColor": "#eaeaea", "borderRadius": "20px"}
        )
    )
    return ht


layout = \
    html.Div([
        html.Div([
            main_title(),
            html.Br(),
        ]),

        dbc.Card(

            dbc.CardBody(

                html.Div([

                    dash_table.DataTable(
                        id='Table',

                        columns=[
                            {"name": i, "id": i, "editable": False} for i in df.columns

                        ],
                        data=df.to_dict('records'),
                        editable=False,
                        filter_action="native",
                        sort_action="native",
                        sort_mode='multi',

                        # style_as_list_view=True,

                        page_current=0,
                        column_selectable="multi",
                        page_size=10,

                        tooltip_data=[
                            {
                                column: {'value': str(value), 'type': 'markdown'}
                                for column, value in row.items()
                            } for row in df.to_dict('records')
                        ],
                        tooltip=
                        {i: {
                            'value': i,
                            'use_with': 'header'  # both refers to header & data cell
                        } for i in df.columns},
                        css=[{
                            'selector': '.dash-table-tooltip' ".show-hide" ".column-header--sort",

                            'rule': 'background-color: #3C3C46; font-family: monospace; max-width: 2px; display: none; float:right;'

                        }],
                        style_data={'color': 'black'},

                        style_header_conditional=[{
                            'if': {
                                'column_id': str(x),
                            },
                            'overflow': 'hidden', 'textOverflow':
                                'ellipsis'
                        } for x in df.columns
                        ],

                        style_header={
                            'textOverflow': 'ellipsis',
                            'textDecoration': 'underline',
                            'textDecorationStyle': 'dotted',
                            'maxWidth': 400,
                            'color': "#474777",
                            'fontWeight': 'bold'

                        },
                        style_filter={
                            'backgroundColor': 'white',

                            "fontSize": 20
                        },
                        style_data_conditional=[{

                            'backgroundColor': 'white',
                            'border': "1px solid #393E3E"

                        } for i in df.columns],

                        style_table={'height': 400, 'overflowX': 'auto', 'overflowY': 'auto',
                                     'borderRadius': '15px'},
                        style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'minWidth': 150, 'maxWidth': 400,
                                    'height': 25},
                        # style_data={"overflow": "hidden",
                        #             'textOverflow': 'ellipsis'}

                    ),
                    html.Br(),

                ])
            ), color='#EAE6EA', style={"borderRadius": "20px"},

        ),
        html.Br(),
        html.Br(),
        sunbrust_graph(dt=yt)
    ])


# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', port=8050, debug=True)
@app.callback(Output("sunbrust", "figure"),
              Input(component_id="Table", component_property="derived_virtual_data"))
def update_layout(value):
    dt = pd.DataFrame(value)
    if value is None or dt.shape[0] < 10:
        raise dash.exceptions.PreventUpdate
    else:

        print(dt.head())
        fig = px.sunburst(dt, color_discrete_sequence=px.colors.qualitative.D3, path=['category', "channel_title"],
                          values='views')
        fig.update_layout(margin=dict(t=40, b=40, l=0, r=0), plot_bgcolor='#673435',
                          paper_bgcolor='#EAE6EA')
        fig.update_traces(textinfo='label+percent parent')
    return fig
