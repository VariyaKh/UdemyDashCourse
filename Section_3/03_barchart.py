import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/2018WinterOlympics.csv'

df = pd.read_csv(DATA_PATH)

medals = ['Gold', 'Silver', 'Bronze']
colors ={'Gold': '#FFD700', 'Silver': '#9EA0A1', 'Bronze': '#CD7F32'}

data = [go.Bar(x=df['NOC'], y=df[medal], name=medal, marker=dict(color=colors[medal])) for medal in medals]
layout = go.Layout(title='Winter olimpic medals in 2018')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)