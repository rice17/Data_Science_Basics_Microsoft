import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper

matplotlib.style.use('ggplot')

scaleFeatures = False

data = pd.read_csv('/home/abhishar/Desktop/DatS/DAT210x-master/Module4/Datasets/kidney_disease.csv')

data = data.dropna(axis = 0)

labels = ['red' if i=='ckd' else 'green' for i in data.classification]

data = data.drop(labels = ['id', 'classification'], axis = 1)

data.wc = pd.to_numeric(data.wc, errors = 'coerce')
data.rc = pd.to_numeric(data.rc, errors = 'coerce')

#nominal features
nominal = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
data = pd.get_dummies(data, columns = nominal)
#name adjustment
if scaleFeatures: data = helper.scaleFeatures(data)
#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(data)
PCA(copy=True, n_components=2, whiten=False)
T = pca.transform(data) 

ax = helper.drawVectors(T, pca.components_, data.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()