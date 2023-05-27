import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.io as pio

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

pd.set_option('display.max_columns', 15)
pf = df[df['Price Each'] > 600]

# fig1
pf = pf.groupby(['city', 'ord_date_day'], as_index=False).agg({'Quantity Ordered': sum})

pf.sort_values(by=['city', 'ord_date_day'], ascending=[True, True], inplace=True)

# fig2
# pf = pf.groupby(['Product', 'city'], as_index=False).agg({'Quantity Ordered': sum})
# colorscales = px.colors.named_colorscales()
# pf.sort_values(by='Quantity Ordered', ascending=True, inplace=True)
app = dash.Dash(__name__)
print(pf.head())

# fig1
# fig = px.bar(pf,
#              'city','Quantity Ordered',
#              color='Product',
#              barmode='relative',
#              # barmode='overlay'
#              # barmode='group',
#              facet_col='ord_date_day',
#              facet_col_wrap=5,
#              facet_col_spacing=0.01,
#              width=1200,
#              height=1000
#
#
#
#
#              )

# fig2
fig = px.bar(pf,
             'city', 'Quantity Ordered',
             barmode='relative',
             width=1200,
             height=800,
             text='Quantity Ordered',
             # labels={},
             template='ggplot2',
             animation_frame='ord_date_day',
             range_y=[0,20],
             category_orders={'ord_date_day':[i for i in range(1,32)]},
             color='city'
             # ['ggplot2', 'seaborn', 'simple_white', 'plotly',
             #  'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
             #  'ygridoff', 'gridon', 'none']

             # barmode='overlay'
             # barmode='group',

             )
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] =3000
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 3000

app.layout = html.Div([
    # html.P("Color Scale"),
    # dcc.Dropdown(
    #     id='colorscale',
    #     options=[{"value": x, "label": x}
    #              for x in colorscales],
    #     value='viridis'
    # ),
    # html.Br(),
    # html.Br(),
    dcc.Graph(id="bar", figure=fig)
])

# @app.callback(
#     Output("bar", "figure"),
#     [Input("colorscale", "value")])
# def change_colorscale(scale):
#     fig = px.bar(pf,
#                  'city', 'Quantity Ordered',
#                  color='Product',
#                  barmode='group',
#                  width=1200,
#                  height=600,
#
#
#                  # barmode='overlay'
#                  # barmode='group',
#
#                  )
#
#     return fig
#
#

