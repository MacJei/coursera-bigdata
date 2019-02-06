from __future__ import print_function
import sys


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'idf.csv'

idfWords = []

with open(path) as idfWordsFile:
    for line in idfWordsFile:
        try:
            word, v = line.split('\t')
            idf = float(v)
            idfWords.append([word, idf])
        except ValueError as e:
            continue
#print(idfWords)


for line in sys.stdin:
    try:
        article_id, tfWord, v = unicode(line.strip()).split('\t')
        tf = float(v)
    except ValueError as e:
        print("reporter:counter:Wiki stats,tf to float errors,%d" % 1, file=sys.stderr)
        continue

    #idfWord = next((w for w in idfWords if tfWord in w), [])
    idx = 0
    idf = None

    for w in idfWords:
        if w[0] == tfWord:
            idf = w[1]
            break

    #if len(idfWord) == 0:
    if idf == None:
        print("reporter:counter:Wiki stats,Unfound tf into idf words,%d" % 1, file=sys.stderr)
        continue
    #idf = idfWord[1]
    print("reporter:counter:Wiki stats,tf*idf words,%d" % 1, file=sys.stderr)
    print(tfWord, article_id, tf, idf, tf*idf, sep='\t')
    #print(tfWord, article_id, tf*idf, sep='\t')
