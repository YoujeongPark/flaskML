from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle
from sklearn.externals import joblib
import numpy as np
# Load the iris data
iris = datasets.load_iris()

# Create a matrix, X, of features and a vector, y.
X, y = iris.data, iris.target

print(y)

clf = LogisticRegression(random_state=0)
clf.fit(X, y)
#
# data = np.array([5.1, 3.5, 1.4, 0.2])
# data = data.reshape(1,-1)
# my_prediction = clf.predict(data)
# print(my_prediction)


joblib.dump(clf, 'pickleIRIS.pkl')