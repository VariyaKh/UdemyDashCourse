#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/2010YumaAZ.csv'

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv(DATA_PATH)
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
data = [go.Scatter(x=df[df['DAY'] == day]['LST_TIME'],
                    y=df[df['DAY'] == day]['T_HR_AVG'], mode='lines', name=day) for day in days]

# Define the layout

layout = go.Layout(title='Temperature by days')


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data, layout=layout)

pyo.plot(fig)
