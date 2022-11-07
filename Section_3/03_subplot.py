import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo

DATA_PATH_1 = '/home/variya/Development/UdemyDashCourse/Section_3/data/2010SitkaAK.csv'
DATA_PATH_2 = '/home/variya/Development/UdemyDashCourse/Section_3/data/2010SantaBarbaraCA.csv'
DATA_PATH_3 = '/home/variya/Development/UdemyDashCourse/Section_3/data/2010YumaAZ.csv'

df_1 = pd.read_csv(DATA_PATH_1)
df_2 = pd.read_csv(DATA_PATH_2)
df_3 = pd.read_csv(DATA_PATH_3)

trace_1 = go.Heatmap(x=df_1['DAY'], 
                     y=df_1['LST_TIME'], 
                     z=df_1['T_HR_AVG'],
                     zmin=5,
                     zmax=40,
                     colorscale='Jet')

trace_2 = go.Heatmap(x=df_2['DAY'], 
                     y=df_2['LST_TIME'], 
                     z=df_2['T_HR_AVG'],
                     zmin=5,
                     zmax=40,
                     colorscale='Jet')

trace_3 = go.Heatmap(x=df_3['DAY'], 
                     y=df_3['LST_TIME'], 
                     z=df_3['T_HR_AVG'],
                     zmin=5,
                     zmax=40,
                     colorscale='Jet')

fig = make_subplots(rows=1, cols=3,
                    subplot_titles=['Sitka AK', 'SB CA', 'Yuma AZ'],
                    shared_yaxes=False)

fig.append_trace(trace_1, 1, 1)
fig.append_trace(trace_2, 1, 2)
fig.append_trace(trace_3, 1, 3)

fig['layout'].update(title='Temps for 3 cities')

pyo.plot(fig)
