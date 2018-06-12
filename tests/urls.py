# -*- coding: utf-8 -*-
"""
urls module for tests
"""
from __future__ import unicode_literals

import sys

if sys.version_info[0] < 3:
    from django.conf.urls import include, url as re_path
else:
    from django.urls import include, re_path

# pylint: disable=invalid-name
urlpatterns = [
    re_path(r'^accounts/', include('allauth.urls')),
]
