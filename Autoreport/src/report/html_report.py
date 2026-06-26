class HTMLReport:

    def __init__(self, dataframe):
        self.data = dataframe

    def create_html(self):

        html = f"""
        <html>

        <head>

        <title>Sales Report</title>

        <style>

        body{{
            font-family:Arial;
            background:#f5f5f5;
            padding:40px;
        }}

        h1{{
            color:#1565C0;
            text-align:center;
        }}

        table{{
            width:60%;
            border-collapse:collapse;
            margin:auto;
            background:white;
        }}

        th,td{{
            border:1px solid black;
            padding:10px;
            text-align:center;
        }}

        th{{
            background:#1565C0;
            color:white;
        }}

        img{{
            display:block;
            margin:auto;
            margin-top:30px;
            width:600px;
        }}

        </style>

        </head>

        <body>

        <h1>Sales Analysis Report</h1>

         <div style="display:flex;gap:20px;margin-bottom:20px;">
         <div style="padding:15px;background:#4CAF50;color:white;border-radius:10px;">
         <h3>Total Sales</h3>
         <h2>{self.data["Sales"].sum()}</h2>
         </div>

         <div style="padding:15px;background:#2196F3;color:white;border-radius:10px;">
         <h3>Average Sales</h3>
         <h2>{round(self.data["Sales"].mean(),2)}</h2>
         </div>

         <div style="padding:15px;background:#FF9800;color:white;border-radius:10px;">
         <h3>Highest Sales</h3>
         <h2>{self.data["Sales"].max()}</h2>
         </div>

         <div style="padding:15px;background:#F44336;color:white;border-radius:10px;">
         <h3>Lowest Sales</h3>
         <h2>{self.data["Sales"].min()}</h2>
         </div>
         </div>

         <table>

         <tr>

         <th>title</th>

         <th>Sales</th>

         </tr>
         """

        for _, row in self.data.iterrows():

            html += f"""

            <tr>

            <td>{row['title']}</td>

            <td>{row['Sales']}</td>

            </tr>

            """

        html += """

        </table>

        <img src="../charts/monthly_sales.png">

        </body>

        </html>

        """

        with open("reports/Sales_Report.html","w") as file:

            file.write(html)