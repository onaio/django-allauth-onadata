# -*- coding: utf-8 -*-
"""
allauth_onadata app views module
"""
from __future__ import unicode_literals

from django.conf import settings

import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2CallbackView,
                                                          OAuth2LoginView)

from .provider import OnadataProvider

BASE_URL = getattr(settings, 'ALLAUTH_ONA_BASE_URL', "https://api.ona.io")


class OnadataOAuth2Adapter(OAuth2Adapter):
    """
    Onadata OAuth2 adapter
    """
    provider_id = OnadataProvider.id
    access_token_url = '{}/o/token/'.format(BASE_URL)
    authorize_url = '{}/o/authorize/'.format(BASE_URL)
    profile_url = '{}/api/v1/user.json'.format(BASE_URL)

    def complete_login(self, request, app, access_token, **kwargs):
        """
        Complete the login
        """
        headers = {'Authorization': 'Bearer {}'.format(access_token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


# pylint: disable=invalid-name
oauth2_login = OAuth2LoginView.adapter_view(OnadataOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(OnadataOAuth2Adapter)
