import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
model = LogisticRegression()
model.fit(X, y)
x_range = np.linspace(1, 8, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_range)[:, 1]
plt.scatter(X, y, label='Actual Data')
plt.plot(x_range, y_prob, label='Pass Probability')
plt.axhline(0.5, linestyle='--', label='Decision Boundary')
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.legend()
plt.show()