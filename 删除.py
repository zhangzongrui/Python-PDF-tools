#删除
def delete(doc,from_pa,to_pa):
    Doc=doc[0:-4]
    doc=fitz.open(doc)
    doc.deletePageRange(from_pa-1,to_pa-1)
    doc.save(Doc+"(new).pdf")
    d1="\n操作完成，文件以保存在:\n"+Doc+"(new).pdf"
    return d1
