import os
import sys

filename = sys.argv[1]

os.system("pdftotext -raw " + filename + " pdfoutput.txt")
