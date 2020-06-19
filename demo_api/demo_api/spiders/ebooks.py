# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.exceptions import CloseSpider


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'

    INCREMENT_BY = 12
    offset = 0

    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12']

    def parse(self, response):

        print(f"This is the response -> {response}")

        # if response["Status Code"] == 500:
        #     raise CloseSpider("Reached last page.........")

        data = json.loads(response.body)
        ebooks = data.get("works")
        for ebook in ebooks:
            yield {
                "Title": ebook.get("title"),
                "Subject": ebook.get("subject")
            }

        self.offset += self.INCREMENT_BY
        yield scrapy.Request(
            url = f"https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}",
            callback=self.parse

        ) 
