from cult.util import get_url_and_return_py_json

url = 'https://raw.githubusercontent.com/risan/quran-json/master/json/quran/en.json'


def json_contents_to_verse_items(json_contents):
    for x in json_contents:
        chapter_num, verse_num, verse = x['surah_number'], x['verse_number'], x['translation']
        yield (
            f"{chapter_num}:{verse_num}",
            verse
        )


json_contents = get_url_and_return_py_json(url)

verses = dict(json_contents_to_verse_items(json_contents))
