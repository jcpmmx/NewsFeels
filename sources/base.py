# coding=utf-8


from dateutil.parser import parse as dt_parse

from django.conf import settings

from newsfeels.utils import get_json, get_text
from nlp import watson


class NewsAPISource(object):
    """
    Class that wraps all logic required to extract data from News API.
    """
    BASE_URL = 'https://newsapi.org/v2/everything'
    SOURCE = None  # Must be a valid News API value (e.g. cnn, the-verge)

    ARTICLES_LIMIT = 33  # How many articles to fetch each time
    ARTICLE_CONTENT_XPATH = None  # Valid XPath pointing to an HTML element with an article's content

    def __init__(self, allow_print=False):
        self.allow_print = allow_print
        if not self.SOURCE:
            raise ValueError('You need to specify a valid value for SOURCE')
        if not self.ARTICLE_CONTENT_XPATH:
            raise ValueError('You need to specify a valid value for ARTICLE_CONTENT_XPATH')

    def get_latest_data(self):
        """
        Returns a list of of the latest HN stories from HN, each one representing a HN story,
        """
          # TODO(Julian): We should cache this request hourly or daily
        params = {'sources': self.SOURCE, 'language': 'en'}
        headers = {'X-Api-Key': settings.NEWSAPI_API_KEY}
        json_data = get_json(self.BASE_URL, params=params, headers=headers)

        if json_data and json_data['status'] == 'ok':
            # TODO(Julian): Check if we already parsed stories (using a DB table), or process and store them otherwise
            for story_data in json_data['articles'][:self.ARTICLES_LIMIT]:
                self._get_feels(story_data)

    def _get_feels(self, story_data):
        """
        Returns a dict with all feels of the given story: the story itself, key information (title, author, publishing 
        date and time) and sentiment.
        """
        story = get_text(story_data.get('url'), xpath=self.ARTICLE_CONTENT_XPATH)
        key_information = {
            'title': story_data['title'],
            'author': story_data['author'],
            'published': dt_parse(story_data['publishedAt']),  # In UTC
            'url': story_data['url'],
        }
        sentiment = watson.get_sentiment(story)

        if self.allow_print:
            print('-------')
            print('{} --- By {} ({})'.format(
                key_information['title'], key_information['author'] or '(Unknown)', key_information['published'])
            )
            if story:
                print('Sentiment: {} ({})'.format(sentiment['label'].title(), sentiment['score']))
            else:
                print("(Article content couldn't be retrieved)")
            print('-------')

        return story, key_information, sentiment
