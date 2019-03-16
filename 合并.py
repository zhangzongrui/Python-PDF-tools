import fitz

#合并
def merge(doc1,doc2):
    Doc=doc1[0:-4]
    doc1=fitz.open(doc1)
    doc2=fitz.open(doc2)
    doc3 = fitz.open()
    doc3.insertPDF(doc1)
    doc3.insertPDF(doc2)
    doc3.save(Doc+"(合并).pdf")
    #print("操作完成，文件以保存在:\n"+Doc+"(合并).pdf")
    m1="操作完成，文件以保存在:\n"+Doc+"(合并).pdf"
    return m1
