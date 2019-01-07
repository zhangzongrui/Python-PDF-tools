import fitz

def split(doc):
    Doc=doc[0:-4]
    doc=fitz.open(doc)
    DOC = fitz.open()
    a=1;b=3
    DOC.insertPDF(doc,from_page=a-1,to_page=b-1)
    DOC.save(Doc+"(拆分).pdf")

doc="F:/Python/test.pdf"
split(doc)
