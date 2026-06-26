import requests
import pandas as pd


class APIReader:

    def __init__(self, url):
        self.url = url

    def load_data(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()

            if "products" in data:
                return pd.DataFrame(data["products"])
            else:
                return pd.DataFrame(data)
        else:
            raise Exception("Failed to fetch API data")