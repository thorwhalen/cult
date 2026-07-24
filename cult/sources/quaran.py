"""Quran (English translation) verse source.

Exposes a ``verses`` mapping of ``"surah:verse" -> verse_translation``.

The verse data is fetched lazily from the ``risan/quran-json`` dataset on
first access to ``verses`` (via :pep:`562` module ``__getattr__``), so merely
importing this module performs **no** network I/O. This keeps test collection
(e.g. ``pytest --doctest-modules``) network-free.

Note: the data is sourced from the current ``main``-branch layout of
``risan/quran-json`` (``dist/quran_en.json``), a list of surah objects each
carrying an ``id`` and a list of ``verses`` (each verse having an ``id`` and a
``translation``).
"""

from cult.util import get_url_and_return_py_json

url = "https://raw.githubusercontent.com/risan/quran-json/main/dist/quran_en.json"

_cache = {}


def json_contents_to_verse_items(json_contents):
    """Yield ``("surah:verse", translation)`` pairs from the raw JSON contents.

    ``json_contents`` is a list of surah objects, each with an ``id`` and a
    ``verses`` list whose items have an ``id`` and a ``translation``.
    """
    for surah in json_contents:
        surah_num = surah["id"]
        for verse in surah["verses"]:
            verse_num = verse["id"]
            yield (f"{surah_num}:{verse_num}", verse["translation"])


def _get_verses():
    """Fetch (once) and return the ``ref -> verse_translation`` mapping."""
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
