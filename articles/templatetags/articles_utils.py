# coding=utf-8


from django import template

register = template.Library()


@register.filter
def get_sentiment_bs_color(sentiment_label):
    """
    Returns a proper style name for Bootstrap colors for the given sentiment label.
    e.g. 'positive' --> 'success'
    """
    bs_color_names = {
        'positive': 'success',
        'negative': 'danger',
        'neutral': 'default',
    }
    return bs_color_names.get(sentiment_label, 'default')
