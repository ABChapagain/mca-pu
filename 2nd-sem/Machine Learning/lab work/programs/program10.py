from sklearn.linear_model import LogisticRegression
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1] # 0 = Fail, 1 = Pass
model = LogisticRegression()
model.fit(X, y)
hours = [[5.5]]
result = model.predict(hours)
probability = model.predict_proba(hours)
print('Prediction:', 'Pass' if result[0] == 1 else 'Fail')
print('Probability:', probability)