# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.geekbuying.com']

    def start_requests(self):

        yield scrapy.Request(url='http://www.geekbuying.com/bestselling',
        callback=self.parse,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })

    def parse(self, response):
        products = response.xpath("//div[@class = 'li_cont']")
        for product in products:
            name = product.xpath(".//a[@class = 'items_p']/text()").get()
            URL = product.xpath(".//a[@class = 'items_p']/@href").get()
            price = product.xpath(".//span[@class = 'items_price']/text()").get()
            yield {
                'productName': name,
                'productURL': URL,
                'productPrice': price,
                'userAgent': response.request.headers['User-Agent']
            }

        nextPage = response.xpath("//a[@class='next']/@href").get()

        if nextPage:
            yield response.follow(url=nextPage,
            callback=self.parse,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
                })