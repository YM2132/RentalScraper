import random

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from ..items import RentalscraperItem


class OnTheMarketSpider(CrawlSpider):
    name = 'onthemarket'
    allowed_domains = ['www.onthemarket.com']
    start_urls = ['https://www.onthemarket.com/to-rent/2-bed-property/mile-end-london/?max-bedrooms=2&max-price=325&price-frequency=pw&radius=3.0&view=grid']

    # base_url = 'www.onthemarket.com'

    rules = (
        Rule(LinkExtractor(allow='details/'), callback='parse_item'),
    )

    def parse_item(self, response):
        title_list = response.xpath('//head/title/text()').get().split(' - ')
        # print(title_list)
        # print(title_list[-1])
        price_pm_pw_str = title_list[1]
        # print(price_pm_pw_str)

        price_pm = price_pm_pw_str[1:6]
        # print(price_pm)

        price_pw = price_pm_pw_str[13:16]
        # print('price per week: ', price_pw)

        # price_pm_pw_list = price_pm_pw_str.split(' ')
        # print(price_pm_pw_list)

        property_type_response = response.xpath('//div/h1[@class="h4 md:text-xl"]/text()').get()

        otm_loader = ItemLoader(item=RentalscraperItem(), response=response)
        otm_loader.add_value('price_pw', price_pw)
        otm_loader.add_value('price_pm', price_pm)
        otm_loader.add_value('location', title_list[0])
        otm_loader.add_value('property_type', property_type_response)
        otm_loader.add_value('url', response.url)
        return otm_loader.load_item()



