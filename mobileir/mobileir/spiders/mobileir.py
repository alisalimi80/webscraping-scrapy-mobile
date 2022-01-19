import scrapy


class QuotesSpider(scrapy.Spider):
    name = "mobileir"
    start_urls = [
        "https://www.mobile.ir/phones/prices-brand-2-samsung.aspx"
    ]

    def parse(self, response):
        name = response.css("a.phone::text").getall()
        price = response.css("td.price a::text").getall()
        
        for digi in range(len(name)):
            yield {
                'name': name[digi],
                'price': price[digi]+"تومن",
                
            }

        next_page = response.css('div.pagination a::attr(href)').getall()
        for i in range(len(next_page)):
            if i>0:
                next_page1 = response.urljoin(next_page[i])
                yield scrapy.Request(next_page1, callback=self.parse)
                
# run with this cli code : scrapy crawl mobileir -o myjayson.json -s FEED_EXPORT_ENCODING=utf-8
