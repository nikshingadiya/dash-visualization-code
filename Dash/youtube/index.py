import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
# Connect to your app pages
from apps import vgames, bar_youtube

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Video Games|', href='/apps/vgames'),
        dcc.Link('Youtube', href='/apps/bar_youtube'),
    ], className="row"),
    html.Div(id='page-content', children=[]),

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/vgames':
        return vgames.layout
    if pathname == '/apps/bar_youtube':
        return bar_youtube.layout
    else:
        return bar_youtube.layout


#
# if __name__ == '__main__':
#     app.run_server(port=8083, debug=True, dev_tools_ui=True)
