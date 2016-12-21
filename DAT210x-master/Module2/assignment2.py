import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
data = pd.read_csv("/home/abhishar/Desktop/DatS/DAT210x-master")


# TODO: Print the results of the .describe() method
#
# .. your code here ..
print(data.describe())


# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print(data.loc[2:4, 'col3'])
