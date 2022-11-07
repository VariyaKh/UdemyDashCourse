import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

DATA_PATH = '/home/variya/Development/UdemyDashCourse/Section_3/data/nst-est2017-alldata.csv'

df = pd.read_csv(DATA_PATH)
df.set_index('NAME', inplace=True)

pop_columns = [col for col in df.columns if col.startswith('POP')]
df_2 = df[df['DIVISION'] == '1'][pop_columns].copy()

data = [go.Scatter(x=df_2.columns,
                   y=df_2.loc[name],
                   mode='lines',
                   name=name) for name in df_2.index]

pyo.plot(data)
