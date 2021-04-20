import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd
import pathlib
import calendar

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


df_long = pd.read_csv(DATA_PATH.joinpath("data.csv"))
df_long['Dates'] = pd.to_datetime(df_long.Dates, dayfirst=True)

monthly_df = df_long.groupby([df_long.Dates.dt.year, df_long.Dates.dt.month,df_long.States,df_long.Regions, df_long.latitude,df_long.longitude])['Usage'].mean()
monthly_df.index = monthly_df.index.set_names(['year', 'month','State','Region','latitude','longitude'])
monthly_df = monthly_df.reset_index()
monthly_df['month'] = monthly_df['month'].apply(lambda x: calendar.month_abbr[x])

fig = px.histogram(monthly_df, x='State', y='Usage',color='State',animation_frame = 'month')

layout = html.Div([
    html.H1('Power Usage during 2019', style={"textAlign": "center"}),

    dcc.Graph(id='histogram',
              config={'displayModeBar': True},
              animate=False,
              figure=fig)
])