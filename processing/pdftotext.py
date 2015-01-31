import os
import sys

filename = sys.argv[1]

os.system("pdftotext -raw -enc UTF-8 " + filename + " pdfoutput.txt")
