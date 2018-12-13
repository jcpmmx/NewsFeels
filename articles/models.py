# coding=utf-8


import hashlib
from uuid import UUID

from django.db import models

from newsfeels.settings.enums import ArticleSource, Sentiment


class Article(models.Model):
    """
    Model that represents an article that has been analyzed already.
    """
    source = models.CharField(max_length=10, choices=ArticleSource.choices())
    external_id = models.CharField(max_length=32, unique=True, editable=False)

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published = models.DateTimeField()
    url = models.URLField('URL')
    content = models.TextField()
    sentiment_label = models.CharField(max_length=10, choices=Sentiment.choices())
    sentiment_score = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source', 'external_id')
        ordering = ('-published',)

    def __str__(self):
        return '({}) {}'.format(self.get_source_display(), self.title)

    def __repr__(self):
        return '<Article "{}">'.format(self)

    def save(self, *args, **kwargs):
        if not self.external_id:
            uuid_components = (self.source, self.title, self.author, self.published, self.url)
            self.external_id = self._generate_hash(*uuid_components)
        super().save(*args, **kwargs)

    def get_sentiment_percentage(self):
        """
        Returns the sentiment score as a percentage value (form 0 to 100).
        e.g. -0.65 --> 65
        """
        return abs(self.sentiment_score)*100

    def get_sentiment_description(self):
        """
        Returns the sentiment as a nicely formatted string.
        e.g. "Positive (1.00)"
        """
        return '{} ({:.2f})'.format(self.get_sentiment_label_display(), self.sentiment_score)

    @classmethod
    def create_articles(cls, source, available_articles):
        """
        Takes a list of 3-tuple with data from articles and creates new DB records, if articles are new.
        """
        current_count = cls.objects.all().count()

        for article_content, key_information, sentiment in available_articles:
            title = key_information['title']
            author = key_information['author']
            published = key_information['published']
            url = key_information['url']
            possible_external_id = cls._generate_hash(source, title, author, published, url)

            if not cls.objects.filter(external_id=possible_external_id).exists() and article_content:
                data = {
                    'source': source,
                    'external_id': possible_external_id,
                    'title': title,
                    'author': author,
                    'published': published,
                    'url': url,
                    'content': article_content,
                    'sentiment_label': sentiment['label'],
                    'sentiment_score': sentiment['score'],
                }
                cls.objects.create(**data)

        new_count = cls.objects.all().count()
        some_article_created = current_count != new_count
        return some_article_created

    @staticmethod
    def _generate_hash(source, title, author, published, url):
        source_data = ''.join(str(x) for x in [source, title, author, published, url]).encode('utf-8')
        return hashlib.md5(source_data).hexdigest()