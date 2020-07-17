pip install .
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly


import pandas as pd
import numpy as np
from datetime import datetime
from scipy.interpolate import interp1d

import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__)

death =  pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

death.rename(columns={'Country/Region': 'Country'}, inplace=True)
confirmed.rename(columns={'Country/Region': 'Country'}, inplace=True)
recovered.rename(columns={'Country/Region': 'Country'}, inplace=True)
country.rename(columns={'Country_Region': 'Country', 'Long_': 'Long'}, inplace=True)

death.drop('Province/State', axis=1, inplace=True)
confirmed.drop('Province/State', axis=1, inplace=True)
recovered.drop('Province/State', axis=1, inplace=True)
country.drop(['People_Tested','People_Hospitalized'],axis=1, inplace=True)

country['Confirmed']=country['Confirmed'].astype(int)
country['Deaths']=country['Deaths'].astype(int)
country['Active']=country['Active'].astype(int)

country.sort_values('Confirmed', ascending=False, inplace=True)

# fixing the size of circle to plot in the map

margin = country['Confirmed'].values.tolist()
circel_range = interp1d([1, max(margin)], [0.2,12])
circle_radius = circel_range(margin)

# main layout for Dash


          
 

# global map heading

global_map_heading = html.H2(children='World map view', className='mt-5 py-4 pb-3 text-center')

# ploting the map
map_fig = px.scatter_mapbox(country, lat="Lat", lon="Long", hover_name="Country", hover_data=["Confirmed", "Deaths"],
                        color_discrete_sequence=["#e60039"], zoom=2, height=500, size_max=50, size=circle_radius)

map_fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0}, height=520)

app.layout =  html.Div(children = [global_map_heading,
         dcc.Graph(
             id='global_graph',
             figure=map_fig
         )
        ]
      )    
     

# start the server

server = app.server

if __name__ == '__main__':
    app.run_server()
