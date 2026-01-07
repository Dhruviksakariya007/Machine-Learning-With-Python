# this method works fine when decision follow step by step logic! such as loan approval, document - yes/no, opt...etc.
# can be too smart! it can remember all the data (memorise) and give 100% accuracy on training data but fail on new data!
# overfitting - when model is too complex
# underfitting - when model is too simple
# e.g - cat image recognition - black, white, grey cat all look different but human can identify them easily, but if we only give black and white cat images to model to train, it may fail to identify grey cat while testing.
from sklearn import *
from sklearn.tree import *
import pandas as pd

data = {
    'StudyHours': [1, 2, 3, 5, 4, 6, 8, 7],
    'TestScores': [10, 25, 40, 60, 70, 90, 99, 85]
}
df = pd.DataFrame(data)

hr = float(input("Enter your Studied Hours: "))

input = df['StudyHours'].values.reshape(-1, 1)
output = df['TestScores']

model = DecisionTreeClassifier()
model.fit(input, output)

predictions = model.predict([[hr]])[0] # [0] or [1] - 0 means value inside list and 1 returns whole list

if predictions >= 90:
    print("Excellent")
elif predictions >= 75 and predictions < 90:
    print("Very Good")
elif predictions >= 50 and predictions < 75:
    print("Good")
else:
    print("********************* Needs Improvement *********************")
print(f"Based on your hours ({hr}) you may score around {predictions}")