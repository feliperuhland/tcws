# coding: utf-8

from rest_framework import viewsets

from api import serializers, models


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all().order_by('posted')

    def get_queryset(self):
        author_id = self.request.query_params.get('author_id', None)
        queryset = models.Article.objects.all().order_by('posted')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all().order_by('name')
    serializer_class = serializers.AuthorSerializer
