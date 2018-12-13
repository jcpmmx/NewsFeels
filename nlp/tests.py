# coding=utf-8


import unittest

from nlp import watson


class WatsonTestCase(unittest.TestCase):
    """
    Tests cases for Watson as a NLP provider.
    """

    def test_get_sentiment(self):
        self.assertEqual(watson.get_sentiment('Im very happy')['label'], 'positive')
        self.assertEqual(watson.get_sentiment('Im very angry')['label'], 'negative')
        self.assertEqual(watson.get_sentiment('Im Julian, a software engineer from Colombia')['label'], 'neutral')


if __name__ == '__main__':
    unittest.main()
