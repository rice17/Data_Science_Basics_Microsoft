import pandas as pd
import os
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
#colors list will store colors for data from respective directories
colors = []
#samples list will store names of files
samples = []

#change working directory to read blue data file names
os.chdir('/home/abhishar/Desktop/DatS/DAT210x-master/Module4/Datasets/ALOI/32')
for files in os.listdir('.'):
    if os.path.isfile(files):
        samples.append('32/'+files)
        colors.append('b')
    
#change working directory to read red data file names
os.chdir('/home/abhishar/Desktop/DatS/DAT210x-master/Module4/Datasets/ALOI/32i')
for files in os.listdir('.'):
    if os.path.isfile(files):
        samples.append('32i/'+files)
        colors.append('r')
        
#change working directory so that the program can read both red and blue files from name
os.chdir('/home/abhishar/Desktop/DatS/DAT210x-master/Module4/Datasets/ALOI')
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here 
array = []
for f in samples:
    img = misc.imread(f)
    img = img.reshape(-1)
    array.append(img)
data = pd.DataFrame(data = array)
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 

#Isomap
from sklearn import manifold
iso = manifold.Isomap(n_neighbors = 5, n_components = 3)
iso.fit(data)
imap = iso.transform(data)
isomap = pd.DataFrame(data=imap)
plt.scatter(isomap[0], isomap[1], c = colors)

"""
#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 3)
pca.fit(data)
X = pca.transform(data)
T = pd.DataFrame(data = X)
plt.scatter(T[0], T[1], c = colors)
"""
#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 

isomap.columns = ['x', 'y', 'z']
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(isomap.x, isomap.y, isomap.z,
          c=colors, marker='o', alpha=0.75)
plt.show()

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

