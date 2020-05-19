# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']

    def start_requests(self):

        yield scrapy.Request(url='https://www.tinydeal.com/specials.html',
        callback=self.parse,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })

    def parse(self, response):

        for product in response.xpath("//ul[@class = 'productlisting-ul']/div"):

            yield {
                'Title': product.xpath(".//a[@class = 'p_box_title']/text()").get(),
                'URL': response.urljoin(product.xpath(".//a[@class = 'p_box_title']/@href").get()),
                'Discounted price': product.xpath(".//div[@class = 'p_box_price']/span[1]/text()").get(),
                'Original price': product.xpath(".//div[@class = 'p_box_price']/span[2]/text()").get(),
                'User-Agent': response.request.headers['User-Agent']
            }

        nextPage = response.xpath("//a[@class = 'nextPage']/@href").get()

        if nextPage:

            yield scrapy.Request(url=nextPage,
            callback=self.parse,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
                })
