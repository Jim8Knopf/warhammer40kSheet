from reportlab.pdfgen import canvas

data = [
    ['bla1', 'bla2', 'bla3', 'bla4'],
    ['bla1', 'bla2', 'bla3', 'bla4'],
    ['bla1', 'bla2', 'bla3', 'bla4'],
]


# ###################################
# Content
fileName = 'MyDoc.pdf'
documentTitle = 'Table'
title = 'this is a table'
subTitle = 'The largest carnivorous marsupial'


# ###################################
# 0) Create document


pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)
pdf.save()
