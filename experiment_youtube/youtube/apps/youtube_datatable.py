import pathlib

import dash
import dash_html_components as html
import dash_table
import pandas as pd

from filtter_data import clean_data

pd.set_option('display.max_columns', 30)
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
app = dash.Dash(__name__)
yt = pd.DataFrame()
for chunk in pd.read_csv(DATA_PATH.joinpath("CAvideos1.csv"), chunksize=10000):
    yt = pd.concat([yt, chunk])
    break
df=yt.copy()


layout = html.Div([

    dash_table.DataTable(
        id='Table',

        columns=[
            {"name": i, "id": i, "hideable": True, "editable": False, "selectable": True} for i in df.columns

        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
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
            'selector': '.dash-table-tooltip',

            'rule': 'background-color: white; font-family: monospace; max-width: 2px;'
        }],

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
             'maxWidth': 400
        },

        style_table={'height': 400, 'overflowX': 'auto', 'overflowY': 'auto'},
        style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'minWidth': 150, 'maxWidth': 300,
                    'height':25},
        # style_data={"overflow": "hidden",
        #             'textOverflow': 'ellipsis'}

    ),

])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)
