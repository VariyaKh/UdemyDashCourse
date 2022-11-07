#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo


# create a DataFrame from the .csv file:
DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/mocksurvey.csv'

df = pd.read_csv(DATA_PATH, index_col=0)

# create traces using a list comprehension:
answers = ['Strongly Agree', 'Somewhat Agree', 'Neutral', 'Somewhat Disagree', 'Strongly Disagree']
data = [go.Bar(y=df.index, x=df[answer], orientation='h', name=answer) for answer in answers]

layout = go.Layout(title='Survay result', barmode='stack')

fig = go.Figure(data, layout=layout)

pyo.plot(fig)





# create a layout, remember to set the barmode here





# create a fig from data & layout, and plot the fig.
