# -*- coding: utf-8 -*-
"""
Settings for tests
"""
from __future__ import unicode_literals

from setuptools import find_packages, setup

setup(
    name='allauth_onadata',
    version=__import__('allauth_onadata').__version__,
    description='A Django app that provides adds tasking to your Django '
    'project.',
    license='Apache 2.0',
    author='Ona Kenya',
    author_email='tech@ona.io',
    url='https://github.com/onaio/allauth-onadata',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'Django >= 1.11',
        'django-allauth >= 0.31.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
    ],
)
