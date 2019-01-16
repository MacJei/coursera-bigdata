#! /usr/bin/env python

import sys

# Your functions may be here.



if __name__ == '__main__':
    # Your code here.
    for line in sys.stdin:
        try:
            _, wordSum, stopWordSum = line.strip().split('\t')
        except:
            continue
        totalWords = int(wordSum)
        totalStopWords = int(stopWordSum)
        percentStopWords = 100.0 * totalStopWords/totalWords
    
    print "{:.5}".format(percentStopWords)
