import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')
        
        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            #absolute_url = f'https://www.worldometers.info/{link}'
            # absolute_url = response.urljoin(link)
            
            # yield scrapy.Request(url = absolute_url)
            
            #relative url
            yield response.follow(url = link)
            
