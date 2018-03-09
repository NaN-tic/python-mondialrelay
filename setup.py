#!/usr/bin/env python
#This file is part of mondialrelay. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages
import mondialrelay


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='mondialrelay',
        version=mondialrelay.__version__,
        author='NaN-TIC',
        author_email='info@nan-tic.com',
        url="https://www.nan-tic.com",
        description="Python API MondialRelay carrier",
        long_description=read('README'),
        download_url="https://bitbucket.org/nantic/python-mondialrelay",
        package_data={'mondialrelay': ['template/*']},
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        install_requires=[
            'genshi',
            ],
        license='GPL-3',
        extras_require={
        },
        # test_suite="mondialrelay.tests",
    )
