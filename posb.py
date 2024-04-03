import pdfplumber

with pdfplumber.open('financial-statements/posb/2019_02.pdf') as pdf:
    for page in pdf.pages:
        print(page.chars[0])
