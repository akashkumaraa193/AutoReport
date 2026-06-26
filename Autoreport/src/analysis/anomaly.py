import numpy as np


class AnomalyDetection:

    def __init__(self, dataframe):
        self.data = dataframe

    def z_score(self):

        sales = self.data["Sales"]

        mean = sales.mean()

        std = sales.std()

        z_scores = []

        for value in sales:

            z = (value - mean) / std

            z_scores.append(float(round(z, 2)))

        return z_scores

    def anomalies(self):

        scores = self.z_score()

        result = []

        for i in range(len(scores)):

            if abs(scores[i]) > 2:

                result.append(self.data.iloc[i])

        return result