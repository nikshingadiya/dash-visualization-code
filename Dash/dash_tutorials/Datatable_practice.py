import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import seaborn as sns

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
            {'id': c, 'name': c, 'editable': True, "selectable": True, 'hideable': True}
            for c in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        page_current=0,
        page_size=10,
        style_table={'height': 400, 'overflowX': 'auto', 'overflowY': 'auto'},
        style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'whiteSpace': 'normal'},

    )
])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050, debug=True)
