import numpy as np
import scipy 
import plotly.offline as pyo
import plotly.figure_factory as ff

x_1 = np.random.randn(200) - 2
x_2 = np.random.randn(200)
x_3 = np.random.randn(200) + 2
x_4 = np.random.randn(200) + 4

hist_data = [x_1, x_2, x_3, x_4]
group_labeles = ['x_1', 'x_2', 'x_3', 'x_4']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labeles, bin_size=[.2, .1, .3, .4])
pyo.plot(fig)