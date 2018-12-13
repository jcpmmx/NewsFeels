# coding=utf-8


from enum import Enum


class ArticleSource(Enum):
    """
    Enum that represents all possible article sources.

    All values must be a valid inside News API (e.g. cnn, the-verge).
    """
    CNN = 'cnn'

    @classmethod
    def choices(cls):
        return ((s.value, s.name) for s in [cls.CNN])


class Sentiment(Enum):
    """
    Enum that represents all possible sentiment labels.
    """
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'

    @classmethod
    def choices(cls):
        return ((s.name, s.value) for s in [cls.POSITIVE, cls.NEGATIVE, cls.NEUTRAL])