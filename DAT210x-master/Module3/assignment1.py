import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
data = pd.read_csv('/home/abhishar/Desktop/DatS/DAT210x-master/Module3/Datasets/wheat.data')

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
# .. your code here ..
s1 = data.loc[:, ['area', 'perimeter']]

#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
# .. your code here ..
s2 = data.loc[:, ['groove', 'asymmetry']]
s3 = data.loc[:, ['compactness', 'width']]
#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..
s1.plot.scatter(x='area', y='perimeter')
plt.show()
s2.plot.scatter(x='groove', y='asymmetry')
plt.show()
s3.plot.scatter(x='compactness', y='width')
plt.show()

