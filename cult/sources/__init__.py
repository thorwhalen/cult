"""Verse sources for :mod:`cult`.

Each submodule here (e.g. :mod:`cult.sources.bible`,
:mod:`cult.sources.king_james_bible`, :mod:`cult.sources.quaran`) exposes a
``verses`` mapping of ``reference -> text``. Sources fetch their data lazily,
so importing a source module performs no network I/O until ``verses`` is
accessed.
"""
