from sklearn import tree

# INPUT [height,weight,shoe size]$
x = [[181,80,44],[181,70,24],[181,80,14],[131,80,44],[11,80,44],[121,80,44],[191,80,44],[181,60,44]]

# OUTPUT 
y = ['male','female','male','female','male','female','female','male']

#     o
#    / \
#   o   o
#  /\   /\
# o  o o  o
# classifies data with all possible outcomes
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[170,60,35]])

# print result 
print(prediction)