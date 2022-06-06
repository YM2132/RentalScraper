import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import RentalscraperItem


class ZooplaSpider(CrawlSpider):
    name = 'zoopla'
    allowed_domains = ['www.zoopla.co.uk']
    start_urls = ['https://www.zoopla.co.uk/to-rent/property/london/mile-end/?beds_max=2&beds_min=2&page_size=25&price_frequency=per_week&price_max=325&view_type=list&q=Mile%20End%2C%20London&radius=3&results_sort=newest_listings&search_source=refine']

    rules = (
        Rule(LinkExtractor(allow='to-rent/details/'), callback='parse_item'),
    )

    def parse_item(self, response):
        price_pm_response = response.xpath('//div/p[@data-testid="price"]/text()').get()
        # print('Per month cost ---->', price_pm_response[1:6])
        price_pw_response = response.xpath('//div/p[@data-testid="rentalfrequency-and-floorareaunit"]/text()').get()
        location_response = response.xpath('//div/address[@data-testid="address-label"]/text()').get()
        property_type_response = response.xpath('//h1[@id="listing-summary-details-heading"]/div/text()').get()

        zoopla_loader = ItemLoader(item=RentalscraperItem(), response=response)
        zoopla_loader.add_value('price_pw', price_pw_response[1:4])
        zoopla_loader.add_value('price_pm', price_pm_response[1:6])
        zoopla_loader.add_value('location', location_response)
        zoopla_loader.add_value('property_type', property_type_response)
        zoopla_loader.add_value('url', response.url)
        return zoopla_loader.load_item()




