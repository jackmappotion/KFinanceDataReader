import urllib
import requests

class DartFetcher:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = 'https://opendart.fss.or.kr'
        self.base_params = {'crtfc_key': api_key}

    def format_url(self, detail_url):
        url = urllib.parse.urljoin(self.base_url, detail_url)
        return url

    def format_params(self, **detail_params):
        params = {**self.base_params, **detail_params}
        return params

    def get_request_params(self, detail_url, **detail_params):
        request_params = {
            "url": self.format_url(detail_url),
            "params": self.format_params(**detail_params),
        }
        return request_params

    def get_resp(self, detail_url, **detail_params):
        try:
            resp = requests.get(**self.get_request_params(detail_url, **detail_params))
            return resp
        except requests.exceptions.SSLError:
            print('SSL error occurred: might be a problem with the [IP or SSL certification.]')
            return None

        except requests.exceptions.HTTPError:
            print(
                'HTTP error occurred: might be a problem with the [internet connection or the server].'
            )
            return None
