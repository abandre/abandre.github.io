from tika import parser
from PyPDF2 import PdfFileWriter, PdfFileReader
import re
import sys
import os

files = []
path="tccs"

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

fout = open("tccs.res","w+")

files.sort(reverse=True)
anoref=-1
for f in files:
	ano=f.split("/")[1]
	if anoref!=ano:
		anoref = ano

		fout.write("<h2>"+str(ano)+"</h2>\r\n")

	inputpdf = PdfFileReader(open(f, "rb"))

	output = PdfFileWriter()
	output.addPage(inputpdf.getPage(0))
	with open("tmp.pdf", "wb") as outputStream:
		output.write(outputStream)
	raw = parser.from_file('tmp.pdf')


	#print(raw)
	content = raw['content'].replace("\n"," ")
	content = content.replace("\t"," ")
	content = content.split()
	content = " ".join(content)
	fout.write("<p>\r\n")
	fout.write(content)
	fout.write("<br><a href=\"/"+f+"\" target=\"_blank\">Ler mais</a>\r\n")
	fout.write("</p>\r\n")
	#break

fout.close()

# for i in range(inputpdf.numPages):
# 	output = PdfFileWriter()
# 	output.addPage(inputpdf.getPage(i))
# 	with open("document-page%s.pdf" % i, "wb") as outputStream:
# 		output.write(outputStream)
# 	break