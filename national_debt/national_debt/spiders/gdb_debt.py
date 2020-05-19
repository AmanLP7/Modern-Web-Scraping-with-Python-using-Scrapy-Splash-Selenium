# -*- coding: utf-8 -*-
import scrapy


class GdbDebtSpider(scrapy.Spider):
    name = 'gdb_debt'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):

        countries_debt = response.xpath("//table[@class = 'datatableStyles__StyledTable-bwtkle-1 hOnuWY table table-striped']/tbody/tr")

        for debt in countries_debt:

            name = debt.xpath(".//td[1]/a/text()").get()
            debtRatio = debt.xpath(".//td[2]/text()").get()
            population = debt.xpath(".//td[3]/text()").get()

            yield {
                'Name': name,
                'Debt ratio': debtRatio,
                'Population': population
            }
