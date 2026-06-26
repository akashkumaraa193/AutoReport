class TrendAnalysis:

    def __init__(self, dataframe):
        self.data = dataframe

    def growth_rate(self):

        sales = self.data["Sales"]

        growth = []

        growth.append(0)

        for i in range(1, len(sales)):

            previous = sales[i - 1]

            current = sales[i]

            rate = ((current - previous) / previous) * 100

            growth.append(float(round(rate, 2)))

        return growth

    def moving_average(self):

        moving=self.data["Sales"].rolling(window=3).mean().round(2)
        return moving.tolist()