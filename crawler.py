'''
Logging is a means of tracking events
that happen when some software runs.

Logging is important for software developing,
debugging, and running.
'''
import logging
import os
import requests

#asctim = ascii time human readable time format
logging.basicConfig(format = '%(asctime)s %(levelname)s : %(message)s')


class Crawler:
	def __init__(self, urls=[]):
		self.visited_urls=[]
		self.urls_to_visit = urls

	def download_url(self, url):
		return requests.get(url).text

	def crawl(self, url):
		html = self.download_url(url)

	def run(self):
		while self.urls_to_visit:
			#pop first element of the urls list
			url = self.urls_to_visit.pop(0)
			
			logging.info(f'Crawling : {url}')

		try:
			self.crawl(url)

		except Exception:
			logging.exception(f'Failed to crawl : {url}')

		finally:
			pass


if __name__ == '__main__':
	os.system('tput reset')

	Crawler(urls=['https://www.customs.go.th']).run()
	#Crawler(urls=['https://www.customs.go.th/statistic_report.php?lang=en&']).run()
