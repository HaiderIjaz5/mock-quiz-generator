# utils.py

from fpdf import FPDF

def save_as_txt(mcqs, file_path="quiz.txt"):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(mcqs)
    return file_path

def save_as_pdf(mcqs, file_path="quiz.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in mcqs.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(file_path)
    return file_path
