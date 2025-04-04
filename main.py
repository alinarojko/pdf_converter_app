from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,300)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 25, 200, 25)

    # set the footer for main page with header
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for i in range (40, 298, 10):
        pdf.line(10, i , 200, i)

    # creating pages adde to the main with header
    for i in range(row["Pages"]-1):
        pdf.add_page()

        # set the footer for the other pages
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for i in range(40, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output("output.pdf")
