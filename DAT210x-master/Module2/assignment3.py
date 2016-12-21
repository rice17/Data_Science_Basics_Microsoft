import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#motor screw pgain vgain class
# .. your code here ..
data = pd.read_csv("/home/abhishar/Desktop/DatS/DAT210x-master/Module2/Datasets/servo.data")

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#27
# .. your code here ..
sub1 = data[data[3] == 5]

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#6
# .. your code here ..
sub2 = data[(data[0] == 'E') & (data[1] == 'E')]


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#2.0606060606060606
# .. your code here ..
sub3 = data[data[2] == 4]
mean4 = sub3[3].mean()
print(mean4)
# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
data.dtypes
sub1.dtypes


