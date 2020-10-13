from cult.util import get_url_and_return_py_json

url = 'https://raw.githubusercontent.com/thiagobodruk/bible/master/json/' + 'en_kjv.json'


def json_contents_to_verse_items(json_contents):
    for x in json_contents:
        name, chapters = x['name'], x['chapters']
        for chapter_num, verses in enumerate(chapters, 1):
            for verse_num, verse in enumerate(verses, 1):
                yield (
                    f"{name} {chapter_num}:{verse_num}",
                    verse
                )


json_contents = get_url_and_return_py_json(url)

verses = dict(json_contents_to_verse_items(json_contents))
