# coding=utf-8


import logging

import requests
from requests_html import HTMLSession

logger = logging.getLogger(__name__)


def get_json(url, method='get', **kwargs):
    """
    Returns the available JSON response as a dict (if any) for the given URL, data and HTTP method.
    """
    try:
        response = _get_requests_method(method)(url, **kwargs)
        response.raise_for_status()
        return response.json()

    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        logger.error('[get_json] Error when trying "%s" to "%s": %s', method, url, str(e))
        return {}


def get_text(url, xpath=None):
    """
    Returns the available text from a given URL.
    """
    try:
        response = HTMLSession().get(url)
        response.raise_for_status()
        if xpath:
            return response.html.xpath(xpath, first=True).text
        return response.html.text

    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        logger.error('[get_text] Error when trying "%s": %s', url, str(e))
        return ''


def _get_requests_method(method='get'):
    """
    Returns the requests method to call as given by `method`.
    """
    _AVAILABLE_METHODS_MAP = {
        'get': requests.get,
    }
    return _AVAILABLE_METHODS_MAP.get(method, lambda url, kwargs: None)
