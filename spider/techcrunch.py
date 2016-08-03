# coding: utf-8

import scrapy


class TechCrunchSpider(scrapy.Spider):
    """
    Spider class for scraping TechCrunchs web site.
    """
    name = 'techcrunch'
    start_urls = ('https://techcrunch.com/',)

    def parse(self, reponse):
        pass
