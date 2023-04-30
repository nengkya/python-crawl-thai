'''
Logging is a means of tracking events
that happen when some software runs.

Logging is important for software developing,
 debugging, and running.
'''
import logging


class Crawler:
	def __init__(self, urls=[]):
		self.visited_urls=[]
		self.urls_to_visit = urls

	def run(self):
		while self.urls_to_visit:
			#pop first element of the urls list
			url = self.urls_to_visit.pop(0)
			
			logging.ingo(f'Crawling : {url}')



if __name__ == '__main__':
	Crawler(urls=['https://www.customs.go.th/statistic_report.php?lang=en&']).run()
