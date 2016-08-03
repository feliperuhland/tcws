# coding: utf-8

import scrapy

from api import tasks


class TechCrunchSpider(scrapy.Spider):
    """
    Spider class for scraping TechCrunchs web site.
    """
    name = 'techcrunch'

    def __init__(self, pages=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = ['https://techcrunch.com/page/{}'.format(page_num) for page_num in range(1, int(pages)+1)]

    def parse(self, response):
        for article_link in response.css('li.river-block'):
            url = article_link.css('div.block-content > h2 > a::attr(href)').extract_first()
            if url:
                yield scrapy.Request(url, callback=self.article_parse)

    def article_parse(self, response):
        main = response.css('div.l-main')
        url = response.url
        title = main.css('header > h1::text').extract_first()
        posted = main.css('div.title-left > div.byline > time::attr(datetime)').extract_first()
        text = ' '.join([a for a in main.css('div.article-entry > p::text').extract() if a != ', '])
        data = {
            'url': url,
            'posted': posted,
            'title': title,
            'text': text,
        }
        author_url = response.urljoin(main.css('div.title-left > div.byline > a::attr(href)').extract_first())
        yield scrapy.Request(author_url, callback=self.author_parse, meta={'data': data})

    def author_parse(self, response):
        twitter_account = None
        for profile in response.css('div.inset-left').css('a::attr(href)'):
            if 'twitter' in profile.extract():
                twitter_account = profile.extract()

        data = response.meta['data']
        data['author'] = {
            'name': response.css('div.page-title > h1::text').extract_first(),
            'profile_url': response.url,
            'twitter_account': twitter_account,
            'resume':  ' '.join([a for a in response.css('div.profile-text > p::text').extract()]),
        }
        tasks.save_data.apply_async([data])
        yield data
