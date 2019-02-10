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

stopWords = Counter()

with open(path) as stopWordsFile:
    for line in stopWordsFile:
        try:         
            stopWords[unicode(line.strip().lower())] = 1
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
    words = [unicode(w.strip(string.punctuation)).lower() for w in words if w != ""]

    wordsC = Counter(words)
    wordsN = [(w, wordsC.get(w)) for w in wordsC if stopWords[w] == 0]
    
    wordsInArticle = len(wordsN)
    
    for word in wordsN:
        if word[0] == "":
            print("reporter:counter:Wiki stats,Null words found,%d" % 1, file=sys.stderr)
            continue

        print("reporter:counter:Wiki stats,Total words found,%d" % 1, file=sys.stderr)
        print(word[0], tagTf, article_id, calcTf(word[1], wordsInArticle), sep='\t')
        print(word[0], tagIdf, '0', 1,  sep='\t')  # zero article_id never exists
