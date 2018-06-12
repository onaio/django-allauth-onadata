# allauth_onadata

[![Build Status](https://travis-ci.org/onaio/django-allauth-onadata.svg?branch=master)](https://travis-ci.org/onaio/django-allauth-onadata)

[django-allauth](https://github.com/pennersr/django-allauth) provider for [Onadata](https://github.com/onaio/onadata) that enables OAuth2 authentication through Onadata servers like [ona.io](http://ona.io).

## Installation

1. Install and setup django-allauth as [usual](https://django-allauth.readthedocs.io/en/latest/installation.html)
2. Install allauth_onadata:
    ```sh
    pipenv install -e git+https://github.com/onaio/django-allauth-onadata.git#egg=allauth-onadata
    ```
3. Add `allauth_onadata` to your Django settings
4. Create an Oauth2 application at the Onadata server.  [Click here for instructions](https://api.ona.io/static/docs/authentication.html#using-oauth2-with-the-ona-api).  The redirect url that you input when you register your application with Onadata is `http://example.com/accounts/onadata/login/callback/` (replace http://example.com with your own domain, of course).
5. Set up a social application in your Django admin using the settings obtained above:
    ![allauth_onadata](https://user-images.githubusercontent.com/372073/41282568-0f2b4856-6e3d-11e8-8a1e-6703b88f2a17.png)

## Settings

```python

# the scope to send with the OAuth2 request
ALLAUTH_ONA_SCOPE = ['read', 'write', 'groups']
# the base URL of the onadata installation
ALLAUTH_ONA_BASE_URL = "https://api.ona.io"  # no trailing slash

```

## Testing

```sh

pip install -U tox

tox

```
