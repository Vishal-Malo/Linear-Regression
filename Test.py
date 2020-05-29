import numpy as np
# vishal malo
import pandas as pd
from sklearn.model_selection import train_test_split
from LinearRegressionClass import LinearRegression

data = pd.read_csv("Salary_Data.csv")
x = data.iloc[:, 0].values
y = data.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
regressor = LinearRegression()
regressor.fit(x_train=x_train, y_train=y_train)

YearsOfExperience = float(input("Enter your years of experience: "))

y_pred = regressor.predict(YearsOfExperience)
print("You should get a salary around \u20B9", y_pred)