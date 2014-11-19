from pkg_resources import resource_string


def get_asset(filename):
    return resource_string('ftw.crawler.tests.assets', filename)


class MockRequest(object):

    def __init__(self, url='http://example.org'):
        self.url = url


class MockResponse(object):

    def __init__(self, content=None, status_code=200, headers=None,
                 request=None):
        self.content = content
        self.status_code = status_code

        if headers is None:
            headers = {}
        self.headers = headers

        if request is None:
            request = MockRequest()
        self.request = request