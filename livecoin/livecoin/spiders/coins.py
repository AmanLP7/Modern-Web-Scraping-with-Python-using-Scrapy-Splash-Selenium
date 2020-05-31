# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class CoinsSpider(scrapy.Spider):
    name = 'coins'
    allowed_domains = ['www.livecoin.net/en']

    # Splash script
    script = '''
        function main(splash, args)
            url = args.url
            splash.private_mode_enabled = False
            assert(splash:go(url))
            assert(splash:wait(0.5))
            usd_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
            usd_tab[3]:mouse_click()
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url="https://www.livecoin.net/en",
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source":self.script
            }
            )

    def parse(self, response):
        print(response.body)
