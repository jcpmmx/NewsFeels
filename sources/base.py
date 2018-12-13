# coding=utf-8


from dateutil.parser import parse as dt_parse

from django.conf import settings

from newsfeels.settings.enums import ArticleSource
from newsfeels.utils import get_json, get_text
from nlp import watson


class NewsAPISource(object):
    """
    Class that wraps all logic required to extract data from News API.
    """
    BASE_URL = 'https://newsapi.org/v2/everything'
    SOURCE = None  # Must be a valid News API value (e.g. cnn, the-verge)

    ARTICLES_LIMIT = 3  # How many articles to process each time
    ARTICLE_CONTENT_XPATH = None  # Valid XPath pointing to an HTML element with an article's content

    def __init__(self, allow_print=False):
        self.allow_print = allow_print
        if not self.SOURCE or not isinstance(self.SOURCE, ArticleSource):
            raise ValueError('You need to specify a valid value for SOURCE')
        if not self.ARTICLE_CONTENT_XPATH:
            raise ValueError('You need to specify a valid value for ARTICLE_CONTENT_XPATH')

    def get_latest_data(self):
        """
        Returns a list of 3-tuple with data from the latest articles from the current source.

        Each article is retrieved via News API before its content is pulled from its original source via so we can 
        analyze it.
        """
        available_articles = []

        # TODO(Julian): We should cache this request hourly or daily
        params = {'sources': self.SOURCE.value, 'language': 'en'}
        headers = {'X-Api-Key': settings.NEWSAPI_API_KEY}
        json_data = get_json(self.BASE_URL, params=params, headers=headers)

        if json_data and json_data['status'] == 'ok':
            # TODO(Julian): Check if we already parsed stories (using a DB table), or process and store them otherwise
            for article_data in json_data['articles'][:self.ARTICLES_LIMIT]:
                available_articles.append(self._get_feels(article_data))
        return available_articles

    def _get_feels(self, article_data):
        """
        Returns a 3-tuple with all feels of the given article: the article itself, key information (title, author, 
        publishing date and time, URL) and sentiment.

        The returned 3-tuple follows these conventions:
        - Article itself is a string with its contents as text
        - Key information is a dict with the following keys: title (str), author (str), published (datetime), url (str)
        - Sentiment is a dict with `label` (one of 'positive', 'negative' and 'neutral') and `score`
        """
        article_content = get_text(article_data.get('url'), xpath=self.ARTICLE_CONTENT_XPATH) or '(None)'
        key_information = {
            'title': article_data['title'],
            'author': article_data['author'] or '(Unknown)',
            'published': dt_parse(article_data['publishedAt']),  # In UTC
            'url': article_data['url'],
        }
        sentiment = watson.get_sentiment(article_content)

        if self.allow_print:
            print('-------')
            print('{} --- By {} ({})'.format(
                key_information['title'], key_information['author'], key_information['published'])
            )
            print('Sentiment: {} ({})'.format(sentiment['label'].title(), sentiment['score']))
            print('-------')

        return article_content, key_information, sentiment
