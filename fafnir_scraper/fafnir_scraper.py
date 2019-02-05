"""Ahh the blah module...

This module does blah blah blah
"""

import logging
import http.client

class FafnirScraper():
    """ Fafnir Scraper class """
    def __init__(self, host, **kwargs):
        self.host = host
        if kwargs is not None:
            try:
                self.port = kwargs["port"]
            except KeyError:
                self.port = None
            try:
                self.https = kwargs["https"]
            except KeyError:
                self.https = True

        logging.info("Host: %s", self.host)
        logging.info("Port: %s", self.port)
        logging.info("HTTPS: %s", self.https)

    def connection(self):
        """Return server connection instance"""
        if not self.https:
            return http.client.HTTPConnection(self.host, self.port)
        else:
            return http.client.HTTPSConnection(self.host, self.port)

    def ping(self):
        return self.connection().request("GET", "/")
