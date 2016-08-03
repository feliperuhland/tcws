# coding: utf-8

from rest_framework import serializers

from api import models


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Article


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Author
