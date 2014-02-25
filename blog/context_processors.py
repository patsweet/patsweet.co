def facebook(request):
    """
    Returns a template variable to access the facebook app id.
    """
    from django.conf import settings
    return {'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID}


def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'

    return {'BASE_URL': scheme + request.get_host()}
