#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/abalone.csv'

df = pd.read_csv(DATA_PATH)

# take two random samples of different sizes:
sample_1 = df['rings'].sample(n=1000, replace=False, random_state=43)
sample_2 = df['rings'].sample(n=1000, replace=False, random_state=101)

# create a data variable with two Box plots:
data = [go.Box(y=sample_1, boxpoints='all', jitter=0.4, pointpos=-1, name='Sample 1'), 
        go.Box(y=sample_2, boxpoints='all', jitter=0.4, pointpos=-1, name='Sample 2')]

# add a layout

layout = go.Layout(title='Box plot')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data, layout=layout)

pyo.plot(fig)