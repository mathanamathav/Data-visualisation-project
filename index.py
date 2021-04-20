import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from apps import chart1,chart2,chart3,chart4,chart5,chart6,startpage


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Welcome page | ', href='/apps/welcomepage'),
        dcc.Link('Line Chart | ', href='/apps/line_chart'),
        dcc.Link('Histogram chart | ', href='/apps/line_chart2'),
        dcc.Link('Box Chart | ', href='/apps/MovingChart'),
        dcc.Link('Bar Chart | ', href='/apps/MovingChart1'),
        dcc.Link('Map Chart | ', href='/apps/MovingChart2'),
        dcc.Link('Heatmap Chart | ', href='/apps/heat_chart'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/welcomepage':
        return startpage.layout
    if pathname == '/apps/line_chart':
        return chart1.layout
    if pathname == '/apps/line_chart2':
        return chart2.layout
    if pathname == '/apps/MovingChart':
        return chart3.layout
    if pathname == '/apps/MovingChart1':
        return chart4.layout
    if pathname == '/apps/MovingChart2':
        return chart5.layout
    if pathname == '/apps/heat_chart':
        return chart6.layout
    else:
        return startpage.layout


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)