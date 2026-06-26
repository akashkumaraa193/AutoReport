import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self, dataframe):
        self.data = dataframe

    def line_chart(self):

        plt.figure(figsize=(8,5))

        plt.plot(
            self.data["title"],
            self.data["Sales"],
            marker="o",
            linewidth=3
        )

        plt.title("Product Prices")

        plt.xlabel("Product")

        plt.ylabel("Sales")

        plt.grid(True)

        plt.savefig("charts/monthly_sales.png")

        plt.close()