import dash_core_components as dcc
import dash_html_components as html
import pathlib

import pandas as pd

import plotly.express as px

import calendar

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data2.csv"))
df_long = pd.read_csv(DATA_PATH.joinpath("data.csv"))
df['Date'] = pd.to_datetime(df.Date, dayfirst=True)
df_long['Dates'] = pd.to_datetime(df_long.Dates, dayfirst=True)

monthly_df = df_long.groupby([df_long.Dates.dt.year, df_long.Dates.dt.month,df_long.States,df_long.Regions, df_long.latitude,df_long.longitude])['Usage'].mean()
monthly_df.index = monthly_df.index.set_names(['year', 'month','State','Region','latitude','longitude'])
monthly_df = monthly_df.reset_index()
monthly_df['month'] = monthly_df['month'].apply(lambda x: calendar.month_abbr[x])

fig = px.bar(monthly_df, x="State", y="Usage",color='Region',animation_frame = 'month')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(title='Region-wise Bar plots')

layout = html.Div([
    html.H1('Moving Bar chart visualization', style={"textAlign": "center"}),

    dcc.Graph(id='timeseries',
              config={'displayModeBar': False},
              animate=True,
              figure=fig)
])
