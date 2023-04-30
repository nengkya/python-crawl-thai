class Crawler:
	def __init__(self, urls=[]):
		self.visited_urls=[]
		self.urls_to_visit = urls

	def run(self):
		while self.urls_to_visit:
			#pop first element of the urls list
			url = self.urls_to_visit.pop(0)



if __name__ == '__main__':
	Crawler(urls=['https://www.customs.go.th/statistic_report.php?lang=en&']).run()
