import os
from setuptools import setup

setup(
    name = "deploycron",
    version = "0.0.1",
    author = "monklof",
    author_email = "monklof@gmail.com",
    description = ("a small crontab deploy/install tool for python"),
    license = "MIT",
    keywords = "crontab, cron, initialize",
    url = "https://github.com/monklof/deploycron",
    packages=['deploycron', 'tests'],
    test_suite = 'nose.collector',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
