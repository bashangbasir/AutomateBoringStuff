import PyPDF2
import os

# not completely compatible with pdf 
# some pdf file may be cant open. 
# may not be able to extract text from pdf file perfectly. 
# this is because pdf file is complicated. 
# this module (PyPDF2) doesn't have a way to extract images or charts or media
# but it can extract text

cwd = os.chdir(r"F:\AutomateBoringStuff\WordExcelPDFDocument\PDF")

pdf_file = open("meetingminutes.pdf","rb") #need to read binary mode since pdf file is in binary 

reader = PyPDF2.PdfFileReader(pdf_file) # this will return reader object

#get number of pages 
num_pages = reader.numPages

#get the page data

page_1 = reader.getPage(0) # get page object
page_1_content = page_1.extractText() #extract text content
print(page_1_content)

