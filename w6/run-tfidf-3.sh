#!/bin/bash
python mapper-tfidf-3.py < wiki-test.txt 2> map-tfidf.err | (unset LC_ALL; LC_CTYPE=en_US.UTF-8 LC_COLLATE=C sort -t$'\t' -k1,2) | python reducer-tfidf-3.py > tfidf.out

