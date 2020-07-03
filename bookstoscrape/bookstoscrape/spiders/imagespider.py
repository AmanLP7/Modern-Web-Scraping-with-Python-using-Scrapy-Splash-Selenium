##------------------------------------- Scrap images using scrapy -------------------------------------## 

import scrapy
from scrapy.loader import ItemLoader
from bookstoscrape.items import BooksToScrapeItem

class ImagesToScrapeSpider(scrapy.Spider):

    name = "downloader"

    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):

        for article in response.xpath("//article[@class='product_pod']"):
            loader = ItemLoader(item = BooksToScrapeItem(), selector = article)
            relativeURL = article.xpath(".//div[@class='image_container']/a/img/@src").extract_first()
            absoluteURL = response.urljoin(relativeURL)
            loader.add_value("image_urls", absoluteURL)
            loader.add_xpath("book_names", ".//h3/a/@title")

            yield loader.load_item()

