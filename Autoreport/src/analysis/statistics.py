class Statistics:

    def __init__(self, dataframe):
        self.data = dataframe

    def average(self):
        return self.data["Sales"].mean()

    def maximum(self):
        return self.data["Sales"].max()

    def minimum(self):
        return self.data["Sales"].min()

    def median(self):
        return self.data["Sales"].median()

    def standard_deviation(self):
        return self.data["Sales"].std()

    def total_sales(self):
        return self.data["Sales"].sum()