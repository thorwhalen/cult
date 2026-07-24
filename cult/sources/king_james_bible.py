"""King James Bible (``en_kjv``) verse source.

Exposes a ``verses`` mapping of ``"Book chapter:verse" -> verse_text``.

The verse data is fetched lazily from a public JSON dataset on first access
to ``verses`` (via :pep:`562` module ``__getattr__``), so merely importing
this module performs **no** network I/O. This keeps test collection (e.g.
``pytest --doctest-modules``) network-free.
"""

from cult.util import get_url_and_return_py_json

url = (
    "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/" + "en_kjv.json"
)

_cache = {}


def json_contents_to_verse_items(json_contents):
    """Yield ``(ref, verse_text)`` pairs from the raw JSON contents."""
    for x in json_contents:
        name, chapters = x["name"], x["chapters"]
        for chapter_num, verses in enumerate(chapters, 1):
            for verse_num, verse in enumerate(verses, 1):
                yield (f"{name} {chapter_num}:{verse_num}", verse)


def _get_verses():
    """Fetch (once) and return the ``ref -> verse_text`` mapping."""
    if "verses" not in _cache:
        json_contents = get_url_and_return_py_json(url)
        _cache["verses"] = dict(json_contents_to_verse_items(json_contents))
    return _cache["verses"]


def __getattr__(name):
    """Lazily provide ``verses``/``json_contents`` without import-time network I/O."""
    if name == "verses":
        return _get_verses()
    if name == "json_contents":
        return get_url_and_return_py_json(url)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
