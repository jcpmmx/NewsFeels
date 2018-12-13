# coding=utf-8


from newsfeels.settings.enums import ArticleSource
from sources.base import NewsAPISource


class CNNSource(NewsAPISource):
    """
    Class that sets CNN as a valid News API source.
    """
    SOURCE = ArticleSource.CNN
    ARTICLE_CONTENT_XPATH = '/html/body//div[@itemprop="articleBody"]'

    def _get_feels(self, article_data):
        """
        Just an example to show that we could do some CNN-only post-processing here.
        If not needed, then a new source would be as simple as a new class with proper SOURCE and ARTICLE_CONTENT_XPATH.
        """
        article_content, key_information, sentiment = super()._get_feels(article_data)
        if key_information['author']:
            key_information['author'] = key_information['author'].split(',', maxsplit=1)[0]
        return article_content, key_information, sentiment


# For testing purposes
if __name__ == '__main__':
    cnn = CNNSource(allow_print=True)
    cnn.get_latest_data()
