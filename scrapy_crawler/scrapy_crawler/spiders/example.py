import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["customs.go.th"]
    start_urls = ["https://www.customs.go.th/statistic_report.php?show_search=1&s=SMy1GW7C8PGzeBj3"]
    rules

    def parse(self, response):
        pass
