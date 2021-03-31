import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

def top_treanding(df=None):
    df['likes'] = df['likes'] + 1
    df['likes/views'] = df['likes'] / df['views']
    df['likes/views'] = df['likes/views'].apply(lambda x: round(x, 3))
    df = df[df['likes/views'] > 0.1]

    df = df.sort_values(['trending_date', 'likes/views'], ascending=[True, True])
    df['t_date'] = df['trending_date'].astype(str)
    return df

def most_likes(df_data):
    df_data = df_data[df_data['trending_date'] == '2017-11-14']
    df_data = df_data.sort_values(by='likes', ascending=False)[:10]
    df_data = df_data.sort_values(by='likes')
    dt = df_data['trending_date'][0]

    return df_data

def most_views(df_data):
    df_data = df_data[df_data['trending_date'] == '2017-11-14']
    df_data = df_data.sort_values(by='views', ascending=False)[:10]

    df_data = df_data.sort_values(by='views')
    dt = df_data['trending_date'][0]
    return df_data