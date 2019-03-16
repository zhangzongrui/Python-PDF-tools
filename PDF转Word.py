def pdfToword(doc):
    Doc=doc[0:-4]
    doc = fitz.open(doc)                  
    DOC = open(Doc + ".doc","w")
    for page in doc:                            
        text = page.getText()   
        DOC.write(text)
    DOC.close()
    #print("操作完成，文件以保存在:"+Doc+".doc")
    p1="操作完成，文件以保存在:\n"+Doc+".doc"
    return p1
