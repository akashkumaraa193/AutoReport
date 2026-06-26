from src.ingestion.csv_reader import CSVReader
from src.ingestion.excel_reader import ExcelReader
from src.ingestion.json_reader import JSONReader
from src.ingestion.sqlite_reader import SQLiteReader
from src.ingestion.api_reader import APIReader
from src.analysis.statistics import Statistics
from src.analysis.trend import TrendAnalysis
from src.analysis.anomaly import AnomalyDetection
from src.visualization.charts import ChartGenerator
from src.report.pdf_report import PDFReport
from src.report.html_report import HTMLReport

print("\n====== SALES REPORT SYSTEM ======")
print("1. CSV")
print("2. JSON")
print("3. Excel")
print("4. SQLite")
print("5. API")

choice = int(input("Enter your choice: "))

if choice == 1:
    reader = CSVReader("sales.csv")

elif choice == 2:
    reader = JSONReader("sales.json")

elif choice == 3:
    reader = ExcelReader("sales.xlsx")

elif choice == 4:
    reader = SQLiteReader("sales.db")

elif choice == 5:
    reader = APIReader("https://dummyjson.com/products")

else:
    print("Invalid Choice")
    exit()

data = reader.load_data()
print(data.columns)
data = data.rename(columns={"price": "Sales",
                            "Month":"title"})

stats = Statistics(data)
trend = TrendAnalysis(data)
anomaly = AnomalyDetection(data)
chart = ChartGenerator(data)
pdf = PDFReport(data)
html = HTMLReport(data)

print("=" * 50)
print("         SALES REPORT")
print("=" * 50)

print()
print(data.columns)
print()

print("=" * 50)

print("Total Sales  :", stats.total_sales())
print("Average Sales:", stats.average())
print("Highest Sales:", stats.maximum())
print("Lowest Sales :", stats.minimum())
print("Median Sales :", stats.median())
print("Standard Dev.:", round(stats.standard_deviation(), 2))

print("=" * 50)

print()

print("Growth Rate (%)")

print(trend.growth_rate())

print()

print("Moving Average")

print(trend.moving_average())

print()

print("=" * 50)

print("Z SCORE")

print(anomaly.z_score())

print()

print("ANOMALIES")

print(anomaly.anomalies())

print("=" * 50)

chart.line_chart()

pdf.create_pdf()

html.create_html()

print()

print("HTML Report Created Successfully!")

print("PDF Created Successfully!")

print("Chart Created Successfully!")