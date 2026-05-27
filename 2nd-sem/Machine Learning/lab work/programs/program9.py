from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
y_true = ['spam', 'ham', 'spam', 'ham', 'spam']
y_pred = ['spam', 'ham', 'spam', 'spam', 'spam']
print('Accuracy:', accuracy_score(y_true, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_true, y_pred, labels=['spam', 'ham']))
print('Classification Report:')
print(classification_report(y_true, y_pred))