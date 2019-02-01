import sys

current_article_id = None
current_word = None
word_sum, wordsInArticle = 0, 0

for line in sys.stdin:
    try:
        article_id, word, count = line.strip().split('\t')
        #print "after parse:", article_id, word, count
        count = int(count)
    except ValueError as e:
        #print "Parse error:", e
        continue
    if current_article_id != article_id:
        wordsInArticle = count  # first string is always words in article count
        current_article_id = article_id
        current_word = None
        print "wordsInArticle:", word, wordsInArticle
        continue
    if current_word != word:
        if current_word != None: 
            print "%s\t%s\t%f" % (current_article_id, current_word, 1.0*word_sum/wordsInArticle)
        word_sum = 0
        current_word = word
    word_sum += count

if current_article_id:
    print "%s\t%s\t%f" % (current_article_id, word, 1.0*word_sum/wordsInArticle)