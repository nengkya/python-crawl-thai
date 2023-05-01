from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ExampleSpider(CrawlSpider):
    name = "example"
    allowed_domains = ["customs.go.th"]
    start_urls = ["https://www.customs.go.th/statistic_report.php?show_search=1&s=SMy1GW7C8PGzeBj3"]
    rules = (Rule(LinkExtractor()),)

    def parse(self, response):
        pass
