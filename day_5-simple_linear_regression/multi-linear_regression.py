# import the necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# get your data for training the model

X = np.array([ [1, 2],
               [2, 3],
               [3, 4], 
               [4, 5], 
               [5, 6]])  # Independent variables (features)
Y = np.array([2, 4, 5, 4, 5])  # Dependent variable

# create an object of the linear regression model
model = LinearRegression()
model.fit(X, Y)

# get the data you want the predicted value for

X_new = np.array([[6, 7]])  # New data with two features
y_pred = model.predict(X_new)

print(y_pred)