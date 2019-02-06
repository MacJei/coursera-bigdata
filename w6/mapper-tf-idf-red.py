from __future__ import print_function
import sys


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode


for line in sys.stdin:
    inVal = unicode(line.strip()).split('\t')
    inValLen = len(inVal)
    #print(inValLen, inVal)
    try:
        if inValLen == 2: # idf data
            print("reporter:counter:Wiki stats,idf words,%d" % 1, file=sys.stderr)
            print(inVal[0], "idf", float(inVal[1]), sep='\t')
        elif inValLen == 3: # tf data
            print("reporter:counter:Wiki stats,tf words,%d" % 1, file=sys.stderr)
            print(inVal[1], "tf", inVal[0], float(inVal[2]), sep='\t')
        else:
            print("reporter:counter:Wiki stats,tf idf parsing errors,%d" % 1, file=sys.stderr)
    except ValueError as e:
        print("reporter:counter:Wiki stats,tf idf to float errors,%d" % 1, file=sys.stderr)
        continue
