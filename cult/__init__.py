from grub import SearchStore as _SearchStore
from types import ModuleType
from importlib import import_module
from py2store import KvReader


# def list_sources():
#     import cult.sources
#
#     return list(filter(lambda x: isinstance(x, ModuleType),
#                        (getattr(cult.sources, x) for x in dir(cult.sources) if not x.startswith('_'))))


def list_sources():
    import cult.sources
    import os
    # TODO: Find better way to do this!
    py_files = filter(lambda x: x.endswith('.py') and not x.startswith('_'),
                      os.listdir(cult.sources.__path__[0]))
    return [x[:-3] for x in py_files]


class SearchTexts:
    def __iter__(self):
        yield from list_sources()

    def __getitem__(self, source):
        return SearchText(source)


from dataclasses import dataclass
from typing import Iterable


# @dataclass
# class Results:
#     store: KvReader
#     refs: Iterable
#
#     def print(self):
#         for i, verse_ref in enumerate(self.refs, 1):
#             verse_text = self.store[verse_ref]
#             print(f"{i}: {verse_ref}\n{verse_text}\n")
#
#     def __repr__(self):
#         return self.refs.__repr__()
#         # return f"Results(..., refs={self.refs.__repr__()})"

_inf = float('infinity')

# TODO: Use pattern/mixin to wrap existing mapping (verses)
class SearchText(KvReader):
    def __init__(self, source, search_max=10):
        # TODO: Better way to do this import thing?
        try:
            source_module = import_module('cult.sources' + '.' + source)
            verses = getattr(source_module, 'verses')
        except Exception as e:
            raise ValueError("Don't know that source: {source}\nError was: {e}")

        self.verses = verses
        self.searcher = _SearchStore(verses, n_neighbors=search_max)
        self.last_search_results = []

    def search(self, query):
        self.last_search_results = self.searcher(query)
        return self.last_search_results
        # return Results(self.verses, self.last_search_results)

    def print_verses(self, x=None, max_verses=_inf):
        verse_refs = self.verses  # default
        if isinstance(x, str):
            verse_refs = self.search(x)
        elif x is None:
            verse_refs = self.last_search_results
        else:
            verse_refs = x

        for i, verse_ref in enumerate(verse_refs, 1):
            if i > max_verses:
                break
            verse_text = self.verses[verse_ref]
            print(f"{i}: {verse_ref}\n{verse_text}\n")

    def __iter__(self):
        yield from self.verses

    def __getitem__(self, k):
        return self.verses[k]

    def __len__(self):
        return len(self.verses)

    def __contains__(self, k):
        return k in self.verses
