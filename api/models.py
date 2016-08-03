# coding: utf-8

from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=60, blank=True)
    profile_url = models.URLField(blank=True, null=True)
    twitter_account = models.CharField(max_length=100, blank=True, null=True)
    resume = models.TextField(blank=True)


class Article(BaseModel):
    url = models.URLField()
    posted = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    author = models.ForeignKey(Author)
