#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo



# create a DataFrame from the .csv file:
DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/mpg.csv'

df = pd.read_csv(DATA_PATH, na_values={'horsepower':'?'})
print(df.origin.unique())

# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(x=df['mpg'],
                   y=df['acceleration'],
                   mode='markers',
                   marker_symbol='circle-open',
                   marker=dict(size=df['displacement']/7,
                               color=df['origin'],
                               showscale=True,
                               line={'width': 4})
                               )
                ]

# create a layout with a title and axis labels
layout = go.Layout(title='Scatter plot',
                    xaxis={'title': 'Acceleration'},
                    yaxis=dict(title='MPG'),
                    hovermode='closest')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data, layout=layout)

pyo.plot(fig)
