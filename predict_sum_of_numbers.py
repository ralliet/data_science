from sklearn import tree

X = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [8, 8], [9, 9], [10, 10], [11, 11]]
Y = [0,2,4,6,8,10,12,16,18,20,22]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
prediction = clf.predict([[6,6]])

# print result 
print(prediction)