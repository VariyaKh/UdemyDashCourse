import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/mpg.csv'

df = pd.read_csv(DATA_PATH, na_values={'horsepower':'?'})

data = [go.Scatter(x=df['horsepower'],
                  y=df['mpg'],
                  text=df['name'],
                  mode='markers',
                  marker_symbol='circle-open',
                  marker=dict(size=df['weight']/120,
                              color=df['cylinders'],
                              showscale=True,
                              line={'width': 4}))]

layout = go.Layout(title='Bubble chart')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
