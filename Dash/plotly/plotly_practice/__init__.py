import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from flask_failsafe import failsafe


@failsafe
def create_app():
    # note that the import is *inside* this function so that we can catch
    # errors that happen at import time
    # from intro_plotly  import  app
    # from bar_plotly import app
    # from Datatable_dashbord import app
    # from sunbrust import  app

    from Scatter3D import app
    return app.server


if __name__ == "__main__":
    # app.server is the underlying flask app
    create_app().run(port="8052", debug=True)


