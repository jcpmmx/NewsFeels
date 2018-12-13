# coding=utf-8


import unittest

from sources.cnn.main import CNNSource


class CNNSourceTestCase(unittest.TestCase):
    """
    Tests cases for Watson as a NLP provider.
    """
    def setUp(self):
        self.articles_limit = 3
        self.cnn = CNNSource()
        self.cnn.ARTICLES_LIMIT = self.articles_limit

    def test_get_latest_data(self):
        articles_data = self.cnn.get_latest_data()
        self.assertEqual(len(articles_data), self.articles_limit)

        some_article_data = articles_data[0]
        self.assertEqual(len(some_article_data), 3)  # article_content, key_information, sentiment

        article_content, key_information, sentiment = some_article_data
        self.assertTrue(isinstance(story, str))
        self.assertTrue(isinstance(key_information, dict))
        self.assertTrue(isinstance(sentiment, dict))
        self.assertIn('title', key_information)
        self.assertIn('author', key_information)
        self.assertIn('published', key_information)
        self.assertIn('url', key_information)
        if article_content:
            self.assertIn('label', sentiment)
            self.assertIn('score', sentiment)


if __name__ == '__main__':
    unittest.main()
