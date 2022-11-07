import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/2010SantaBarbaraCA.csv'

df = pd.read_csv(DATA_PATH)

data = [go.Heatmap(x=df['DAY'], 
                   y=df['LST_TIME'], 
                   z=df['T_HR_AVG'],
                   colorscale='Jet')]

layout = go.Layout(title='SB CA Temps')

fig = go.Figure(data, layout)

pyo.plot(fig)
