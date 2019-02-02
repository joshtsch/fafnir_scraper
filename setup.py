#!/usr/bin/env python

"""This is the setup module for Fafnir FafnirScraper

This module does the thing.
"""

from setuptools import setup

with open("README.md", "r") as readme:
    README = readme.read()
with open("requirements.txt", "r") as require:
    REQUIREMENTS = require.read()
with open("requirements_dev.txt", "r") as require_dev:
    REQUIREMENTS_DEV = require_dev.read()

setup(
    name='fafnir_scraper',
    version='1.0.0',
    author='Josh Tscheschlog',
    author_email='jlt5389@gmail.com',
    description='',
    long_description=README,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/jlt5389/fafnir',
    packages=['fafnir_scraper'],
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    tests_require=REQUIREMENTS_DEV,
    test_suite='nose.collector',
)
