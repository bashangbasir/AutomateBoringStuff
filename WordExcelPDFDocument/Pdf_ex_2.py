import PyPDF2
import os

# we can merge 2 pdf file into 1 single file 

os.chdir(r"F:\AutomateBoringStuff\WordExcelPDFDocument\PDF")

pdf_file_1 = open("meetingminutes.pdf","rb")
pdf_file_2 = open("meetingminutes2.pdf","rb")

reader_1 = PyPDF2.PdfFileReader(pdf_file_1)
reader_2 = PyPDF2.PdfFileReader(pdf_file_2)

#create writer object
writer = PyPDF2.PdfFileWriter()

for page_num in range(reader_1.numPages):
    page = reader_1.getPage(page_num)
    writer.addPage(page)

for page_num in range(reader_2.numPages):
    page = reader_2.getPage(page_num)
    writer.addPage(page)

output_file = open("combinedminutes.pdf","wb") # write binary mode
writer.write(output_file)

pdf_file_1.close()
pdf_file_2.close()