import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/mpg.csv'

df = pd.read_csv(DATA_PATH)

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=2))]
layout = go.Layout(title='Histogram')
fig = go.Figure(data, layout)
pyo.plot(fig)