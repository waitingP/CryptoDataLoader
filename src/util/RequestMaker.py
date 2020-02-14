from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class RequestMaker:
    def __init__(self):
        self.req_proxy = RequestProxy()

    def _generate_proxied_request(self, url, params=None):
        if params is None:
            params = {}
        for _ in range(0, len(self.req_proxy.get_proxy_list())):
            proxy_response = self.req_proxy.generate_proxied_request(url, params=params)
            if proxy_response is not None:
                return proxy_response
        return None

    def get(self, url, params=None):
        proxy_response = self._generate_proxied_request(url, params)
        if proxy_response is None:
            raise RuntimeError('Failed to generate proxied request for {}'.format(url))

        return proxy_response
