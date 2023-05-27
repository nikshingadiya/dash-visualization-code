import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
app=dash.Dash(__name__)
import pandas as pd
import plotly.express as px
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
app = dash.Dash(__name__)
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
print(fig.show())
print(df.head())
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application. mnikNikhil
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])



# if __name__ == '__main__':
#     app.run_server(debug=True)