import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Read CSV file
df = pd.read_csv("data.csv")

# Data analysis
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()

# Create PDF
pdf = SimpleDocTemplate("output_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("<b>Automated Report Generation</b>", styles["Title"]))
content.append(Paragraph("Internship: CodTech", styles["Normal"]))
content.append(Paragraph(" ", styles["Normal"]))

content.append(Paragraph(f"Average Score:{average_score}", styles["Normal"]))
content.append(Paragraph(f"Highest Score:{highest_score}", styles["Normal"]))
content.append(Paragraph(f"Lowest Score:{lowest_score}", styles["Normal"]))

pdf.build(content)

print("PDF report generated successfully!")