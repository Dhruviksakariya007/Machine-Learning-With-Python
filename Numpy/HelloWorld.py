import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataSet = pd.read_csv('music.csv')
x = dataSet.drop(columns=['genre'])
y = dataSet['genre']

# model = DecisionTreeClassifier()
# model.fit(x, y)
# predictions = model.predict([[31, 1], [22, 0]]) # Add new record for prediction!
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) #0.2 means 20% data for testing and 80% for training
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_train)

score = accuracy_score(y_train, predictions)
print(f"Accuracy: {score}")

# print(dataSet)

# print(f"Predictions: = {predictions}")