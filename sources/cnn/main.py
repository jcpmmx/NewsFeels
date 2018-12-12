# coding=utf-8


from sources.base import NewsAPISource


class CNNSource(NewsAPISource):
    """
    Class that sets CNN as a valid News API source.
    """
    SOURCE = 'cnn'
    ARTICLES_LIMIT = 3
    ARTICLE_CONTENT_XPATH = '/html/body//div[@itemprop="articleBody"]'

    def _get_feels(self, story_data):
        # Just an exmaple to show that we could do some CNN-only post-processing here
        story, key_information, sentiment = super()._get_feels(story_data)
        key_information['author'] = key_information['author'].split(',', maxsplit=1)[0]
        return story, key_information, sentiment


# For testing purposes
if __name__ == '__main__':
    cnn = CNNSource()
    cnn.get_latest_data()
