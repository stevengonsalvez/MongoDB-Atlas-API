#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os


from setuptools import find_packages, setup

from mongodbatlas.version import __VERSION__

# Package meta-data.
NAME = 'mongodbatlas'
DESCRIPTION = 'Python API to the MongoDB Atlas REST Interface'
URL = 'https://github.com/jdrumgoole/MongoDB-Atlas-API'
EMAIL = 'joe@joedrumgoole.com'
AUTHOR = 'Joe Drumgoole'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = __VERSION__


# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION



# Where the magic happens:
setup(
    name=NAME,
    version="0.2.3b2",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=['requests',
                      'dateutils'],
    packages=find_packages(),
    tests_require=["nose"],
    license='Apache 2.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    entry_points={
        'console_scripts': [
            'atlascli=mongodbatlas.atlascli:main',
        ]},
    test_suite='nose.collector',
)
