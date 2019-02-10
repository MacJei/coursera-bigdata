import sys
from math import log

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

current_article_id = None
current_word = None

wordIdfSum = 0

tagIdf = 'idf'
tagTf = 'tf'

def calcIdf(wordDt):
    return 1.0/log(1.0 + wordDt)

def calcTfIdf(tf, idf):
    return 1.0*tf*idf

for line in sys.stdin:
    try:
        word, tag, article_id, count = unicode(line.strip()).split('\t')
        #print "after parse:", word, tag, article_id, count
        if article_id == "" or tag == "" or word == "" or count == "":   # sanity check
            continue    # skip
        if tag == tagIdf: count = int(count)
        if tag == tagTf:  count = float(count)
    except ValueError as e:
        print "Parse error:", e
        continue        # skip
        

    if current_word != word:
        wordIdfSum = 0
        current_word = word
    
    if tag == tagIdf:
        wordIdfSum += count

    if tag == tagTf:
        #print word, current_word, tagIdf, "wordIdfSum", wordIdfSum
        print "%s\t%s\t%f" % (current_word, article_id, calcTfIdf(count, calcIdf(wordIdfSum)))
