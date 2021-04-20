import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data.csv"))
df['Dates'] = pd.to_datetime(df.Dates, dayfirst=True)

states_list = ['Tamil Nadu', 'Punjab', 'Rajasthan','Kerala','Karnataka']

layout = html.Div([
    html.H1('Line chart', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='states-dropdown', value='Tamil Nadu', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in states_list]
        ), className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-chart', figure={}),

    html.Div([
        html.P('')
    ])
])


@app.callback(
    Output(component_id='my-chart', component_property='figure'),
    [Input(component_id='states-dropdown', component_property='value')]
)
def build_graph(states_dropdown):
    df_filtered = df[df['States'] == states_dropdown]
    fig = px.line(df_filtered, x='Dates', y='Usage')
    return fig
