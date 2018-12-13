# coding=utf-8


from django.http import HttpResponse
from django.views import generic

from sources.utils import load_articles

from .models import Article


class IndexView(generic.ListView):
    """
    Main view of the `articles` app.
    """
    template_name = 'articles/index.html'

    def get_queryset(self):
        return Article.objects.all()


def load(request):
    """
    Small view that triggers the process for pulling articles and analyzing them.
    """
    if load_articles():
        return HttpResponse('OK')
    return HttpResponse(status=204)