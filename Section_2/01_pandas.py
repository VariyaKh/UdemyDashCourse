import pandas as pd

PATH = '/home/variya/Development/Plotly-Dashboards-with-Dash/0-02-Pandas-Crash-Course/salaries.csv'

df = pd.read_csv(PATH)

print(df)

print(df['Salary'])