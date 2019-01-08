import sys

totalWords, totalStopWords = 0, 0

for line in sys.stdin:
    #print line.strip().split('\t')
    try:
        _, wordSum, stopWordSum = line.strip().split('\t')
    except:
        continue
    print wordSum, stopWordSum
    totalWords += int(wordSum)
    totalStopWords += int(stopWordSum)
    
print "wordSum-stopWordSum\t%d\t%d" % (totalWords, totalStopWords)
print "stop WordSum\t%f" % (1.0*totalStopWords/totalWords)
