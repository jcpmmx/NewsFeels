# coding=utf-8


import logging

from django.conf import settings
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

_logger = logging.getLogger(__name__)
_watson_nlu = NLU(
    url=settings.IBM_CLOUD_API_ENDPOINT,
    iam_apikey=settings.IBM_CLOUD_API_KEY,
    version=settings.IBM_CLOUD_API_VERSION
)

def get_sentiment(text):
    """
    Returns the sentiment of the given text, as a dict with label and score.
    """
    try:
        if text:
            return _watson_nlu.analyze(
                text=text,
                features=Features(sentiment=SentimentOptions())
            ).get_result()['sentiment']['document']

    except Exception as e:
        _logger.error('[get_sentiment] Error when trying with "%s...": %s', text[:100], str(e))
    return {}
