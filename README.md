# 🧾 Payment Receipt Generator using Python

This project demonstrates how to create professional **payment receipts in PDF format** using Python and the **ReportLab** library. It is useful for generating invoices, transaction receipts, and billing summaries programmatically.

---

## 🚀 Features
- Generates PDF receipts automatically
- Uses tabular transaction data
- Custom styling (colors, alignment, borders)
- Beginner-friendly and reusable

---

## 🛠️ Technologies Used
- Python
- ReportLab

---

## 🧠 Project Approach (Step-by-Step)
## 1️⃣ Import Required Modules
We import ReportLab modules for:
- PDF creation.
- Table rendering.
- Styling and colors.

## 2️⃣ Prepare Transaction Data
The receipt data is stored as a list of lists:
- The first row acts as table headers.
- Remaining rows contain transaction details.

## 3️⃣ Create a PDF Template
- A SimpleDocTemplate is created using A4 page size.

## 4️⃣ Apply Styles:
- Default stylesheet is loaded.
- Title is center-aligned.
- Table borders, background colors, and text colors are defined using TableStyle.

## 5️⃣ Build the PDF
- All elements (title + table) are passed to pdf.build() to generate the final receipt.

---

## 🖼️ Sample Output
![Application Screenshot]()

---

## 📌 Use Cases
Billing systems
Invoice generators
Subscription receipts
Learning PDF automation

---

## 🤝 Contributing
Pull requests are welcome.
