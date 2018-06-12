# -*- coding: utf-8 -*-
"""
allauth_onadata app urls module
"""
from __future__ import unicode_literals

from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import OnadataProvider

# pylint: disable=invalid-name
urlpatterns = default_urlpatterns(OnadataProvider)
