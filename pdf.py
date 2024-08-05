import pypdf
import os

#  Autor Marek Ostrowski

os.chdir("C:\\Users\\ostro\\Python\\PDF")
pdfFile = ('dhl24.pdf')
reader = pypdf.PdfReader(pdfFile)
page1 = reader.pages[0]
text = page1.extract_text()
print(text)





