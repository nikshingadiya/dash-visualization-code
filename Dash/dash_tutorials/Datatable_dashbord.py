import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import seaborn as sns
from plotly.subplots import make_subplots
app = dash.Dash(__name__)
df = pd.read_csv("Dataset/Sales_April_2019.csv").dropna()


# data cleaning


def cleaning_data(df):
    df = df.dropna()

    # cleaning column and seperate appropriate colums
    i = df[df['Quantity Ordered'] == 'Quantity Ordered'].index
    # here we look df['Quantity Ordered'].unique() we find  'Quantity Ordered' so it's noise (order id etc in row)
    df.drop(i, axis=0, inplace=True)

    # convert to object to int or float respectivly columns
    df['Quantity Ordered'] = df['Quantity Ordered'].astype(float)
    df['Price Each'] = df['Price Each'].astype(float)

    # seperate columns time or date from orderdate
    df['Order Date'] = df['Order Date'].str.split(' ')
    df['ord_date'] = df['Order Date'].apply(lambda x: x[0])  # date
    df['ord_time'] = df['Order Date'].apply(lambda x: x[1])  # time
    df['ord_date_day'] = df['ord_date'].str.split('/').apply(lambda x: int(x[1]))  # day

    df['ord_date_month'] = df['ord_date'].str.split('/').apply(lambda x: int(x[0]))  # month

    # time convert minute to hour
    df['ord_time'] = df['ord_time'].str.split(':').apply(lambda x: round(float(x[0]) + float(x[1]) / 60, 2))
    # now we seperate address columns
    df['Purchase Address'] = df['Purchase Address'].str.split(',')
    df['area_in_city'] = df['Purchase Address'].apply(lambda x: x[0])  # area and street
    df['city'] = df['Purchase Address'].apply(lambda x: x[1])  # city
    df['state_zip'] = df['Purchase Address'].apply(lambda x: x[2])  # stae_zip

    df.drop(axis=1, columns=['Purchase Address', 'Order Date', 'ord_date'], inplace=True)
    return df


df = cleaning_data(df)

app.layout = html.Div([
    dash_table.DataTable(
        id='Table',

        columns=[
            {"name": i, "id": i, "hideable": True, "editable": True, "selectable": True} for i in df.columns

        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        page_current=0,
        column_selectable="multi",
        page_size=10,
        style_header={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'whiteSpace': 'normal', 'span': '13px'},
        style_table={'height': 400, 'overflowX': 'auto', 'overflowY': 'auto'},
        style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'minWidth': '0px', 'width': '0px', 'maxWidth': '0px'},
        # style_data={"overflow": "hidden", 'border': '#393E3', 'backgroundColor': '#393E3E ', 'color': '#D0D3D4',
        #             'span': '13px'}

    ),
    html.Br(),
    html.Br(),
    html.Br(),

    # dcc.Graph(id="hist",figure=px.histogram(df,"Quantity Ordered"))
    dcc.Graph(id="bar")

])


@app.callback(Output(component_id="bar", component_property="figure"),
              Input(component_id="Table", component_property="derived_virtual_data"))
def update_layout(value):
    if value is None:
        raise dash.exceptions.PreventUpdate
    else:
        # dt = pd.DataFrame(value)
        # print(dt.head())
        # dt = dt.groupby('city', as_index=False).agg({'Quantity Ordered': sum})
        # dt = dt.sort_values(by='Quantity Ordered')
        # fig = px.bar(dt, x='city', y='Quantity Ordered', color="Quantity Ordered", text='Quantity Ordered',width=800, height=500)
        # fig.update_traces(texttemplate='%{text:.2s}', textposition='outside' )

        fig = make_subplots(
            rows=1, cols=2,horizontal_spacing=0.1)
        dt = pd.DataFrame(value)
        print(dt.head())
        for j,i in enumerate(['city','state_zip']):
            dk = dt.groupby(i, as_index=False).agg({'Quantity Ordered': sum})
            dk = dk.sort_values(by='Quantity Ordered')

            fig1=px.bar(dk, x=i, y='Quantity Ordered', color="Quantity Ordered", text='Quantity Ordered')

            fig1.update_xaxes(title_text=i, row=1, col=j)
            fig1.update_yaxes(title_text="Quantity Ordered", row=1, col=j)

            fig.add_trace(fig1.data[0],row=1,col=j+1)

        fig.update_xaxes(title_text="city", row=1, col=1)
        fig.update_yaxes(title_text="Quantity Ordered", row=1, col=1)

        fig.update_xaxes(title_text="state_zip", row=1, col=2)
        fig.update_yaxes(title_text="Quantity Ordered", row=1, col=2)

        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(height=600, width=1200, title_text="Stacked Subplots")

    # fig= px.histogram(dt["Quantity Ordered"])
    return fig


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)
