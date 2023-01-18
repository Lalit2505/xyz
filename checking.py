from pdf import converter

pdf_file='setu.pdf'
docx_file='setu_1.docx'

cv=converter(pdf_file)
cv.convert(docx_file)
cv.close()

