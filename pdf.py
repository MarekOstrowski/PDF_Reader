import pypdf
import os

#  Autor Marek Ostrowski

os.chdir("C:\\Users\\ostro\\Python\\PDF")
pdfFile = ('dhl24.pdf')
reader = pypdf.PdfReader(pdfFile)
page1 = reader.pages[0]

#  Write Firt page to PDF
output_pdf = pypdf.PdfWriter()
output_pdf.add_page(page1)
output_pdf.write("first_page.pdf")






