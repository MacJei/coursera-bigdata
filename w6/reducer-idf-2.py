import sys
from math import log

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

current_key = None
word_sum = 0
tag = "idf"

for line in sys.stdin:
    try:
        key, count = unicode(line.strip()).split('\t', 1)
        if key == "" or count == "":    # sanity check
            continue
        count = int(count)
    except ValueError as e:
        continue
    if current_key != key:
        if current_key:
            print "%s\t%s\t%f" % (current_key, tag, (1.0/log(1.0 + word_sum)))
        word_sum = 0
        current_key = key
    word_sum += count

if current_key:
    print "%s\t%s\t%f" % (current_key, tag, (1.0/log(1.0 + word_sum)))