import sys
from math import log

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

tf = "tf"
idf = "idf"

for line in sys.stdin:
    inVal = unicode(line.strip()).split('\t')
    if (len(inVal) < 2 and len(inVal) > 4):      # sanity check
        continue
    try:
        if inVal[1] == idf:
            idfWord, _, idfDt = inVal
            idfDt = float(idfDt)

        if inVal[1] == tf:
            tfWord, _, article_id, tfNt = inVal
            tfNt = float(tfNt)
            if idfWord == tfWord:
                print "%s\t%s\t%f" % (idfWord, article_id, tfNt*idfDt)

    except ValueError as e:
        continue


