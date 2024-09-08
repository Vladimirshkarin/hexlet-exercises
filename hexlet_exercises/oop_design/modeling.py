from urllib.parse import urlparse, parse_qs


# BEGIN (write your solution here)
class Url:
    def __init__(self, url):
        self.parsed_url = urlparse(url)
        self.url_dict = {
            "scheme": self.parsed_url.scheme,
            "netloc": self.parsed_url.netloc,
            "path": self.parsed_url.path,
            "params": self.parsed_url.params,
            "query": parse_qs(self.parsed_url.query),
            "fragment": self.parsed_url.fragment,
            "username": self.parsed_url.username,
            "password": self.parsed_url.password,
            "hostname": self.parsed_url.hostname,
            "port": self.parsed_url.port,
        }

    def get_scheme(self):
        return self.url_dict["scheme"]

    def get_hostname(self):
        return self.url_dict["hostname"]

    def get_query_params(self):
        return self.url_dict["query"]

    def get_query_param(self, key, default_value=None):
        value = self.url_dict["query"].get(key, default_value)
        if isinstance(value, list):
            return ", ".join(value)
        return value

    def __eq__(self, other_obj):
        if isinstance(other_obj, Url):
            return self.url_dict == other_obj.url_dict
        else:
            return False
# END


# BEGIN reference solution
class Url_ref:
    def __init__(self, url):
        self.url = urlparse(url)
        self.query_params = {}

        if self.url.query:
            self.query_params = parse_qs(self.url.query)

    def get_scheme(self):
        return self.url.scheme

    def get_hostname(self):
        return self.url.hostname

    def get_query_params(self):
        return self.query_params

    def get_query_param(self, key, default_value=None):
        return self.query_params.get(key, [default_value])[0]

    def __eq__(self, other):
        return self.url == other.url
# END reference solution
