# -*- coding: utf-8 -*-
"""
allauth_onadata provider module
"""
from __future__ import unicode_literals
from django.conf import settings
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

SCOPE = getattr(settings, 'ALLAUTH_ONA_SCOPE', ['read', 'write', 'groups'])


class OnadataAccount(ProviderAccount):
    """
    Onadata Provider Account
    """

    def get_profile_url(self):
        """
        get the profile URL at ona.io
        """
        return self.account.extra_data.get('url')

    def get_avatar_url(self):
        """
        Get the profile image url
        """
        return self.account.extra_data.get('gravatar')

    def to_str(self):
        """
        String representation of profile
        """
        return self.account.extra_data.get('username')


class OnadataProvider(OAuth2Provider):
    """
    Onadata Provider
    """
    id = 'onadata'
    name = 'Onadata'
    account_class = OnadataAccount

    def get_default_scope(self):
        """
        Default scope
        """
        return SCOPE

    def extract_uid(self, data):
        """
        Extract unique user identifier
        """
        return data['username']

    def extract_common_fields(self, data):
        """
        Set the common fields expected by auth.User
        """
        first_name = ''
        last_name = ''
        if data.get('name') is not None:
            names = data.get('name').split(" ")
            first_name = names[0]
            if len(names) > 1:
                last_name = ' '.join(names[1:])

        return dict(
            email=data.get('email'),
            username=data.get('username'),
            first_name=first_name,
            last_name=last_name
        )


provider_classes = [OnadataProvider]  # pylint: disable=invalid-name
