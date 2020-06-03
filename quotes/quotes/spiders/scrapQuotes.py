# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class ScrapquotesSpider(scrapy.Spider):
    name = 'scrapQuotes'
    allowed_domains = ['quotes.toscrape.com']

    # Splash script
    script = '''
            function main(splash, args)

                url = args.url
                splash.private_mode_enabled = False
                assert(splash:go(url))
                assert(splash:wait(0.5))

                return splash:html()

            end
            '''

    def start_requests(self):
        yield SplashRequest(
            url="http://quotes.toscrape.com/js/",
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source":self.script
            }
            )


    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                "text": quote.xpath(".//span[@class='text']/text()").get(),
                "author": quote.xpath(".//span[2]/small[@class='author']/text()").get(),
                "tags": quote.xpath(".//div[@class='tags']/a/text()").getall()
            }

        nextPage = response.xpath("//li[@class='next']/a/@href").get()

        if nextPage:
            absoluteURL = f"http://quotes.toscrape.com{nextPage}"
            yield SplashRequest(
            url=absoluteURL,
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source":self.script
            }
            )







