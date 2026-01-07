# outpur always in 2d matrix TN/FN, TP/FP
# confusion matrix tells how many correct and incorrect predictions are made by the classification model
# compared to the actual outcomes (target values) in the dataset
# used in medicine, fraud detection, quality control etc
from sklearn.metrics import confusion_matrix

true_ans =  [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
predicted_ans = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0]

cm = confusion_matrix(true_ans, predicted_ans)
print("Confusion Matrix: \n", cm)
