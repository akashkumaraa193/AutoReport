from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFReport:

    def __init__(self, dataframe):
        self.data = dataframe

    def create_pdf(self):

        pdf = canvas.Canvas("reports/Sales_Report.pdf", pagesize=letter)

        width, height = letter

        pdf.setFont("Helvetica-Bold",22)
        pdf.drawCentredString(width/2,height-50,"Sales Analysis Report")

        pdf.setFont("Helvetica",12)

        pdf.drawString(50,700,"Total Sales : "+str(self.data["Sales"].sum()))
        pdf.drawString(50,680,"Average Sales : "+str(round(self.data["Sales"].mean(),2)))
        pdf.drawString(50,660,"Highest Sales : "+str(self.data["Sales"].max()))
        pdf.drawString(50,640,"Lowest Sales : "+str(self.data["Sales"].min()))

        y=590

        pdf.setFont("Helvetica-Bold",12)

        pdf.drawString(50,y,"title")
        pdf.drawString(150,y,"Sales")

        pdf.setFont("Helvetica",12)

        y-=25

        for _,row in self.data.iterrows():

            pdf.drawString(50,y,str(row["title"]))
            pdf.drawString(150,y,str(row["Sales"]))

            y-=20

        pdf.drawImage(
            "charts/monthly_sales.png",
            300,
            380,
            width=250,
            height=180
        )

        pdf.setFont("Helvetica-Oblique",10)

        pdf.drawString(
            180,
            30,
            "Generated Automatically using Python"
        )

        pdf.save()