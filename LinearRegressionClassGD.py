class LinearRegression:
    def __init__(self):
        self.m = 1
        self.b = 0

    def ss(self, m, b):
        sum = 0
        if m == 1:
            for i in range(len(self.x_train)):
                sum = sum + 2*self.x_train[i] * (self.m * self.x_train[i] + self.b - self.y_train[i])
        elif b == 1:
            for i in range(len(self.x_train)):
                sum = sum + 2*(self.m * self.x_train[i] + self.b - self.y_train[i])

        return sum

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

        lr = 0.01
        count = 0
        while count <= 1000:
            ssm = self.ss(m=1, b=0)
            ssb = self.ss(m=0, b=1)
            step_m = ssm * lr
            step_b = ssb * lr
            m = self.m - step_m
            b = self.b - step_b
            self.m = m
            self.b = b
            count = count + 1
            if -0.01 < step_m < 0.01 or -0.01 < step_b < 0.01:
                break

    def predict(self, x_test):
        return self.m * x_test + self.b
