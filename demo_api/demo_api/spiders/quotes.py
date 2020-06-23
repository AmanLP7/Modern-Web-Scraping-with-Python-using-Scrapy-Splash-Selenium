# -*- coding: utf-8 -*-
import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        data = json.loads(response.body)
        quotes = data.get("quotes")
        
        for quote in quotes:
            yield {
                'author': quote.get("author").get("name"),
                'tags': quote.get("tags"),
                'text': quote.get("text")
            }

        hasNext = data.get("has_next")

        if hasNext == True:
            nextPage = data.get("page") + 1
            yield scrapy.Request(
                url=f"http://quotes.toscrape.com/api/quotes?page={nextPage}",
                callback=self.parse
            )


