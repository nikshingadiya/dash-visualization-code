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
import plotly.figure_factory as ff
import plotly.offline as pyo
import seaborn as sns
df = pd.read_csv('C:/Users/nikhil/Documents/GitHub/jupyter/data/terrorismData.csv').dropna()
fig= px.choropleth(df,
                  )
pyo.plot(fig, filename='Map1_Interactive.html')