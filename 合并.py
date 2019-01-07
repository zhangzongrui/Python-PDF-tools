import fitz

def merge(doc1,doc2):
    doc=doc1[0:-4]
    doc1=fitz.open(doc1)
    doc2=fitz.open(doc2)
    doc3 = fitz.open()
    doc3.insertPDF(doc1)
    doc3.insertPDF(doc2)
    doc3.save(doc+"(合并).pdf")

doc1="F:/Python/test1.pdf"
doc2="F:/Python/test2.pdf"
merge(doc1,doc2)
