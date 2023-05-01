import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["customs.go.th"]
    start_urls = ["http://customs.go.th/"]

    def parse(self, response):
        pass
