import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash import Dash
from dash.dependencies import Input, Output

import  numpy as np
import  matplotlib.pylab as plt
import  plotly.graph_objs as go

import plotly.offline as pyo
# df = pd.read_csv('C:/Users/nikhil/Documents/GitHub/jupyter/data/terrorismData.csv').dropna()
#
# pd.set_option("display.max_columns", 20)
# l1=list(df.Country.unique())


 # define flask app.server

app = dash.Dash(__name__) # call flask server


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#############################################################################
app.layout = html.Div(children=[
    html.Div(["Input: ",
              dcc.Input(id='my-input', value='initial value', type= "text")]),
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure='figure'
    ),

    dcc.Graph(
        id='numpy-fig'
    ),
    html.Div(["Input-data: ",
              dcc.Input(id='data-point', value=10, type="number")]),
html.Div(id='my-output')
])
##############################################################################
@app.callback(
    [Output(component_id='my-output', component_property='children'),
     Output(component_id='numpy-fig', component_property='figure'),
     Output(component_id='example-graph', component_property='figure')],
    [Input(component_id='my-input', component_property='value'),
     Input(component_id="data-point", component_property='value')]
)
def update_output_div(input_value,input_value2=10):
    # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    data=[go.Scatter(x=df['Fruit'],y=df["Amount"],mode='markers')]
    layout=go.Layout(title="fruit_amount",xaxis={'title':'Fruit'},yaxis={'title':'Amount'})
    fig=go.Figure(data,layout)
    random_x = np.random.randint(1, 101, (input_value2))
    random_y = np.random.randint(1, 101, (input_value2))
    data1=[go.Scatter(x=random_x,y=random_y,mode='markers',
                      marker=dict(size=12,
                                  color='rgb(51,100,251)',
                                  symbol= 'diamond',
                                  line={'width':2})
                      )]
    layout1=go.Layout(title="numpy-fig",xaxis=dict(title="x_value"),yaxis=dict(title="y_value"), height=700)
    fig1=go.Figure(data1,layout1)
    fig1.update_layout(transition_duration=500)
    return 'Output: {}'.format(input_value),fig1,fig



