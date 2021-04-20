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


fig = px.scatter_geo(monthly_df,'latitude','longitude', color="Region",
                     hover_name="State", size="Usage",
                     animation_frame="month", scope='asia')
fig.update_geos(lataxis_range=[5,35], lonaxis_range=[65, 100])

layout = html.Div([
html.H1('Overall india Map visualization', style={"textAlign": "center"}),
dcc.Graph(id='geo_data',
          config={'displayModeBar': False},
          animate=True,
          figure = fig)
])

