import pandas as pd
from sklearn.linear_model import LinearRegression
X = [[800], [1000], [1200], [1500], [1800]]
y = [150000, 180000, 210000, 260000, 300000]
model = LinearRegression()
model.fit(X, y)
area = [[1400]]
prediction = model.predict(area)
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)
print('Predicted price for 1400 sq.ft:', prediction[0])