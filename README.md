
# cult

Religious texts search engine.

Sources the religious texts on-demand, from various on-line sources, but caches these locally. 

Texts can than be searched (on the verse level), using a tf-idf engine.

No database is needed. Texts are downloaded, stored in their raw format and uploaded and indexed in RAM, on demand.

# Examples

```python
from cult import SearchTexts, SearchText

search_texts = SearchTexts()
list(search_texts)
```



    ['bible', 'quaran', 'king_james_bible']



```python
bib = search_texts['bible']
print(f"{len(bib)} verses\n")
```

    31104 verses
    


```python
bib['John 1:1']
```


    'From the first he was the Word, and the Word was in relation with God and was God.'




```python
bib.search('search for words')
```




    array(['Ecclesiastes 12:10', 'Psalms 27:8', 'Psalms 44:21', 'Luke 2:45',
           'Psalms 119:155', 'Zephaniah 2:3', 'Luke 19:10', '1 Samuel 17:56',
           'Job 8:5', 'Psalms 105:4'], dtype='<U20')




```python
bib.print_verses('search for words')
```

    1: Ecclesiastes 12:10
    The Preacher made search for words which were pleasing, but his writing was in words upright and true.
    
    2: Psalms 27:8
    When you said, Make search for my face, my heart said to you, For your face will I make my search.
    
    3: Psalms 44:21
    Will not God make search for it? for he sees the secrets of the heart.
    
    4: Luke 2:45
    And seeing that he was not there, they went back to Jerusalem, to make search for him.
    
    5: Psalms 119:155
    Salvation is far from evil-doers; for they have made no search for your rules.
    
    6: Zephaniah 2:3
    Make search for the Lord, all you quiet ones of the earth, who have done what is right in his eyes; make search for righteousness and a quiet heart: it may be that you will be safely covered in the day of the Lord's wrath.
    
    7: Luke 19:10
    For the Son of man came to make search for those who are wandering from the way, and to be their Saviour.
    
    8: 1 Samuel 17:56
    And the king said, Make search and see whose son this young man is.
    
    9: Job 8:5
    If you will make search for God with care, and put your request before the Ruler of all;
    
    10: Psalms 105:4
    Let your search be for the Lord and for his strength; let your hearts ever be turned to him.
    



```python
qua = search_texts['quaran']
len(qua)
```




    6236




```python
qua.print_verses('search for words')
```

    1: 24:26
    Evil words are for evil men, and evil men are [subjected] to evil words. And good words are for good men, and good men are [an object] of good words. Those [good people] are declared innocent of what the slanderers say. For them is forgiveness and noble provision.
    
    2: 33:70
    O you who have believed, fear Allah and speak words of appropriate justice.
    
    3: 18:109
    Say, "If the sea were ink for [writing] the words of my Lord, the sea would be exhausted before the words of my Lord were exhausted, even if We brought the like of it as a supplement."
    
    4: 10:82
    And Allah will establish the truth by His words, even if the criminals dislike it."
    
    5: 12:76
    So he began [the search] with their bags before the bag of his brother; then he extracted it from the bag of his brother. Thus did We plan for Joseph. He could not have taken his brother within the religion of the king except that Allah willed. We raise in degrees whom We will, but over every possessor of knowledge is one [more] knowing.
    
    6: 10:64
    For them are good tidings in the worldly life and in the Hereafter. No change is there in the words of Allah. That is what is the great attainment.
    
    7: 47:21
    Obedience and good words. And when the matter [of fighting] was determined, if they had been true to Allah, it would have been better for them.
    
    8: 73:6
    Indeed, the hours of the night are more effective for concurrence [of heart and tongue] and more suitable for words.
    
    9: 25:75
    Those will be awarded the Chamber for what they patiently endured, and they will be received therein with greetings and [words of] peace.
    
    10: 7:162
    But those who wronged among them changed [the words] to a statement other than that which had been said to them. So We sent upon them a punishment from the sky for the wrong that they were doing.
    
