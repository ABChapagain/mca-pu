import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = [[800], [1000], [1200], [1500], [1800]]
y = [150000, 180000, 210000, 260000, 300000]
model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)
plt.scatter(X, y, label='Actual Data')
plt.plot(X, predicted, label='Regression Line')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)