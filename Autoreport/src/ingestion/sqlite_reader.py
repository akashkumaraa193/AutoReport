import sqlite3
import pandas as pd


class SQLiteReader:

    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        conn = sqlite3.connect(self.filename)

        df = pd.read_sql_query(
            "SELECT * FROM sales",
            conn
        )

        conn.close()

        df = df.rename(columns={
             "Month": "title"
        })

        return df