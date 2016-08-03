# coding: utf-8

from celery import shared_task
from django.conf import settings
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor

from api import models
from spider.techcrunch import TechCrunchSpider


@shared_task
def freq():
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    d = process.crawl(TechCrunchSpider, pages=settings.PAGES)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


@shared_task
def save_data(data):
    author, _ = models.Author.objects.update_or_create(
        name=data['author']['name'],
        defaults=data['author']
    )
    data['author'] = author
    article, _ = models.Article.objects.update_or_create(
        url=data['url'],
        defaults=data,
    )
