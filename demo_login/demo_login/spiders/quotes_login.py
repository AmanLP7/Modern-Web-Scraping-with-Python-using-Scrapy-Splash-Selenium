# -*- coding: utf-8 -*-
import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['quotes.toscrape.com/login']
    start_urls = ['https://quotes.toscrape.com/login/']

    def parse(self, response):
        pass
