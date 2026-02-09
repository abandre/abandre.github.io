from tika import parser # pip install tika
import os
from os import walk
import sys

# for i in `ls *.docx`; do soffice --headless --convert-to pdf $i; done

filenames = next(walk(sys.argv[1]), (None, None, []))[2] 

print(filenames)

f = open("res.txt","w+")
for arq in filenames:
	os.system("pdftk "+sys.argv[1]+"/"+arq+" cat 1 output out.pdf")
	raw = parser.from_file("out.pdf")
	
	f.write('<p>\n')
	f.write(raw['content'].replace('\n','')+'\n')
	f.write('<br><a href="/tccs/'+sys.argv[1]+"/"+arq+'" target="_blank">Ler mais</a>\n')
	f.write('</p>\n')	

f.close()

