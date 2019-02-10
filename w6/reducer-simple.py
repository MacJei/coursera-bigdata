import sys


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode


for line in sys.stdin:
    print line.strip()


