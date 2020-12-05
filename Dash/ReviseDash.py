
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
m = {'width': '25%',
     'display': 'inline-block',
     'background-color': ' #4E387E',
     'padding-top': '25px',
     'padding-right': '10px',
     'padding-bottom': '10px',
     'padding-left': '10px'}

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# x = np.random.normal(3, 6, 100)
#
# fig1 = px.histogram(x=x)

# print(fig.show())
# print(df.head())
app.layout = html.Div(children=[
    html.H1(children='Hello Dash Nik'),

    html.Br(),
    html.Div(["Input Mean "]),
    html.Div([
        dcc.Slider(id='mean_slider',
                   min=1,
                   max=120,
                   step=1,
                   value=4,
                   marks={
                       1: {'label': 'Min=1 ', 'style': {'color': '#77b0b1'}},

                       120: {'label': 'Max=120', 'style': {'color': '#77b0b1'}}}
                   ),

    ], style=m),
    html.Br(),

    html.Div(id='slider-output-container'),
    html.Br(),
    html.Div(["Input std "]),
    html.Div([
        dcc.Slider(id='std_slider',
                   min=0,
                   max=12,
                   step=1,
                   value=4,
                   marks={
                       0: {'label': 'Min=0', 'style': {'color': '#77b0b1'}},

                       12: {'label': 'Max=12', 'style': {'color': '#77b0b1'}}}
                   ),

    ], style=m),
    html.Br(),
    html.Div(id='slider-output-container2'),

    html.Br(),

    dcc.Graph(
        id='histogram_slider'),

    html.Div([
           dcc.Dropdown(
                        id='city',
                        value='SF',
                        options=[
                            {'label': 'Montreal', 'value': 'Montreal'},
                            {'label': 'SF', 'value': 'SF'},

                          ],
                        multi=True,
                        placeholder="Select a city"
                        )
           ]),
    html.Div(id='dd-output-container')

])


@app.callback([Output('slider-output-container', 'children'),
               Output('slider-output-container2', 'children'),
               Output(component_id='histogram_slider', component_property='figure'),

               ],

              [Input(component_id='mean_slider', component_property='value'),
               Input(component_id='std_slider', component_property='value')])
def update_output(*value):
    x = np.random.normal(value[0], value[1], 1000)
    fig2 = px.histogram(x)

    return f'selected mean:= {value[0]}', f'selected std:= {value[1]}', fig2


@app.callback(Output('dd-output-container', 'children'),
              [Input('city', 'value')]

              )
def update_output(value):
    return df.to_json(
    )

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8051, debug=True)
#     [
#         Output(component_id='histogram', component_property='figure'),
#         Output(component_id='example-graph', component_property='figure')],
#     [Input(component_id='my_input_mean', component_property='value')]
# )
# def update_output_div(input_value):
#     x = np.random.normal(input_value, 6, 100)
#
#     fig1 = px.histogram(x=x)
#
#     return fig1, fig
#

# def run_server(self,
#                port=8051,
#                debug=True,
#                **flask_run_options):
#     self.server.run(port=port, debug=debug, **flask_run_options)
#

