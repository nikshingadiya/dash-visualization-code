import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from youtube.flask_failsafe import failsafe


@failsafe
def create_app():
    # from Scatter3D import app
    from youtube.bar_youtube import app
    return app.server


if __name__ == "__main__":
    # app.server is the underlying flask app
    create_app().run(port="8052", debug=True)


