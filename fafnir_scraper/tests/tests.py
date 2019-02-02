"""Testing the thing

This module does tests
"""

from unittest import TestCase

import fafnir_scraper.fafnir_scraper as fafnir_scraper

class TestFafnirScraper(TestCase):
    """ Test class """
    def test_init_args(self):
        """Test class init with arguments"""
        scraper = fafnir_scraper.FafnirScraper("host", port="Port", https=False)
        self.assertTrue(scraper.host == "host")
        self.assertTrue(scraper.port == "Port")
        self.assertTrue(not scraper.https)

    def test_init_noargs(self):
        """Test class init with no arguments"""
        scraper = fafnir_scraper.FafnirScraper("host")
        self.assertTrue(scraper.host == "host")
        self.assertTrue(scraper.port is None)
        self.assertTrue(scraper.https)

    def test_connection_https(self):
        """Test class init with no arguments"""
        conn = fafnir_scraper.FafnirScraper("www.journaldev.com")
        self.assertTrue(conn.ping())
