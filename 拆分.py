import fitz

#拆分
def split(doc, from_pa, to_pa):
    Doc=doc[0:-4]
    doc=fitz.open(doc)
    DOC = fitz.open()
    DOC.insertPDF(doc,from_page=from_pa-1,to_page=to_pa-1)
    DOC.save(Doc+"(拆分).pdf")
    #print("操作完成，文件以保存在:"+Doc+"(拆分).pdf")
    s1="\n操作完成，文件以保存在:\n"+Doc+"(拆分).pdf"
    return s1

def main():
    doc="F:/Python/test.pdf"
    split(doc)

if __name__ == '__main__':
    main()

