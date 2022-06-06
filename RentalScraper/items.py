# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def price_comma_stripper(price_pm):
    return int(price_pm.replace(',', ''))

def price_pw_int(price_pw):
    return int(price_pw)


class RentalscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    price_pw = scrapy.Field(input_processor=MapCompose(price_pw_int), output_processor=TakeFirst())
    price_pm = scrapy.Field(input_processor=MapCompose(price_comma_stripper), output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    property_type = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())

