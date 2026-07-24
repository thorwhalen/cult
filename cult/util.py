"""Utilities for :mod:`cult` — cached URL fetching and JSON decoding.

Uses :class:`graze.Graze` to fetch (and locally cache) remote URL contents,
so repeated access to a source dataset does not re-download it.
"""

import json
from graze import Graze

graze_url = Graze()


def get_url_contents(url):
    """Return the (locally cached) raw bytes/contents of ``url``."""
    return graze_url[url]


def get_url_and_return_py_json(url):
    """Fetch ``url`` and decode its contents as JSON into Python objects."""
    return json.loads(get_url_contents(url))
