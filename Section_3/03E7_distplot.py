#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.figure_factory as ff
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/iris.csv'

# create a DataFrame from the .csv file:
df = pd.read_csv(DATA_PATH)

# Define the traces

iris_types = ['Iris-setosa','Iris-versicolor','Iris-virginica']
hist_data = [df[df['class'] == iris_type]['petal_length'] for iris_type in iris_types]

# Define a data variable
fig = ff.create_distplot(hist_data, group_labels=iris_types, bin_size=0.2)
# Create a fig from data and layout, and plot the fig
pyo.plot(fig)
