# coding=utf-8


from django.views import generic

from sources.utils import load_articles

from .models import Article


class IndexView(generic.ListView):
    """
    Main view of the `articles` app.
    """
    template_name = 'articles/index.html'

    def get_queryset(self):
        # load_articles()  # To populate the DB with articles and their analysis
        return Article.objects.all()
