import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
data = pd.read_csv('/home/abhishar/Desktop/DatS/DAT210x-master/Module3/Datasets/wheat.data')

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..
data = data.drop(axis = 1, labels = ['id'])

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
correlation_matrix = data.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(correlation_matrix, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(data.columns))]
plt.xticks(tick_marks, data.columns, rotation='vertical')
plt.yticks(tick_marks, data.columns)

plt.show()



