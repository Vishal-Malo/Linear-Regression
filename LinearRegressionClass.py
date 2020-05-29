import numpy as np


class LinearRegression:
    def __init__(self):
        self.result = []
        self.result_w = []

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

        self.x_mean = np.mean(self.x_train)
        self.y_mean = np.mean(self.y_train)

        self.m = 0
        self.c = 0

        for i in range(len(self.x_train)):
            num = (self.x_train[i] - self.x_mean) * (self.y_train[i] - self.y_mean)
            den = (self.x_train[i]) ** 2

            self.m = self.m + (num / den)
            self.c = self.c + (self.y_mean - ((num / den) * self.x_mean))

        self.m = self.m / len(self.x_train)
        self.c = self.c / len(self.x_train)

    def predict(self, x_test):
        return self.m * x_test + self.c
