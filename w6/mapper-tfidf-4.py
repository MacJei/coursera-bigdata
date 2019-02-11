from __future__ import print_function
import sys
import re
import string
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'stop_words_en.txt'
tagTf = 'tf'
tagIdf = 'idf'

stopWords = set()

with open(path) as stopWordsFile:
    for line in stopWordsFile:
        try:         
            stopWords.add(unicode(line.strip().lower()))
        except ValueError as e:
            continue

def calcTf(wordN, totalWordsN):
    return 1.0 * wordN/totalWordsN

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        print("reporter:counter:Wiki stats,Wrong articles found,%d" % 1, file=sys.stderr)
        continue

    text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)

    wordsN = Counter()

    wordsInArticle = 0

    for word in words:
        word = word.strip(string.punctuation).lower()
        if word == "":
            print("reporter:counter:Wiki stats,Null words found,%d" % 1, file=sys.stderr)
            continue
        if word in stopWords:
            print("reporter:counter:Wiki stats,Stop words found,%d" % 1, file=sys.stderr)
            continue
        wordsInArticle += 1
        print("reporter:counter:Wiki stats,Total words found,%d" % 1, file=sys.stderr)
        #print(article_id, tagWord, word, 1, sep='\t')
        wordsN[word] += 1

    for wordN in wordsN:
        count = wordsN.get(wordN)
        print(wordN, tagTf, article_id, "%.6f" % calcTf(count, wordsInArticle), sep='\t')
        print(wordN, tagIdf, '0', 1,  sep='\t')  # zero article_id never exists

