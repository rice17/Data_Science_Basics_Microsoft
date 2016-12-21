import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves
# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
data = pd.read_csv("/home/abhishar/Desktop/DatS/DAT210x-master/Module3/Datasets/wheat.data")


#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..

data = data.drop(axis = 1, labels = ['id', 'area', 'perimeter'])


#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
plt.figure()
andrews_curves(data, 'wheat_type', alpha = 0.4)
plt.show()


