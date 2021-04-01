import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import re

def search_words(text):
    result = re.findall(r'\w+', text)
    result = result[0:3]
    return " ".join(result)


def datef(x):
    l, m, n = x[0], x[1], x[2]
    x[0] = l
    x[1] = n
    x[2] = m
    return str("20" + x[0] + "-" + x[1] + "-" + x[2])


def clean_data(df):
    #   trending_date
    df['trending_date'] = df['trending_date'].str.replace(".", "-",regex=True)
    df['trending_date'] = df['trending_date'].str.split("-").apply(lambda x: datef(x))
    df['trending_date'] = pd.to_datetime(df['trending_date'])

    # yt['regular_date'] = yt['trending_date'].apply(lambda x: x.date())
    # publish_time
    df['publish_time'] = pd.to_datetime(df['publish_time'])

    # making object to numeric
    df['views'] = df['views'].astype('Int64')
    df['likes'] = df['likes'].astype('Int64')
    df['dislikes'] = df['dislikes'].astype('Int64')
    df['comment_count'] = df['comment_count'].astype('Int64')
    df['video_short_names'] = df['title'].apply(lambda x: search_words(x))

    return df
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


    return df_data

def most_views(df_data):
    df_data = df_data[df_data['trending_date'] == '2017-11-14']
    df_data = df_data.sort_values(by='views', ascending=False)[:10]

    df_data = df_data.sort_values(by='views')
    dt = df_data['trending_date'][0]
    return df_data