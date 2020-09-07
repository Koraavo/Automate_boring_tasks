import PyPDF4
import os
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF4.PdfFileReader(pdfFile)
# reader.numPages # get all the pages in the pdf
page = reader.getPage(0)
print(page.extractText())

writer = PyPDF4.PdfFileWriter()
for pages in range(reader.numPages):
    page = reader.getPage(pages)
    writer.addPage(page)

output = open("new_minutes.pdf", 'wb')
writer.write(output)
output.close()
pdfFile.close()



