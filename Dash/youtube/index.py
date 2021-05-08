import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main tree.py file
from app import app
# Connect to your app pages
from apps import bar_youtube
from apps import  youtube_datatable
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('   Youtube DataTable|', href='/apps/youtube_datatable'),
        dcc.Link('   Youtube', href='/apps/bar_youtube'),
    ], className="row",style={'marginLeft': 25, 'marginTop': 0}),
    html.Div(id='page-content', children=[]),

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/youtube_datatable':
        return youtube_datatable.layout
    if pathname == '/apps/bar_youtube':
        return bar_youtube.layout
    else:
        return youtube_datatable.layout



if __name__ == '__main__':
    app.run_server(port=9099, debug=True, dev_tools_ui=True)
