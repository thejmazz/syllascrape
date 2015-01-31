import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import itertools

class URLtoText:
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

		self.response = urllib.request.urlopen(self.url)
		self.html = self.response.read()
		self.soup = BeautifulSoup(self.html, parse_only=only_table_tags)
		return(self.soup)

	def extract_from_table(self, converted_text):
		''' (URLtoText, BeautifulSoup) -> NoneType
		'''

		just_text = str(converted_text)
		first_table = just_text.split('<tr>')
		# for x in first_table:
		# 	second_table = x.split('\n')
		# for y in second_table:
		# 	third_table.append(y.lstrip('<td>'))
		# for z in third_table:
		# 	fourth_table.append(z.strip('</strong>'))
		# for z in third_table:
		# 	if z != '':
		# 		fourth_table.append(z)

		for item in first_table:
			print(item)

	def join_tables(self, final_table):
		''' (URLtoText) -> str
		'''

		table_into_string = ' '.join(final_table)
		final_string = table_into_string.strip('\n')
		print(final_string)



if __name__ == '__main__':
	u = URLtoText("http://www.cdf.toronto.edu/~csc209h/winter//info.html")
	only_table_tags = SoupStrainer('tr') # find only tables
	converted_text = u.convert_only_tables()
	final_table = u.extract_from_table(converted_text)
	# u.join_tables(final_table)
	# output temp.txt
