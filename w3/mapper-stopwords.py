import sys
import re


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'stop_words_en.txt'

# Your code for reading stop words here
stopWords = open(path).read().lower().split()

wordSum, stopWordSum = 0, 0

for line in sys.stdin:
    try:
        article_id, text = unicode(line.lower().strip()).split('\t', 1)
    except ValueError as e:
        continue

    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    #print words
    # Your code for mapper here.
    for word in words:
        if word in stopWords:
            stopWordSum += 1
            #print >> sys.stderr, "reporter:counter:Stop words,1"
        wordSum += 1
        #print >> sys.stderr, "reporter:counter:Total words, 1"
    #wordSum += len(words) 
       
print >> sys.stderr, "reporter:counter:Total words,twords,%d" % wordSum
print >> sys.stderr, "reporter:counter:Stop words,swords,%d" % stopWordSum

print "wordSum-stopWordSum\t%d\t%d" % (wordSum, stopWordSum)
