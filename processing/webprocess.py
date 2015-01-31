from __future__ import print_function
import sys
import urllib2
# import os
from bs4 import BeautifulSoup


class URLtoHTML:
	'''
	Converts given URL to text output. 

	'''

	def __init__(self, url):
		''' (URLtoText, str) -> NoneType
		'''

		self.url = url

	def convert_only_tables(self):
		''' (URLtoText) -> str
		'''

		self.response = urllib2.urlopen(self.url)
		self.html = self.response.read()
		self.soup = BeautifulSoup(self.html)
		return self.soup

	def extract_from_table(self, converted_text):
		''' (URLtoText, BeautifulSoup) -> NoneType
		'''

		second_table = []
		just_text = str(converted_text)
		first_table = just_text.split('<td>')
		for item in first_table:
			second_table.append(item.strip('\n'))
		string_table_HTML = ' '.join(second_table)
		return string_table_HTML

	def join_tables(self, final_table):
		''' (URLtoText) -> str
		'''

		table_into_string = ' '.join(final_table)
		final_string = table_into_string.strip('\n')
		return final_string 


class HTMLtoText:

	def __init__(self, HTML_string):
		'''
		'''

		self.HTML_string = HTML_string

	def convert_to_text(self):
		'''
		'''

		self.soup = BeautifulSoup(self.HTML_string)
		just_text = self.soup.get_text()
		return just_text



if __name__ == '__main__':
	u = URLtoHTML(sys.argv[1])
	# only_table_tags = SoupStrainer('') # find only tables
	converted_text = u.convert_only_tables()
	final_tables = u.extract_from_table(converted_text)
	h = HTMLtoText(final_tables)
	output = h.convert_to_text()

	with open('tmp.txt', 'w') as file:
		file.write(output)

	# os.system("python process.py tmp.txt")
