import urllib.request
from bs4 import BeautifulSoup

class URLtoText:
	'''
	Converts given URL to text output. 

	'''

	def __init__(self, url):
		''' (URLtoText, str) -> NoneType
		'''

		self.url = url

	def convert_to_text(self):
		''' (URLtoText) -> str
		'''

		response = urllib.request.urlopen(self.url)
		html = response.read()
		self.soup = BeautifulSoup(html)
		return self.soup.prettify()

	def extract_from_table(self):
		''' (URLtoText) -> NoneType
		'''

		self.td = self.soup.find_all('td')

	def from_table_to_text(self):
		''' (URLtoText) -> str
		'''

		print(self.td.get_text())

if __name__ == '__main__':
	u = URLtoText("http://www.cdf.toronto.edu/~csc209h/winter//info.html")
	u.convert_to_text()
	u.extract_from_table()
	u.from_table_to_text()