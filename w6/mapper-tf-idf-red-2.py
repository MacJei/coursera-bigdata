from __future__ import print_function
import sys


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

tf = "tf"
idf = "idf"

for line in sys.stdin:
    inVal = unicode(line.strip()).split('\t')
    if len(inVal) > 4:
        print("reporter:counter:Wiki stats,tf idf > 4 parsing errors,%d" % 1, file=sys.stderr)
        continue
    try:
        if inVal[1] == idf: # idf data
            print("reporter:counter:Wiki stats,idf words,%d" % 1, file=sys.stderr)
            print(inVal[0], idf, float(inVal[2]), sep='\t')
            
        elif inVal[1] == tf: # tf data
            print("reporter:counter:Wiki stats,tf words,%d" % 1, file=sys.stderr)
            print(inVal[0], tf, inVal[2], float(inVal[3]), sep='\t')
            
        else:
            print("reporter:counter:Wiki stats,tf idf last else parsing errors,%d" % 1, file=sys.stderr)
    except ValueError as e:
        print("reporter:counter:Wiki stats,tf idf to float errors,%d" % 1, file=sys.stderr)
        continue
