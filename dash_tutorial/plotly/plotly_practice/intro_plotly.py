
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv("../Dataset/Sales_April_2019.csv").dropna()


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


"""['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'ord_time',
       'ord_date_day', 'ord_date_month', 'area_in_city', 'city', 'state_zip']"""
df = cleaning_data(df)


app = dash.Dash(__name__)
fig = px.pie(df, values='Quantity Ordered', names='Product',hole=0.3)
fig.update_traces(textinfo='percent', textfont_size=15,insidetextfont=dict(color='blue'))
fig.update_layout(legend={"itemclick":False})
app.layout = html.Div([

    dcc.Graph(id="pie", figure=fig

              )
])

