import sys


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

current_article_id = None
current_word = None
word_sum, wordsInArticle = 0, 0

tagWord = 'wordN'
tagWords = 'totalWordsNt'
tagTf = 'tf'

for line in sys.stdin:
    try:
        article_id, tag, word, count = unicode(line.strip()).split('\t')
        #print "after parse:", article_id, word, count
        if article_id == "" or tag == "" or word == "" or count == "":   # sanity check
            continue
        count = int(count)
    except ValueError as e:
        #print "Parse error:", e
        continue

    if current_article_id != article_id:
        if tag == tagWords: # get total words in article
            wordsInArticle = count
            continue
        if current_article_id != None:
            print "%s\t%s\t%s\t%f" % (current_word, tagTf, current_article_id, 1.0*word_sum/wordsInArticle)
            word_sum = 0
            current_word = word
        current_article_id = article_id
        #print "wordsInArticle:", word, wordsInArticle
        
    if current_word != word:
        if current_word != None:
            print "%s\t%s\t%s\t%f" % (current_word, tagTf, current_article_id, 1.0*word_sum/wordsInArticle)
            #print "%s\t%s\t%d\t%d" % (current_article_id, current_word, word_sum, wordsInArticle)
        word_sum = 0
        current_word = word
    word_sum += count

if current_article_id:
    print "%s\t%s\t%s\t%f" % (current_word, tagTf, current_article_id, 1.0*word_sum/wordsInArticle)
