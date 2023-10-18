# coding: utf-8

"""
    PlayHT API

    The PlayHT's API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devs@play.ht
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "playht"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="PlayHT API",
    author_email="devs@play.ht",
    url="",
    keywords=["Swagger", "PlayHT API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The PlayHT&#x27;s API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.  # noqa: E501
    """
)
