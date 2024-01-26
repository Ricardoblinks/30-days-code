# import the necessary libraries
import numpy as np


"""
first of all let us write a function that will generate the Mean, Slope and intercept
then define a prediction model that takes in the slope, intercept and the value you want a prediction on
"""

# linear regression for single feature


def simpleLinearRegression(X, Y):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X) ** 2)
    slope = numerator / denominator

    intercept = mean_Y - slope * mean_X

    return slope, intercept

def predict(slope, intercept, x_new):

    y_pred = slope * x_new + intercept
    return y_pred


# lets test this out

# get the data into 2 arrays

# X = np.array([1,2,3,4,5,6,7,8,9])
# Y = np.array([2,4,1,1,4,6,4,3,1])
X = np.array([1, 2, 3, 4, 5])  # Independent variable
Y = np.array([2, 4, 5, 4, 5])  # Dependent variable


# use the regression model to get the slope and intercept
slope, intercept = simpleLinearRegression(X, Y)

x_new = np.array([5, 12, 14])
y_pred = predict(slope, intercept, x_new)

# lets print out our result
print(y_pred)