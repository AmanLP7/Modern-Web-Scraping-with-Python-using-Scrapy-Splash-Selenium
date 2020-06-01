# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class ScrapquotesSpider(scrapy.Spider):
    name = 'scrapQuotes'
    allowed_domains = ['quotes.toscrape.com/js']



    def parse(self, response):
        pass
