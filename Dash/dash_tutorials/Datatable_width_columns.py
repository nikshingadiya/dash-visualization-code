import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

pd.set_option('display.max_columns', 12)

app = dash.Dash(__name__)
df = pd.read_csv("Dataset/Sales_April_2019.csv").dropna()
app.layout = html.Div([
    dash_table.DataTable(
        id='Table',
        columns=[
            {'id': c, 'name': c, 'editable': True, "selectable": True, 'hideable': True}
            for c in df.columns
        ],

        data=df.to_dict('records'),
        editable=True,
        column_selectable='multi',
        filter_action="native",
        # style_as_list_view=True,
        sort_action="native",
        # sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        # selected_rows=[],
        # page_action='native',
        # markdown_options={'link_target': '_parent'},
        page_current=0,
        page_size=10,

        #
        # style_header={'font-size': '14px', 'padding': '2px 22px', 'span': '13px',
        #               'fontWeight': 'bold', 'margin': '5px',
        #               'margin-bottom': '1.5em'},

        # style_data={'border': '#393E3', 'backgroundColor': '#393E3E ','color':'#D0D3D4'},
        # style_data={'whitespace': 'normal', 'height': 'auto', 'overflowY': 'auto'},
        # style_data={'overflowY': 'hidden', 'maxWidth': 0, 'textOverflow': 'ellipsis'},

        style_table={'overflowX': 'Scroll'},
        # fixed_columns={'headers': True, 'data': 1},
        # style_cell={'height': 'auto',
        #             'minWidth': '180px', 'width': '180px',
        #             'maxWidth': '180px',
        #             'whiteSpace': 'normal'
        #             }

        # style_data_conditional=[ {
        #     'if': {
        #         'column_id': str(x),
        #     },
        #     'backgroundColor': 'dodgerblue',
        #     'color': 'white' } for x in [ y for y in df.columns if y in ['country','year'] ]
        # ]


)

])


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8055, debug=True)



