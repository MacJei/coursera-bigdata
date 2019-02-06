#!/bin/bash
python mapper-idf.py < tf.out 2> map-idf.err | (unset LC_ALL; LC_CTYPE=en_US.UTF-8 LC_COLLATE=C sort -t$'\t' -k1,2) | python reducer-idf.py > idf.out

