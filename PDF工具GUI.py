import time
import glob
import fitz
from tkinter import *
from tkinter.filedialog import *

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

#删除
def delete(doc,from_pa,to_pa):
    Doc=doc[0:-4]
    doc=fitz.open(doc)
    doc.deletePageRange(from_pa-1,to_pa-1)
    doc.save(Doc+"(new).pdf")
    d1="\n操作完成，文件以保存在:\n"+Doc+"(new).pdf"
    return d1

#PDF转Word
def pdfToword(doc):
    Doc=doc[0:-4]
    doc = fitz.open(doc)                  
    DOC = open(Doc + ".doc","wb")
    for page in doc:                            
        text = page.getText().encode("utf8")   
        DOC.write(text)
    DOC.close()
    #print("操作完成，文件以保存在:"+Doc+".doc")
    p1="操作完成，文件以保存在:\n"+Doc+".doc"
    return p1

#PDF转图片
def PDF_Pic(doc,from_page,to_page):
    Doc=doc[0:-4]
    doc = fitz.open(doc)
    for pg in range(from_page-1,to_page):
        page = doc[pg]
        zoom = int(100)
        rotate = int(0)
        H=20; M=40; L=60
        trans = fitz.Matrix(zoom / M, zoom / M).preRotate(rotate)
        pm = page.getPixmap(matrix=trans,alpha=True)
        pm.writePNG(Doc+"第%s页.png" % str(pg+1))
    #print("操作完成!")
    p3="\n操作完成!\n"
    return p3

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

def wait(x):
    time.sleep(x)

def load():
    text.insert(INSERT,"初始化...\n")
    text.delete("1.0","end")

#合并文档功能
def merges():
    load()
    text.insert(INSERT,"请选择第一个文件\n\n")
    doc1=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
    text.insert(INSERT,"请选择第二个文件\n\n")
    doc2=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
    m1=merge(doc1,doc2)
    text.insert(INSERT,m1)

#PDF转word功能
def PDF2word():
    load()
    text.insert(INSERT,"请选择文件\n\n")
    doc=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
    p1=pdfToword(doc)
    text.insert(INSERT,p1)

#图片转PDF功能
def Pic2PDF():
    load()
    text.insert(INSERT,"使用介绍：\n你需要把转换的图片放在一个新建的目录下,程序会按名称进行排序转换成PDF文件")
    text.insert(INSERT,"\n\n请选择文件夹\n\n")
    doc=askdirectory()
    doc1=doc+r"/*"
    p2=pic2pdf2(doc1)
    text.insert(INSERT,p2)

class App:
    
    def __init__(self,x):
        self.x=x
        self.doc=x
    
    def enter(self):
        from_page=int(v1.get())
        to_page=int(v2.get())

        if self.x==1 :
            s1=split(self.doc,from_page,to_page)
            text.insert(INSERT,s1)
        elif self.x==2 :
            d1=delete(self.doc,from_page,to_page)
            text.insert(INSERT,d1)
        elif self.x==3 :
            p3=PDF_Pic(self.doc,from_page,to_page)
            text.insert(INSERT,p3)

    #PDF转图片功能
    def PDF2Pic(self):
        load()
        self.x=3
        text.insert(INSERT,"请选择文件\n")
        self.doc=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
        text.insert(INSERT,"\n请在下面输入要转换的始、末页\n")

    #删除页面功能
    def deletes(self):
        load()
        self.x=2
        text.insert(INSERT,"请选择文件\n")
        self.doc=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
        text.insert(INSERT,"\n请在下面输入要删除的始、末页\n")

    #拆分页面功能
    def splits(self):
        load()
        self.x=1
        text.insert(INSERT,"请选择文件\n")
        self.doc=askopenfilename(defaultextension=".pdf",filetypes=[("PDF",".pdf")])
        text.insert(INSERT,"\n请在下面输入要拆分的始、末页\n")

app=App(1)
root=Tk()
root.title("PDF工具 V2.0")
#root.geometry('500x500')

frame=Frame(root)
frame.pack(side=TOP,padx=10,pady=10)
frame1=Frame(root)
frame1.pack(side=TOP,padx=10,pady=10)

title=Label(frame,text="  PDF工具 V2.0 ",fg="Blue",bg="SkyBlue")
title.pack()
text=Text(frame,width=28,height=12)
text.pack()

v1=StringVar()
v2=StringVar()
Label(frame,text=" 起始页: ",fg="Blue",bg="SkyBlue").pack(fill=X,side=LEFT)
Entry(frame,textvariable=v1,width=10).pack(fill=X,side=LEFT)
Label(frame,text=" 终止页: ",fg="Blue",bg="SkyBlue").pack(fill=X,side=LEFT)
Entry(frame,textvariable=v2,width=10).pack(fill=X,side=LEFT)
Button(frame,text="  确定  ",fg="Blue",bg="SkyBlue",command=lambda:app.enter()).pack(fill=X,side=LEFT)

Button(frame1,text="  文档拆分  ",fg="Blue",bg="SkyBlue",command=app.splits).pack(fill=X,side=LEFT)
Button(frame1,text="  文档合并  ",fg="Blue",bg="SkyBlue",command=merges).pack(fill=X,side=LEFT)
Button(frame1,text="  删除页面  ",fg="Blue",bg="SkyBlue",command=app.deletes).pack(fill=X,side=LEFT)
Button(frame1,text=  "PDF转word" ,fg="Blue",bg="SkyBlue",command=PDF2word).pack(fill=X,side=LEFT)
Button(frame1,text= " PDF转图片 ",fg="Blue",bg="SkyBlue",command=app.PDF2Pic).pack(fill=X,side=LEFT)
Button(frame1,text= " 图片转PDF ",fg="Blue",bg="SkyBlue",command=Pic2PDF).pack(fill=X,side=LEFT)

mainloop()
