import pandas as pd
import time

# Grab the DLA HAR dataset from:
# http://groupware.les.inf.puc-rio.br/har
# http://groupware.les.inf.puc-rio.br/static/har/dataset-har-PUC-Rio-ugulino.zip


#
# TODO: Load up the dataset into dataframe 'X'
#
# .. your code here ..
X = pd.read_csv("/home/abhishar/Desktop/DatS/DAT210x-master/Module6/Datasets/dataset-har-PUC-Rio-ugulino.csv", delimiter = ";")


#
# TODO: Encode the gender column, 0 as male, 1 as female
#
# .. your code here ..
X.gender = X.gender.map({"Man":0, "Woman":1})

#
# TODO: Clean up any column with commas in it
# so that they're properly represented as decimals instead
#
# .. your code here ..
X.how_tall_in_meters = X.how_tall_in_meters.replace(",", ".", regex = True)
X.body_mass_index = X.body_mass_index.replace(",", ".", regex = True)

X = X.drop(X.index[[122076]], axis = 0)
#
# INFO: Check data types
print X.dtypes



#
# TODO: Convert any column that needs to be converted into numeric
# use errors='raise'. This will alert you if something ends up being
# problematic
#
# .. your code here ..
X.z4 = pd.to_numeric(X.z4, errors = "raise")
X.body_mass_index = pd.to_numeric(X.body_mass_index, errors = "raise")
X.how_tall_in_meters = pd.to_numeric(X.how_tall_in_meters, errors = "raise")
#
# INFO: If you find any problematic records, drop them before calling the
# to_numeric methods above...


#
# TODO: Encode your 'y' value as a dummies version of your dataset's "class" column
#
# .. your code here ..
y = pd.get_dummies(X['class'])

#
# TODO: Get rid of the user and class columns
#
# .. your code here ..
X = X.drop(axis = 1, labels = ['class', 'user'])
print X.describe()


#
# INFO: An easy way to show which rows have nans in them
print X[pd.isnull(X).any(axis=1)]



#
# TODO: Create an RForest classifier 'model' and set n_estimators=30,
# the max_depth to 10, and oob_score=True, and random_state=0
#
# .. your code here ..
from sklearn.ensemble import RandomForestClassifier as RForest
model = RForest(n_estimators = 30, max_depth = 10, oob_score = True, random_state = 0)

#
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
# .. your code here ..
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 7, test_size = 0.3)


print "Fitting..."
s = time.time()
#
# TODO: train your model on your training set
#
# .. your code here ..
model.fit(X_train, y_train)
print "Fitting completed in: ", time.time() - s


#
# INFO: Display the OOB Score of your data
score = model.oob_score_
print "OOB Score: ", round(score*100, 3)




print "Scoring..."
s = time.time()
#
# TODO: score your model on your test set
#
# .. your code here ..
score = model.score(X_test, y_test)
print "Score: ", round(score*100, 3)
print "Scoring completed in: ", time.time() - s


#
# TODO: Answer the lab questions, then come back to experiment more


#
# TODO: Try playing around with the gender column
# Encode it as Male:1, Female:0
# Try encoding it to pandas dummies
# Also try dropping it. See how it affects the score
# This will be a key on how features affect your overall scoring
# and why it's important to choose good ones.



#
# TODO: After that, try messing with 'y'. Right now its encoded with
# dummies try other encoding methods to experiment with the effect.

