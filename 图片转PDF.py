#图片转PDF
def pic2pdf2(doc1):       
    Doc=doc1[0:-1]
    doc = fitz.open()                                  
    for img in sorted(glob.glob(doc1)):                   
        imgdoc = fitz.open(img)                        
        imgpdf = imgdoc.convertToPDF()                
        imgPDF = fitz.open("pdf",imgpdf)              
        doc.insertPDF(imgPDF)                          
    doc.save(Doc+"Image.pdf")                          
    doc.close()
    p2="\n操作完成，文件以保存在:\n"+Doc+"Image.pdf"
    return p2
