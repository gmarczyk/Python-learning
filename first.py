from sklearn import tree
from sklearn.datasets import load_iris

# -- Decision tree building
features = [[140, 1], [130, 1], [150, 1], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[140, 0]]))

# -- Load iris dataset
iris = load_iris()

print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])

for i in range(len(iris.target)):
    print("Example %d: label %s, features %s" % (i, iris.target[i],
                                                 iris.data[Fi]))
