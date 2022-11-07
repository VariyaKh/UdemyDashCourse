#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo



# Define a data variable
x_random = np.random.randn(1000)
y_random = np.random.rand(1000)


data = [go.Scatter(x=x_random, y=y_random, mode='markers')]

# Define the layout

layout = go.Layout(title='Scatter plot')

# Create a fig from data and layout, and plot the fig

fig = go.Figure(data, layout=layout)

pyo.plot(fig)
