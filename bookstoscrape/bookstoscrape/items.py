# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class BooksToScrapeItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    book_names = scrapy.Field(
        output_processor = TakeFirst()
    )