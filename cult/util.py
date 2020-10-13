import json
from graze import Graze

graze_url = Graze()


def get_url_contents(url):
    return graze_url[url]


def get_url_and_return_py_json(url):
    return json.loads(get_url_contents(url))

