# -*- coding: utf-8 -*-

#importing required libraries
import pandas as pd
import numpy as np


#Loading the parkinsons data
data = pd.read_csv("/home/abhishar/Desktop/DatS/DAT210x-master/Module6/Datasets/parkinsons.data")

#Droping name column
data = data.drop("name", axis = 1)

#Separating status
status = data['status']
data = data.drop('status', axis = 1)


#Spliting the data for training and testing
from sklearn.cross_validation import train_test_split
train_data, test_data, train_status, test_status = train_test_split(data, status, random_state = 7, test_size = 0.3)


#Scaling features using StandardScalar as it is found to be best based
# on trail and error
from sklearn.preprocessing import StandardScaler
scaling = StandardScaler()
scaling.fit(train_data)
train_data = scaling.transform(train_data)
test_data = scaling.transform(test_data)


#Reducing dimensions ...
"""
from sklearn.decomposition import PCA
pca = PCA(n_components = 14)
pca.fit(train_data)
train_data = pca.transform(train_data)
test_data = pca.transform(test_data)
"""
from sklearn.manifold import Isomap
isomap = Isomap(n_neighbors = 2, n_components = 6)
isomap.fit(train_data)
train_data = isomap.transform(train_data)
test_data = isomap.transform(test_data)


#Importing SVC
from sklearn.svm import SVC

#Trying various combination for C and gamma for best model
max_score = 0

for C in range(5, 200, 5):
	for gamma in range(1, 100, 1):
		model = SVC(C = float(C)/100, gamma = float(gamma)/1000)
		model.fit(train_data, train_status)
		score = model.score(test_data, test_status)
		if score>max_score:
			max_score = score

print max_score
