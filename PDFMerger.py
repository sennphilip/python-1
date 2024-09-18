from os import listdir, mkdir
from os.path import isfile, join, exists
from PyPDF2 import PdfMerger

path = "/Users/philipsenn/Downloads/pytests/"
pdffiles = [f for f in sorted(listdir(path)) if isfile(join(path, f)) and '.pdf' in f]
print('\nList of PDF Files:\n')
for file in pdffiles:
   print(file)

resultFile = input("\nEnter the name of the result file : ")
if '.pdf' not in resultFile:
   resultFile += '.pdf'

merger = PdfMerger()
for pdf in pdffiles:
   merger.append(path+pdf)

merger.write(path+resultFile)
merger.close()
