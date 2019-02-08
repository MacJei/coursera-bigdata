from __future__ import print_function
import sys
import re


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'stop_words_en.txt'

stopWords = set()

with open(path) as stopWordsFile:
    for line in stopWordsFile:
        try:         
            stopWords.add(unicode(line.strip()))
        except ValueError as e:
            continue

import string

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue

    words = re.split("\W*\s+\W*", text.lower(), flags=re.UNICODE)
    
    wordsInArticle = 0
    
    for word in words:
        word = word.strip(string.punctuation)
        if word in stopWords:
            print("reporter:counter:Wiki stats,Stop words found,%d" % 1, file=sys.stderr)
            continue
        if word == "":
            print("reporter:counter:Wiki stats,Null words found,%d" % 1, file=sys.stderr)
            continue
        wordsInArticle += 1
        print("reporter:counter:Wiki stats,Total words found,%d" % 1, file=sys.stderr)
        print(article_id, word.strip(string.punctuation), 1, sep='\t')
    print(article_id, "!wordsInArticle", wordsInArticle, sep='\t')

