# Creating Payment Receipts using ReportLab

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Receipt data (list of lists)
DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    [
        "16/11/2020",
        "Full Stack Development with React & Node JS - Live",
        "Lifetime",
        "10,999.00/-",
    ],
    ["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
    ["Sub Total", "", "", "20,998.00/-"],
    ["Discount", "", "", "-3,000.00/-"],
    ["Total", "", "", "17,998.00/-"],
]

# Create PDF document
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# Load default styles
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1  # Center alignment

# Title paragraph
title = Paragraph("GeeksforGeeks", title_style)

# Table styling
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

# Create table
table = Table(DATA, style=style)

# Build PDF
pdf.build([title, table])

print("✅ Payment receipt generated successfully: receipt.pdf")