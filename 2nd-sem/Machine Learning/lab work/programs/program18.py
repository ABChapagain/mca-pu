# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Decision Tree classifier
model = DecisionTreeClassifier(random_state=1)

# Perform 10-fold cross validation prediction
y_pred = cross_val_predict(model, X, y, cv=10)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)

# Display results
print("Accuracy:", accuracy * 100)

print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))

print("\nClassification Report:")
print(classification_report(y, y_pred, target_names=iris.target_names))