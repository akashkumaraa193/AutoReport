import pandas as pd


class CSVReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)

        data = data.rename(columns={
          "Month": "title"
        })
 
        return data