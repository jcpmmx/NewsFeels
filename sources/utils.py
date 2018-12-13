# coding=utf-8


from articles.models import Article
from sources.cnn.main import CNNSource


def load_articles():
    """
    Method that loops among the available sources, gets articles and stores them in DB.
    """
    # TODO(Julian): This should be done async via task/queue, cron or or similar. Ideally, UI would wait for data to be 
    # ready or load it as it comes.
    _AVAILABLE_SOURCES = (
        CNNSource,
    )
    for source_class in _AVAILABLE_SOURCES:
        article_source = source_class()
        available_articles = article_source.get_latest_data()
        Article.create_articles(article_source.SOURCE.value, available_articles)
