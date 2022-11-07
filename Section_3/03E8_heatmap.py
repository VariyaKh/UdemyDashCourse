#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/flights.csv'
# Create a DataFrame from  "flights" data
df = pd.read_csv(DATA_PATH)

# Define a data variable
data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'])]

# Define the layout
layout = go.Layout(title='Flights')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data, layout)

pyo.plot(fig)
