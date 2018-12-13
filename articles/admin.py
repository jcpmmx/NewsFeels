# coding=utf-8


from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    Admin interface for the Article model.
    """
    list_display = ('id', 'source', 'title', 'author', 'published', 'get_sentiment_description')
    list_display_links = ('id', 'title')
    list_filter = ('source', 'published', 'created', 'modified')
    search_fields = ('source', 'title', 'author', 'content')

    fieldsets = (
        (None, {
            'fields': ('source', 'external_id', 'created', 'modified')
        }),
        ('Article', {
            'fields': ('title', 'author', 'published', 'url', 'content')
        }),
        ('Sentiment', {
            'fields': ('sentiment_label', 'sentiment_score')
        }),
    )
    readonly_fields = ('external_id', 'created', 'modified')

    def get_sentiment_description(self, obj):
        return obj.get_sentiment_description()
    get_sentiment_description.short_description = 'Sentiment'


admin.site.register(Article, ArticleAdmin)
