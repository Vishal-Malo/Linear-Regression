class LinearRegression:
    def __init__(self):
        self.m = 1
        self.b = 0

    def calculate_stepsize(self, m, b):
        s = 0
        if m:
            s = 2 * sum(self.x_train * (self.m * self.x_train + self.b - self.y_train))
        elif b:
            s = 2 * sum((self.m * self.x_train + self.b - self.y_train))

        return s

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

        learning_rate = 0.0001
        count = 0
        while count <= 1000:
            ssm = self.calculate_stepsize(m=True, b=False)
            ssb = self.calculate_stepsize(m=False, b=True)
            step_m = ssm * learning_rate
            step_b = ssb * learning_rate
            self.m = self.m - step_m
            self.b = self.b - step_b
            count = count + 1
            if -0.01 < step_m < 0.01 or -0.01 < step_b < 0.01:
                break

    def predict(self, x_test):
        return self.m * x_test + self.b
