# how well the model is performing! sklearn.metrics
# just for scoring the results

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

true_ans =  [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
predicted_ans = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0]

# accuracy is not enough when the data is unbalanced - assume 95% of data is of class 0 and 5% is of class 1
# if the model predicts everything as class 0, it will have 95% accuracy but will be useless for detecting class 1
# hence we need precision, recall and f1 score
print(f"Accuracy: {accuracy_score(true_ans, predicted_ans)} \n")
# precision is used when false alarms are dengerous - means that falsly accusing someone of a crime
print(f"Precision: {precision_score(true_ans, predicted_ans)} \n")
# recall is used when missing case is dengerous - means that missing a cancer diagnosis
print(f"Recall: {recall_score(true_ans, predicted_ans)} \n")
# f1 score is the harmonic mean of precision and recall - used when we want a balance between precision and recall
print(f"F1 Score: {f1_score(true_ans, predicted_ans)} \n")