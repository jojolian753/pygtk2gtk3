#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys
from distutils import log

import pygtk2gtk3


# -----------------------------------------------------------------------------

pkg_name = pygtk2gtk3.__name__
pkg_version = pygtk2gtk3.__version__

long_desc = \
"""
Description is to come later
"""

# -----------------------------------------------------------------------------

requires = []

# -----------------------------------------------------------------------------

if sys.version_info < (2, 7):
    print('ERROR: {0} requires at least Python 2.7 to run.'.format(pkg_name))
    sys.exit(1)

# -----------------------------------------------------------------------------

setup(
    name=pkg_name,
    version=pkg_version,
    url='https://github.com/placidrage/pygtk2gtk3',
    download_url='https://github.com/placidrage/pygtk2gtk3',
    license='GPLv3',
    author='Joe R. Nassimian',
    author_email='nassimian.joseph@gmail.com',
    description="2to3 fixers to convert from pygtk to gtk3",
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Production/Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=requires,
)

# -----------------------------------------------------------------------------
