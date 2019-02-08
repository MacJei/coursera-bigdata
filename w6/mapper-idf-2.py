from __future__ import print_function
import sys

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

for line in sys.stdin:
    word, _, _, _ = unicode(line.strip()).split('\t')
    print("reporter:counter:Idf stats,Total words found,%d" % 1, file=sys.stderr)
    print(word, 1, sep='\t')


