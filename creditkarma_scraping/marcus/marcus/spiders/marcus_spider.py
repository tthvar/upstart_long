import scrapy
class MarcusSpider(scrapy.Spider):
    name = "marcus_reviews"

    def start_requests(self):
        main = "https://www.creditkarma.com/reviews/personal-loan/single/id/goldmansachs?pg="
        urls = []
        for i in range(1, 7):
            urls.append(main + str(i))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.readmoreInner'):
            yield {
                'text': quote.css('p').get(),
            }