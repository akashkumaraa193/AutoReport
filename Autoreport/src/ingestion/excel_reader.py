import pandas as pd

class ExcelReader:

    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        data = pd.read_excel(self.filename)

        data = data.rename(columns={
        "Month": "title"
        })

        return data