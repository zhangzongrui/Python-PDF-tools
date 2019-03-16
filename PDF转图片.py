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
